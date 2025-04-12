#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path

def update_file(file_path: Path, content: str, append: bool = False) -> dict:
    """
    Updates a file with the provided content.
    If append=True, appends the content to the file.
    Returns a status dictionary with success flag and message.
    """
    result = {"path": str(file_path), "success": False, "message": ""}
    
    try:
        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Update the file
        mode = 'a' if append else 'w'
        with open(file_path, mode, encoding='utf-8') as f:
            f.write(content)
        
        result["success"] = True
        result["message"] = f"{'Appended to' if append else 'Updated'} {file_path}"
    except Exception as e:
        result["message"] = f"Error updating {file_path}: {e}"
    
    return result

def main():
    parser = argparse.ArgumentParser(description="Update memory bank files in a single operation.")
    parser.add_argument("--mode-slug", required=True, help="The slug of the mode (e.g., 'code', 'tdd').")
    parser.add_argument("--memory-path", default="memory-bank", help="Path to the memory-bank directory.")
    parser.add_argument("--active-context", help="Content to update in activeContext.md.")
    parser.add_argument("--global-context", help="Content to update in globalContext.md.")
    parser.add_argument("--mode-specific", help="Content to update in mode-specific/<mode-slug>.md.")
    parser.add_argument("--feedback", help="Content to update in feedback/<mode-slug>-feedback.md.")
    parser.add_argument("--maintenance", help="Content to update in maintenance.md (will be created if it doesn't exist).")
    parser.add_argument("--append", action="store_true", help="Append to files instead of overwriting.")
    parser.add_argument("--commit", action="store_true", help="Automatically commit changes to git with descriptive message.")
    args = parser.parse_args()

    memory_base_path = Path(args.memory_path)
    mode_slug = args.mode_slug
    results = []

    if not memory_base_path.is_dir():
        print(f"Error: Memory bank directory not found at '{memory_base_path}'")
        return

    # Update files based on provided arguments
    if args.active_context:
        results.append(update_file(memory_base_path / "activeContext.md", args.active_context, args.append))
    
    if args.global_context:
        results.append(update_file(memory_base_path / "globalContext.md", args.global_context, args.append))
    
    if args.mode_specific:
        mode_specific_path = memory_base_path / "mode-specific" / f"{mode_slug}.md"
        results.append(update_file(mode_specific_path, args.mode_specific, args.append))
    
    if args.feedback:
        feedback_path = memory_base_path / "feedback" / f"{mode_slug}-feedback.md"
        results.append(update_file(feedback_path, args.feedback, args.append))
    
    if args.maintenance:
        results.append(update_file(memory_base_path / "maintenance.md", args.maintenance, args.append))
    
    # Print results
    for result in results:
        status = "✅" if result["success"] else "❌"
        print(f"{status} {result['message']}")
    
    # Handle git commit if requested
    if args.commit and results and any(r["success"] for r in results):
        try:
            import subprocess
            
            # Get repo root
            repo_root = memory_base_path
            while repo_root.parent != repo_root and not (repo_root / ".git").exists():
                repo_root = repo_root.parent
            
            if not (repo_root / ".git").exists():
                print("❌ Not a git repository. Skipping commit.")
                return
                
            # Stage changes to memory bank files
            subprocess.run(["git", "-C", str(repo_root), "add", str(memory_base_path)], check=True)
            
            # Commit with descriptive message
            commit_msg = f"Update memory bank for {mode_slug} mode"
            if args.append:
                commit_msg = f"Append to memory bank for {mode_slug} mode"
            
            subprocess.run(["git", "-C", str(repo_root), "commit", "-m", commit_msg], check=True)
            print(f"✅ Committed changes to git: '{commit_msg}'")
        except Exception as e:
            print(f"❌ Error during git commit: {e}")

if __name__ == "__main__":
    main()