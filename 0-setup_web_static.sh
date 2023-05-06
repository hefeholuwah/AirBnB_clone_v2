#!/usr/bin/env bash

# Update package lists and install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Allow HTTP traffic through UFW firewall
sudo ufw allow 'Nginx HTTP'

# Create directories for static files and set up test file
sudo mkdir -p /data/web_static/releases/test
sudo chown -R $USER:$USER /data/web_static/shared
echo "This is a test page" | sudo tee /data/web_static/releases/test/index.html

# Set up Nginx virtual host for static files
sudo cp /data/web_static/releases/test /data/web_static/current
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
sudo systemctl restart nginx
