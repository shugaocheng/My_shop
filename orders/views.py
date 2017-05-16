from django.shortcuts import render,redirect
from .models import OrderItem,Order
from .forms import OrderCreateForm
from .tasks import order_created
from shoppingcart.shoppingcart import ShoppingCart
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def order_create(request):
    order_items = Order.objects.filter(user_id=request.user.id)
    items =[ order for order in order_items]
    shopping_cart = ShoppingCart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_order = form.save(commit=False)
            new_order.paid = True
            new_order.user = request.user
            new_order = form.save(commit=False)
            if shopping_cart.coupon:
                new_order.coupon = shopping_cart.coupon
                new_order.discount = shopping_cart.coupon.discount
            new_order.save()
            # 为购物车每件商品创建数据库实例信息
            for item in shopping_cart:
                OrderItem.objects.create(order=new_order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # 清空购物车
            shopping_cart.clear()
            # 调用异步任务
            # order_created.delay(new_order.id)
            return render(request,'orders/order/created.html',{'order':new_order})
    else:
        form = OrderCreateForm(initial={'first_name':items[0].first_name,'last_name':items[0].last_name,'email':items[0].email})
    return render(request,
                  'orders/order/create.html',
                  {'shopping_cart':shopping_cart,
                   'form':form})


def order_detail(request):
    order_detail = OrderItem.objects.all()
    order = Order.objects.filter(paid=True,user=request.user.id)
    if order:
        order_detail = order_detail.filter(order=order)
    return render(request,
                  'orders/order/order_detail.html',
                  {'order_detail':order_detail})


def order_delete(request,order_id):
    # order = OrderItem.objects.filter(id=order_id)
    Order.objects.get(id=order_id).delete()
    return redirect('orders:order_detail')
