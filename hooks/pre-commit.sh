#!/usr/bin/env bash

branch=$(git symbolic-ref --short head)
if [[ "$branch" == "main" ]]; then
    echo "Commit on main is now allowed. Please use a feature branch."
    exit 1
fi
exit 0
