server {
  listen        80;
  server_name   blog.aweffr.com;
  return 302    https://$host$request_uri;
}


# Default server configuration
server {
  server_name blog.aweffr.com;

	# SSL configuration
	listen                  443 ssl;
  ssl_certificate         certs/aweffr.com/fullchain;
  ssl_certificate_key     certs/aweffr.com/key;
  ssl_trusted_certificate certs/aweffr.com/fullchain;

  ssl_protocols          TLSv1.2 TLSv1.3;
  ssl_ciphers            ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;

  # OCSP Stapling
  ssl_stapling           on;
  ssl_stapling_verify    on;
  resolver               1.1.1.1 1.0.0.1 8.8.8.8 8.8.4.4 208.67.222.222 208.67.220.220 valid=60s;
  resolver_timeout       2s;

  # 启用 session resumption 提高HTTPS性能
  # http://vincent.bernat.im/en/blog/2011-ssl-session-reuse-rfc5077.html
  ssl_session_cache shared:SSL:50m;
  ssl_session_timeout 1d;
  ssl_session_tickets off;

  # DHE密码器的Diffie-Hellman参数, 推荐 2048 位
  ssl_dhparam certs/aweffr.com/dhparam.pem;

  client_max_body_size 1536m;

  # gzip
  gzip            on;
  gzip_vary       on;
  gzip_proxied    any;
  gzip_comp_level 6;
  gzip_types      text/plain text/css text/xml application/json application/javascript application/rss+xml application/atom+xml image/svg+xml;

  # favicon.ico
  location = /favicon.ico {
    log_not_found off;
    access_log    off;
  }

  # robots.txt
  location = /robots.txt {
    log_not_found off;
    access_log    off;
  }

  location /static/ {
    root /data/aweffr_com;
  }

  location /media/protected/ {
    internal;
    root /data/aweffr_com;
  }

  location /media/ {
    root /data/aweffr_com;
  }

  location / {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;

    proxy_pass http://127.0.0.1:9001;
  }

  include includes/letsencrypt-webroot;
}
