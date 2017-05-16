import os
from django.conf import settings
from celery import Celery,task
from orders import tasks
# 设置DJANGO_SETTINGS_MODULE 变量
# os.environ['DJANGO_SETTINGS_MODULE'] = 'myshop.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myshop.settings')
# 创建实例
app = Celery('myshop')
celery = Celery('myshop')
# 加载项目设置中任意的定制化配置
app.config_from_object('django.conf:settings')
# 自动查找在INSTALLED_APPS中的异步应用任务,Celery将在每个应用路径下查找tasks.py加载其中的异步任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
