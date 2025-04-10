#!/bin/bash
# Script to download Roo Code documentation from GitHub

# Target directory
TARGET_DIR="/home/rookslog/roo-mode-factory/library/docs/roocode"
mkdir -p "$TARGET_DIR"

# Download root markdown files
echo "Downloading root markdown files..."
curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/docs/index.md" -o "$TARGET_DIR/index.md"
curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/docs/faq.md" -o "$TARGET_DIR/faq.md"
curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/docs/community.md" -o "$TARGET_DIR/community.md"
curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/docs/tips-and-tricks.md" -o "$TARGET_DIR/tips-and-tricks.md"
curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/docs/tutorial-videos.mdx" -o "$TARGET_DIR/tutorial-videos.mdx"
curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/docs/tutorial-videos.json" -o "$TARGET_DIR/tutorial-videos.json"

# Function to download directory content
download_directory() {
    local dir_path="$1"
    local target_subdir="$2"
    
    # Create target subdirectory
    mkdir -p "$TARGET_DIR/$target_subdir"
    
    # Get directory listing using GitHub API
    echo "Getting contents of $dir_path..."
    local dir_contents=$(curl -s "https://api.github.com/repos/RooVetGit/Roo-Code-Docs/contents/$dir_path")
    
    # Extract file paths and download each file
    echo "$dir_contents" | grep -o '"path": "[^"]*"' | cut -d'"' -f4 | while read -r file_path; do
        # Check if it's a file or directory
        local item_type=$(echo "$dir_contents" | grep -A1 "\"path\": \"$file_path\"" | grep "\"type\":" | cut -d'"' -f4)
        local file_name=$(basename "$file_path")
        
        if [ "$item_type" = "file" ]; then
            echo "Downloading $file_path..."
            curl -s "https://raw.githubusercontent.com/RooVetGit/Roo-Code-Docs/main/$file_path" -o "$TARGET_DIR/$target_subdir/$file_name"
        elif [ "$item_type" = "dir" ]; then
            # Recursively download subdirectory
            download_directory "$file_path" "$target_subdir/$file_name"
        fi
    done
}

# Download each main section directory
echo "Downloading advanced-usage directory..."
download_directory "docs/advanced-usage" "advanced-usage"

echo "Downloading basic-usage directory..."
download_directory "docs/basic-usage" "basic-usage"

echo "Downloading features directory..."
download_directory "docs/features" "features"

echo "Downloading getting-started directory..."
download_directory "docs/getting-started" "getting-started"

echo "Downloading providers directory..."
download_directory "docs/providers" "providers"

echo "Downloading troubleshooting directory..."
download_directory "docs/troubleshooting" "troubleshooting"

echo "Downloading update-notes directory..."
download_directory "docs/update-notes" "update-notes"

echo "Documentation download complete!"