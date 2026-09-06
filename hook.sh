#!/usr/bin/env bash

# Set the log file path
LOG_FILE=~/.claude/hooks/blocked.log

# Define the patterns to block
BLOCKED_COMMANDS=('rm -rf' 'DROP TABLE' 'git push --force' 'TRUNCATE' 'DELETE FROM')

# Create the log file if it doesn't exist
mkdir -p $(dirname ${LOG_FILE})
touch ${LOG_FILE}

# Set up a pre-hook function
pre_hook() {
local command=$1
if [[ "${BLOCKED_COMMANDS[@]} =~ ${command}" ]]; then
echo "[$(date +'%Y-%m-%d %H:%M:%S')] Blocked command: $command" >>${LOG_FILE}
echo "Command blocked. Please use a more safe alternative."
fi
}

# Hook the bash commands
pre_hook "$@"
