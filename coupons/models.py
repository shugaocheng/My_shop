from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Coupons(models.Model):
    code = models.CharField(max_length=50,unique=True)  # 优惠劵代码
    valid_form = models.DateTimeField()     # 优惠券生效时间
    valid_to = models.DateTimeField()       # 优惠券过期时间
    discount = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)]) # 折扣率
    active = models.BooleanField(default=True)  # 是否有效

    def __str__(self):
        return self.code
