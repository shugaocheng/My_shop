from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.

# 使用TabularInline把这个模型引用为OrderAdmin的内联元素,这样就可以在一个页面编辑product模型和Order模型
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','address','postal_code','city','paid','created','updated']
    list_filter = ['paid','created','updated']
    inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin)