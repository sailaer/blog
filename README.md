
部署文档

使用centos7，腾讯云，其他服务器大同小异

首先在服务器上安装git

然后执行命令git源码服务器

然后安装

easy_install -i http://pypi.douban.com/simple virtualenv

创建虚拟环境

virtualenv venv

安装pip

easy_install -i http://pypi.douban.com/simple pip

激活虚拟环境

source venv/bin/activate

然后安装支持库

pip install -r requirements.txt

解决编码问题
Python27\Lib\site-packages下创建文件sitecustomize.py

import sys

reload(sys)

sys.setdefaultencoding('utf-8')   #  或gb2312

然后部署数据库

python manage.py db upgrade

然后运行

gunicorn -b 0.0.0.0:80 manage:app

成功。

ps：使用netstat -antup | grep命令可以查找关闭程序。、
    unbuntu需要sudo权限。