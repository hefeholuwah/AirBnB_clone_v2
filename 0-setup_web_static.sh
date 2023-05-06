#!/usr/bin/env bash

# Update package lists and install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Allow HTTP traffic through UFW firewall
sudo ufw allow 'Nginx HTTP'

# Create directories for static files and set up test file
sudo mkdir -p /var/www/html/test
sudo chown -R $USER:$USER /var/www/html
echo "This is a test page" | sudo tee /var/www/html/test/index.html

# Set up Nginx virtual host for static files
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
sudo sed -i '/^}/i \\tlocation /static/ {\n\t\talias /var/www/html/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo systemctl restart nginx
