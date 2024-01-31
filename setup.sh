#! /usr/bin/env bash

# download required files
echo "Setting up the container..."
if [ -f "Dockerfile" ]; then
    echo "Dockerfile already exists!"
    prompt="Do you want to overwrite it? [y/n] "
    read -p "$prompt" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm Dockerfile
    else
        echo "Aborting..."
        exit 1
    fi
fi
git clone https://github.com/rambasnet/course-container.git
rm -rf course-container/.git
rm course-container/README.md
rm course-container/setup.sh
rm course-container/.gitignore
rm course-container/LICENSE
cp -r course-container/. ./
rm -rf course-container
git config core.hooksPath .githooks
echo "Downloaded required files. Container ready!"
