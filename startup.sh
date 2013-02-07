#!/bin/sh
PATH="/bin:/usr/bin:/sbin:/usr/sbin:/jffs/usa"

# Restart DD-WRT on Port 81
killall -q httpd
httpd -p 81 -h /www

# Start mini_httpd
killall mini_httpd
mini_httpd -p "80" -c "**.cgi" -u root -d "/jffs/usa/www" -l /tmp/mini_httpd.log
