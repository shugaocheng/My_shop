from django.db import models
from shop.models import Product
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from coupons.models import Coupons
from decimal import Decimal
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,related_name='user_order',db_index=True,verbose_name='用户')
    first_name = models.CharField(max_length=50,verbose_name='姓氏')
    last_name = models.CharField(max_length=50,verbose_name='名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=200,verbose_name='收货地址')
    postal_code = models.CharField(max_length=20,verbose_name='邮政编码')
    city = models.CharField(max_length=100,verbose_name='所在城市')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='最后修改时间')
    paid = models.BooleanField(default=False,verbose_name='订单状态')   # 判断已完成和未完成订单
    coupon = models.ForeignKey(Coupons,related_name='orders',null=True,blank=True)
    discount = models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)])
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    # 得到所有商品的总消费
    def get_total_cost(self):
        total_cost =  sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount  / Decimal('100'))

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items')
    product = models.ForeignKey(Product,related_name='order_items')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    # 得到某件商品的总消费
    def get_cost(self):
        return self.price * self.quantity