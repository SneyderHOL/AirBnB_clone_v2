#!/usr/bin/env bash
#Bash script that sets up the web server for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
echo "Testing configuration" > /data/web_static/releases/test/index.html
sudo mkdir -p /data/web_static/shared/
sudo rm -fr /data/web_static/current
sudo ln -sfT /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "/default_server;/ a location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}/" /etc/nginx/sites-available/default
sudo service nginx restart
