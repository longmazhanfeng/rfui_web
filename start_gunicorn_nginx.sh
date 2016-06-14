#!/bin/sh
# 启动gunicorn服务和nginx代理服务
cd /Users/netease/Desktop/rf-djangoweb
nginx -s stop
nginx
gunicorn -c gunicorn.conf.py myaccoutsite.wsgi