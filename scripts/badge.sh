#!/bin/bash

# pass --remote or -r flag to catch last update from remote repository
# or leave blank to catch last update from local repository

color=green

# Check if the first argument is "--remote" or "-r"
if [[ "$1" == "--remote" || "$1" == "-r" ]]; then
    # Fetch from remote repository

    # GitHub username and repository name
    username="SHEscher"
    repository="scilaunch"

    # Fetch the repository's information using the GitHub API
    response=$(curl -s "https://api.github.com/repos/${username}/${repository}")

    # Extract the last commit date from the response
    last_commit_date=$(echo "${response}" | jq -r '.pushed_at')

    # Format the date in a desired format (e.g., YYYY-MM-DD or Mon DD, YYYY))
    # formatted_date=$(date -j -f "%Y-%m-%dT%H:%M:%SZ" "${last_commit_date}" +"%Y--%m--%d")
    formatted_date=$(date -j -f "%Y-%m-%dT%H:%M:%SZ" "${last_commit_date}" +"%b_%d,_%Y")

else
    # Do on local repository

    # Get the absolute path of the script's directory
    script_path=$(dirname "$(readlink -f "$0")")
    # go now in parent directory (repo_root/scripts -> repo_root/)
    repository_path=$(dirname "${script_path}")

    # Ensure to be in repository directory
    cd "${repository_path}" || exit

    # Fetch the last commit date using Git
    last_commit_date=$(git log -1 --format=%ci)

    # Format the date in a desired format (e.g., YYYY-MM-DD or Mon DD, YYYY))
    # formatted_date=$(date -j -f "%Y-%m-%d %H:%M:%S %z" "${last_commit_date}" +"%Y--%m--%d")
    formatted_date=$(date -j -f "%Y-%m-%d %H:%M:%S %z" "${last_commit_date}" +"%b_%d,_%Y")

fi

# Generate the badge using shields.io
badge_url="https://img.shields.io/badge/last_update-${formatted_date}-$color"

# Output the badge URL
echo "${badge_url}"

# Replace the old badge URL in the README.md file
sed -i '' "s|https://img.shields.io/badge/last_update-.*-$color|${badge_url}|g" README.md
# If it is not present then this has no effect

# Commit the changes
git commit README.md -m "Update 'last-update' badge in README.md"
