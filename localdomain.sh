#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 [domain-name] [port]"
    exit 1
fi

DOMAIN_NAME=$1
PORT=$2

# Add domain to /etc/hosts
if ! grep -q "127.0.0.1 $DOMAIN_NAME" /etc/hosts; then
    echo "Adding $DOMAIN_NAME to /etc/hosts..."
    echo "127.0.0.1 $DOMAIN_NAME" | sudo tee -a /etc/hosts
else
    echo "$DOMAIN_NAME is already in /etc/hosts."
fi

# Create Nginx server configuration
NGINX_CONFIG_DIR="/opt/homebrew/etc/nginx/servers"
NGINX_CONFIG_FILE="$NGINX_CONFIG_DIR/$DOMAIN_NAME.conf"

if [ ! -d "$NGINX_CONFIG_DIR" ]; then
    echo "Nginx configuration directory not found: $NGINX_CONFIG_DIR"
    exit 1
fi

echo "Creating Nginx server configuration for $DOMAIN_NAME..."
sudo tee "$NGINX_CONFIG_FILE" > /dev/null <<EOL
server {
    listen 80;
    server_name $DOMAIN_NAME;

    location / {
        proxy_pass http://localhost:$PORT;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOL

# Restart Nginx
echo "Restarting Nginx..."
brew services restart nginx

echo "Setup complete! You can now access http://$DOMAIN_NAME."
