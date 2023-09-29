#!/usr/bin/env bash

GIT_DIR=$(git rev-parse --git-dir)

echo "Installing hooks..."
# this command creates symlink to our pre-commit script
ln -s ../../hooks/pre-commit.sh $GIT_DIR/hooks/pre-commit
chmod +x ./hooks/pre-commit.sh
chmod +x ./hooks/run-test.sh
echo "Done"!
