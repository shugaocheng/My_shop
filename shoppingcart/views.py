from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .shoppingcart import ShoppingCart
from .forms import ShoppingCartAddProductForm
from coupons.models import Coupons
from coupons.forms import CouponsForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
# Create your views here.

# 只响应POST状态的请求
# @require_POST
# @login_required
def shopping_cart_add(request,product_id):
    # 初始化购物车的信息,生成购物车会话ID
    shopping_cart = ShoppingCart(request)
    product = get_object_or_404(Product,id=product_id)
    form = ShoppingCartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shopping_cart.add(product=product,
                          # user=username,
                          quantity=cd['quantity'],
                          update_quantity=cd['update'])
    # 重定向到该视图
    return redirect('shopping_cart:shopping_cart_detail')

def shopping_cart_remove(request,product_id):
    shopping_cart = ShoppingCart(request)
    product = get_object_or_404(Product,id=product_id)
    shopping_cart.remove(product)
    return redirect('shopping_cart:shopping_cart_detail')


# 购物车详情
def shopping_cart_detail(request):
    shopping_cart = ShoppingCart(request)
    for item in shopping_cart:
        item['update_quantity_form'] = ShoppingCartAddProductForm(initial={'quantity':item['quantity'],'update':True})
    # 引入优惠券表单
    coupon_apply_form = CouponsForm()
    return render(request,
                  'shopping_cart/detail.html',
                  {'shopping_cart':shopping_cart,
                   'coupon_apply_form':coupon_apply_form})