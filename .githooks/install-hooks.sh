#!/usr/bin/env bash

GIT_DIR=$(git rev-parse --git-dir)

echo "Installing hooks..."
# this command creates symlink to our pre-commit script
ln -s ../../hooks/pre-commit.sh $GIT_DIR/hooks/pre-commit
ln -s ../../hooks/pre-push.sh $GIT_DIR/hooks/pre-push
chmod +x ./hooks/pre-commit.sh
chmod +x ./hooks/pre-push.sh
chmod +x ./hooks/run-test.sh
echo "Done"!
