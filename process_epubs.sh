#!/bin/bash

# Script to find EPUB files and process them using pipelines/rag_ingestion.py
# Allows specifying a custom output file format.

# --- Default Values ---
DEFAULT_OUTPUT_FORMAT=".rag.md"
PYTHON_SCRIPT="pipelines/rag_ingestion.py"

# --- Function Definitions ---
usage() {
  echo "Usage: $0 <input_directory> <output_directory> [-f|--output-format <extension>]"
  echo "  input_directory:  Directory containing EPUB files (searched recursively)."
  echo "  output_directory: Directory where processed files will be saved."
  echo "  -f, --output-format: Optional output file extension (e.g., .txt). Defaults to '${DEFAULT_OUTPUT_FORMAT}'."
  exit 1
}

print_error() {
  echo "Error: $1" >&2
  exit 1
}

# --- Argument Parsing ---
INPUT_DIR=""
OUTPUT_DIR=""
OUTPUT_FORMAT="${DEFAULT_OUTPUT_FORMAT}"

# Use getopt for robust argument parsing
TEMP=$(getopt -o f: --long output-format:,help -n "$0" -- "$@")
if [ $? != 0 ]; then usage; fi
eval set -- "$TEMP"
unset TEMP

while true; do
  case "$1" in
    '-f'|'--output-format')
      OUTPUT_FORMAT="$2"
      shift 2
      ;;
    '--help')
      usage
      ;;
    '--')
      shift
      break
      ;;
    *)
      # Should not happen with getopt
      print_error "Internal error parsing arguments!"
      ;;
  esac
done

# Remaining arguments are input and output directories
INPUT_DIR="$1"
OUTPUT_DIR="$2"

# --- Validation ---
if [ -z "$INPUT_DIR" ] || [ -z "$OUTPUT_DIR" ]; then
  echo "Error: Input and output directories are mandatory."
  usage
fi

if [ ! -d "$INPUT_DIR" ]; then
  print_error "Input directory '$INPUT_DIR' does not exist or is not a directory."
fi

if [ ! -f "$PYTHON_SCRIPT" ]; then
    print_error "Python script '$PYTHON_SCRIPT' not found."
fi

if [ ! -x "$PYTHON_SCRIPT" ]; then
    print_error "Python script '$PYTHON_SCRIPT' is not executable. Please run: chmod +x $PYTHON_SCRIPT"
fi

# Validate output format
if [[ ! "$OUTPUT_FORMAT" =~ ^\. ]]; then
    print_error "Invalid output format '$OUTPUT_FORMAT'. Must start with a dot (e.g., .txt, .md)."
fi

# Check and create output directory
if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Output directory '$OUTPUT_DIR' does not exist. Attempting to create..."
  mkdir -p "$OUTPUT_DIR"
  if [ $? -ne 0 ]; then
    print_error "Failed to create output directory '$OUTPUT_DIR'."
  fi
  echo "Output directory '$OUTPUT_DIR' created successfully."
fi

# --- Processing ---
echo "Starting EPUB processing..."
echo "Input Directory:  $INPUT_DIR"
echo "Output Directory: $OUTPUT_DIR"
echo "Output Format:    $OUTPUT_FORMAT"
echo "Python Script:    $PYTHON_SCRIPT"
echo "---"

processed_count=0
error_count=0

# Use find and process substitution for robust file handling
while IFS= read -r epub_file; do
  echo "Processing file: $epub_file"

  # Get base filename without extension
  base_name=$(basename "$epub_file" .epub)
  # Construct output filename and path
  output_filename="${base_name}${OUTPUT_FORMAT}"
  output_path="${OUTPUT_DIR}/${output_filename}"

  # --- IMPORTANT ASSUMPTION ---
  # This assumes pipelines/rag_ingestion.py has been modified to accept
  # the full output path as the second argument, instead of just the output directory.
  # Example Python argparse modification needed:
  # parser.add_argument("output_path", help="Full path for the output file.")
  # And update the saving logic in run_pipeline function.
  # ---

  # Execute the Python script
  "$PYTHON_SCRIPT" "$epub_file" "$output_path"

  if [ $? -eq 0 ]; then
    echo "Successfully processed '$epub_file' -> '$output_path'"
    ((processed_count++))
  else
    echo "Error processing '$epub_file'. Check script output above." >&2
    ((error_count++))
  fi
  echo "---"

done < <(find "$INPUT_DIR" -iname '*.epub' -print) # Case-insensitive search

echo "Processing complete."
echo "Total files processed successfully: $processed_count"
if [ $error_count -gt 0 ]; then
  echo "Total files failed: $error_count" >&2
fi

exit $error_count # Exit with 0 if no errors, >0 otherwise