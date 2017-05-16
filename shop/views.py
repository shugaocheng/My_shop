from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from shoppingcart.forms import ShoppingCartAddProductForm
from orders.models import Order,OrderItem
from .recommender import Recommender
from .forms import SearchForm
from django.db.models import Q
# Create your views here.

# 检索所有商品
def product_list(request,category_slug=None):
    category = None
    # 所有商品类别
    categories = Category.objects.all()
    # 所有有效商品
    products = Product.objects.filter(available=True)
    # 如果商品类别标签不为空
    if category_slug:
        # 根据标签查找该商品类别
        category = get_object_or_404(Category,slug=category_slug)
        # 有效商品根据标签类别进行过滤,查出该类别所有有效商品
        products = products.filter(category=category)
    return render(request,'shop/product/list.html',
                  {'category':category,
                   'categories':categories,
                   'products':products})

# 检索某个商品
def product_detail(request,id,slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    shopping_cart_product_form = ShoppingCartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product],4)
    return render(request,
                  'shop/product/detail.html',
                  {'product':product,
                   'shopping_cart_product_form':shopping_cart_product_form,
                   'recommended_products':recommended_products})



def get_product(request):
    search = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            search = Product.objects.filter(Q(name__icontains=search)|Q(slug__icontains=search))
            # print(search)
    else:
        form = SearchForm()
    return render(request,
                  'shop/product/search_list.html',
                  {'form':form,'search':search})
