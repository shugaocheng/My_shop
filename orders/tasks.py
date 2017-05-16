from celery import task
from django.core.mail import send_mail
from .models import Order

from django.conf import settings

# celery任务使用task装饰来定义
@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = '订单编号. {}'.format(order.id)
    message = '亲爱的 {},\n\n你已经成功订购该商品.\
              你的订单编号是 {}'.format(order.first_name,order.id)
    mail_sent = send_mail(subject,
                          message,
                          'shugaocheng@163.com',
                          [order.email])
    return mail_sent