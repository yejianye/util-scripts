#!/bin/bash

# Service and command configuration
echo "Checking the status of elasticsearch..."

# Loop until the service is in a running state
while true; do
    # launchctl list | grep -q "^[0-9].*com.ryanye.elasticsearch"
    curl http://127.0.0.1:9200 >& /dev/null
    if [ $? -eq 0 ]; then
    echo "elasticsearch is running. Starting the command..."
    sleep 5
    cd ~/repos/ryclj
    /opt/homebrew/bin/lein ring server-headless
    exit 0
  else
    echo "elasticsearch is not running yet. Retrying in 2 seconds..."
    sleep 2
  fi
done
