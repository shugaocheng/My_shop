from django.contrib import admin
from shop.models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    # 使用prepopulated_fields来指定slug字段,因为该字段会使用其他字段的值来自动生成
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available','created','updated']
    # 设置可编辑的字段,一次可编辑多行,需要和list_display的字段对应
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)