#!/usr/bin/env python3
import argparse
import subprocess
import os
from pathlib import Path
import datetime

def run_command(command, cwd=None):
    """Run a shell command and return the output and error code"""
    result = subprocess.run(command, capture_output=True, text=True, cwd=cwd, shell=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_branch_name(repo_path):
    """Get the current git branch name"""
    stdout, stderr, exit_code = run_command("git rev-parse --abbrev-ref HEAD", cwd=repo_path)
    if exit_code != 0:
        raise Exception(f"Failed to get branch name: {stderr}")
    return stdout

def main():
    parser = argparse.ArgumentParser(description="Complete a feature cycle with proper version control integration.")
    parser.add_argument("--feature-name", required=True, help="Name of the completed feature")
    parser.add_argument("--message", help="Additional commit message")
    parser.add_argument("--repo-path", default=".", help="Path to the git repository")
    parser.add_argument("--tag-version", action="store_true", help="Create a version tag")
    parser.add_argument("--version", help="Version tag (if --tag-version is used)")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running tests before commit")
    parser.add_argument("--create-branch", help="Create and switch to a new branch before committing")
    args = parser.parse_args()

    repo_path = Path(args.repo_path).absolute()
    feature_name = args.feature_name.strip()
    
    print(f"📦 Completing feature cycle for: {feature_name}")
    
    # Check if this is a git repository
    if not (repo_path / ".git").exists():
        print("❌ Not a git repository. Aborting.")
        return 1

    # Get current branch
    try:
        current_branch = get_branch_name(repo_path)
        print(f"🔍 Current branch: {current_branch}")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 1

    # Create new branch if requested
    if args.create_branch:
        branch_name = args.create_branch
        print(f"🔀 Creating new branch: {branch_name}")
        stdout, stderr, exit_code = run_command(f"git checkout -b {branch_name}", cwd=repo_path)
        if exit_code != 0:
            print(f"❌ Failed to create branch: {stderr}")
            return 1
        print(f"✅ Switched to new branch: {branch_name}")

    # Run tests if not skipped
    if not args.skip_tests:
        print("🧪 Running tests before commit...")
        
        # First check if package.json exists and has test script
        if (repo_path / "package.json").exists():
            print("📦 Found package.json, running npm test...")
            stdout, stderr, exit_code = run_command("npm test", cwd=repo_path)
            if exit_code != 0:
                print(f"❌ Tests failed: {stderr}")
                user_input = input("Tests failed. Continue anyway? (y/N): ")
                if user_input.lower() != 'y':
                    return 1
            else:
                print("✅ Tests passed")
        
        # Then check for pytest
        elif (repo_path / "pytest.ini").exists() or list(repo_path.glob("**/test_*.py")):
            print("🐍 Found Python tests, running pytest...")
            stdout, stderr, exit_code = run_command("pytest", cwd=repo_path)
            if exit_code != 0:
                print(f"❌ Tests failed: {stderr}")
                user_input = input("Tests failed. Continue anyway? (y/N): ")
                if user_input.lower() != 'y':
                    return 1
            else:
                print("✅ Tests passed")

    # Check git status
    stdout, stderr, exit_code = run_command("git status --porcelain", cwd=repo_path)
    if not stdout:
        print("ℹ️ No changes to commit.")
    else:
        print(f"📝 Changes to be committed:\n{stdout}")
        
        # Stage all changes
        print("📋 Staging changes...")
        stdout, stderr, exit_code = run_command("git add .", cwd=repo_path)
        if exit_code != 0:
            print(f"❌ Failed to stage changes: {stderr}")
            return 1
            
        # Build commit message
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_msg = f"feat: Complete {feature_name} [{timestamp}]"
        if args.message:
            commit_msg += f"\n\n{args.message}"
            
        # Commit changes
        print(f"💾 Committing with message: {commit_msg}")
        stdout, stderr, exit_code = run_command(f'git commit -m "{commit_msg}"', cwd=repo_path)
        if exit_code != 0:
            print(f"❌ Failed to commit changes: {stderr}")
            return 1
        print("✅ Changes committed successfully")
        
    # Create tag if requested
    if args.tag_version:
        version = args.version if args.version else f"v{datetime.datetime.now().strftime('%Y.%m.%d.%H%M')}"
        tag_message = f"Version {version} - {feature_name}"
        
        print(f"🏷️ Creating tag: {version}")
        stdout, stderr, exit_code = run_command(f'git tag -a "{version}" -m "{tag_message}"', cwd=repo_path)
        if exit_code != 0:
            print(f"❌ Failed to create tag: {stderr}")
            return 1
        print(f"✅ Tag created: {version}")
    
    print(f"✨ Feature cycle completed: {feature_name}")
    print("💡 Suggestions for next steps:")
    print("  • Push changes with: git push origin <branch-name>")
    if args.tag_version:
        print(f"  • Push tags with: git push origin {version}")
    print("  • Create a pull request if working on a feature branch")
    
    return 0

if __name__ == "__main__":
    exit(main())