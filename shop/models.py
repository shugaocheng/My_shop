from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

# 商品类别
class Category(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='类别名称')  # db_index 索引
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)        # 唯一

    class Meta:
        ordering = ('name',)
        # 给Category模型取名为'category'
        verbose_name = 'category'
        # 指定模型的复数形式,如果不指定会自动在模型名称后面加一个's'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # 构建商品类别的url
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

# 商品详情
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products')
    name = models.CharField(max_length=200,db_index=True)                   # 商品名称
    slug = models.SlugField(max_length=200,db_index=True)                   # 商品标签
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)     # 商品图片
    description = models.TextField(blank=True)                              # 商品描述
    price = models.DecimalField(max_digits=10,decimal_places=2)             # 商品价格(十进制,max_digits设定最大值,decimal_places设定最小值)
    stock = models.PositiveIntegerField()                                   # 正整数字段,存储库存
    available = models.BooleanField(default=True)                           # 是否可购买
    created = models.DateTimeField(auto_now_add=True)                       # 创建时间
    updated = models.DateTimeField(auto_now=True)                           # 最后更新时间

    class Meta:
        ordering = ('name',)
        # 指定id,slug使用共同索引,可使用这两个字段来查询商品
        index_together = (('id','slug'),)


    def __str__(self):
        return self.name

    # 构建单一商品的url
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id,self.slug])