#!/bin/bash

# Function to check and commit changes in a repository
commit_changes() {
    local repo_path="$1" # The first argument is the repository path

    echo "Checking repository at $repo_path..."

    # Navigate to the repository's directory
    cd "$repo_path" || exit

    # Check for untracked files or changes in the working tree
    if git status --porcelain | grep .; then
        # If output exists, there are changes
        echo "Changes detected in $repo_path. Preparing to commit..."

        # Add changes to tracked files and new files to the staging area
        git add .

        # Commit changes with a timestamped message
        git commit -m "Automated commit on $(date)"

        # Optionally, you can push to your remote repository
        # git push origin main

        echo "Changes committed for $repo_path."
    else
        # No changes detected
        echo "No changes detected in $repo_path. Exiting..."
    fi
}

# Loop through each argument provided to the script
echo "========== Auto Commit on $(date) ============="
for repo_path in "$@"; do
    commit_changes "$repo_path"
done
