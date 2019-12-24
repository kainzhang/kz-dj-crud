# Django CRUD 练习：商场管理系统
本系统是基于Django 3.0的简单CRUD练习\
用于完成我的课程作业，以及为初学者提供示范代码\
系统系统了几个模块的CRUD操作和用户登录注册\
如代码存在不规范或者Bug，也欢迎你指出修改\
页面使用LESS添加Style，代码是大一时写的有点混乱
  
## 安装 Django 框架
首先确保安装Python为3.6以上版本，然后使用pip安装：
```	
pip install django==3.0
```

## 运行本系统
创建数据库：
```
python manage.py makemigrations
```
```
python manage.py migrate
```
运行开发服务器:
```
python manage.py runserver
```

## 创建超级用户
Django Admin需要使用Superuser登录:
```
python manage.py createsuperuser
```
根据提示创建超级用户，Admin地址：
```
http://localhost:8000/admin
```
