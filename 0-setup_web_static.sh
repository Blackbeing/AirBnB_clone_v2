#!/usr/bin/env bash
# Setup server for deployment

# Update repos
apt-get update 

# install nginx
apt install nginx -y

# Create required directories
mkdir -p /data/web_static/{releases/test,shared}

# Create dummy html
cat <<'EOF' > /data/web_static/releases/test/index.html
<html>
	<head></head>
	<body>ALX Webservers</body>
</html>
EOF

# Create symbolic link, overwrite if exists
ln -fs /data/web_static/releases/test/ /data/web_static/current

# Change directory ownership
chown -R ubuntu:ubuntu /data/

# Setup nginx to serve static content
cat <<'EOF' > /etc/nginx/sites-enabled/default
server {
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;

	root /user/share/nginx/html;
	index index.html index.htm;

	server_name _;

	location /hbnb_static {
		alias /data/web_static/current/;
	}
	location / {
		try_files $uri $uri/ =404;
	}
}
EOF

# restart nginx
service nginx restart
