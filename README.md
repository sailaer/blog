
部署文档

首先在服务器上安装git
创建文件夹myblog
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
然后部署数据库
python manage.py db upgrade
然后运行
gunicorn manage:app
gunicorn -b 0.0.0.0:80 manage:app

