#!/usr/bin/env bash
current_branch=$(git symbolic-ref --short head)
if [[ $current_branch != "main" ]]; then
  exit 0
fi
echo "Running pre-push hook on main branch"
bash ./hooks/run-test.sh
# $? stores exit value of the last command
if [ $? != 0 ]; then
 echo "Tests must pass before push!"
 exit 1
fi