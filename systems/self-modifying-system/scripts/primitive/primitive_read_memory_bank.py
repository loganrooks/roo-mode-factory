#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
import sys

def format_file_content_primitive(file_path: Path) -> list[str]:
    """
    Reads a file and formats its content with line numbers.
    Self-contained version for primitive script.
    """
    output_lines = []
    if file_path.is_file():
        output_lines.append(f"--- START FILE: {file_path.relative_to(Path.cwd())} ---")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    # Mimic the 'read_file' tool format
                    output_lines.append(f"{i + 1} | {line.rstrip()}")
        except Exception as e:
             output_lines.append(f"Error reading file {file_path}: {e}")
        output_lines.append(f"--- END FILE: {file_path.relative_to(Path.cwd())} ---")
    # else:
        # Optionally add a note if a file doesn't exist
        # output_lines.append(f"--- INFO: File not found: {file_path.relative_to(Path.cwd())} ---")
    return output_lines

def main():
    parser = argparse.ArgumentParser(description="[PRIMITIVE] Concatenate core and mode-specific memory bank files.")
    parser.add_argument("--mode-slug", required=True, help="The slug of the mode (e.g., 'system-strategist').")
    parser.add_argument("--memory-path", default="memory-bank", help="Path to the memory-bank directory.")
    args = parser.parse_args()

    memory_base_path = Path(args.memory_path)
    mode_slug = args.mode_slug

    if not memory_base_path.is_dir():
        print(f"Error: Memory bank directory not found at '{memory_base_path}'", file=sys.stderr)
        sys.exit(1) # Exit with error code

    # Define core files relative to memory_base_path
    core_files = [
        memory_base_path / "activeContext.md",
        memory_base_path / "globalContext.md",
    ]

    # Define mode-specific files relative to memory_base_path
    mode_specific_file = memory_base_path / "mode-specific" / f"{mode_slug}.md"
    feedback_file = memory_base_path / "feedback" / f"{mode_slug}-feedback.md"

    files_to_read = core_files + [mode_specific_file, feedback_file]

    all_output_lines = []
    for file_path in files_to_read:
        # Use the self-contained formatting function
        all_output_lines.extend(format_file_content_primitive(file_path))
        # Add a blank line between file contents for readability
        if all_output_lines and not all_output_lines[-1].startswith("--- INFO"):
             all_output_lines.append("") # Add separator line

    # Print the combined output to stdout
    print("\n".join(all_output_lines))

if __name__ == "__main__":
    main()