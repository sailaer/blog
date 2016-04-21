
# 部署文档

使用ubuntu，腾讯云，其他服务器大同小异

首先在服务器上安装git

然后执行命令git源码服务器

然后安装

 sudo apt-get install python-pip
 sudo apt-get install python-dev
 yum install -y pcre pcre-devel pcre-static

easy_install -i http://pypi.douban.com/simple virtualenv

创建虚拟环境

 virtualenv -p /usr/bin/python3 venv

安装pip

 sudo apt-get install python-pip

easy_install -i http://pypi.douban.com/simple pip

激活虚拟环境

source venv/bin/activate

然后安装支持库

pip install --no-cache-dir -r requirements.txt

解决编码问题
Python27\Lib\site-packages下创建文件sitecustomize.py

import sys

reload(sys)

sys.setdefaultencoding('utf-8')   #  或gb2312

然后部署数据库

python manage.py db upgrade

然后配置uwsgi，ngxin，gunicorn都可以。

[uwsgi]

socket=127.0.0.1:8001

processes=4

threads=2

master=true

pythonpath=/home/ubuntu/blog

module= manage

callable=app

memory-report=true

stats=127.0.0.1:9191


#
# The default server
#
server {
    listen       80 ;
    server_name  115.159.215.174/;
    # charset koi8-r;

    #access_log  logs/host.access.log  main;

    # Load configuration files for the default server block.
    include /etc/nginx/default.d/*.conf;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
	include uwsgi_params;
        uwsgi_pass  127.0.0.1:8001;
	uwsgi_param UWSGI_SCRIPT manage:app;
	uwsgi_param UWSGI_CHDIR  /home/blog;
    }

    error_page  404              /404.html;
    location = /404.html {
        root   /usr/share/nginx/html;
    }

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}


[program:my_flask]
command=/home/ubuntu/venv/bin/uwsgi /home/ubuntu/blog/config.ini

directory=/home/ubuntu/blog


user=root

autostart=true

autorestart=true

stdout_logfile=/home/ubuntu/blog/logs/uwsgi_supervisor.log
~

uwsgi config.ini

gunicorn -b 0.0.0.0:80 manage:app

成功。

ps：使用netstat -antup | grep命令可以查找关闭程序。、
    unbuntu需要sudo权限。