#! /usr/bin/env bash

# download required files
git clone https://github.com/rambasnet/course-container.git
rm -rf course-container/.git
rm course-container/README.md
rm course-container/setup.sh
cp -r course-container/ ./
rm -rf course-container
echo "Downloaded required files"
