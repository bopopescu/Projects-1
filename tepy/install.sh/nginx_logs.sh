#!/bin/bash
pkill -9 nginx
mv  /opt/server/nginx/logs/*  /opt/server/nginx/backup_logs
/opt/server/nginx/sbin/nginx
rsync --delete -vzrtopg -e ssh /opt/server/nginx/baackup_logs/* root@@bakcup:/root/log/23.97.76.216
rm -rf /opt/server/nginx/backup_logs/*

