#! /usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "Working directory is $SCRIPT_DIR"

#chown user:users /home/user/.zsh_history
#chown user:users /home/user/.gitconfig
chown user:users --recursive /home/user/. &> /dev/null
echo "#!/bin/sh" > /home/user/kattis-cli/kattis
echo 'python "${KATTIS_CLI}/submit.py" "$@"' >> /home/user/kattis-cli/kattis
