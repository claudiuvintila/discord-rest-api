#!/bin/bash

PROC_COUNT=$(ps aux | grep -i discord-api | grep server.py | wc -l)

if [[ "$PROC_COUNT" == 0 ]]; then
  echo "Starting script"
  cloudlinux-selector run-script --json --interpreter python --user claudiuv --app-root discord-api --script-name server.py &
fi
