from decimal import Decimal
from shop.models import Product
from django.conf import settings
from coupons.models import Coupons
from django.contrib.auth.models import User
import json


class ShoppingCart(object):
    def __init__(self,request):
        """
        初始化购物车
        """
        self.session = request.session
        self.cookie = request.COOKIES
        # 初始化优惠券ID
        self.coupons_id = self.session.get('coupons_id')
        shopping_cart = self.session.get(settings.CART_SESSION_ID)
        print(request.COOKIES)
        # print(self.session.values())
        if not shopping_cart:
            # 没有购物车,设置空字典=空购物车
            shopping_cart = self.session[settings.CART_SESSION_ID] = {}
        elif 'sessionid' not in self.cookie.keys():
            shopping_cart = self.session[settings.CART_SESSION_ID] = {}
        elif self.cookie['sessionid'] == self.session.session_key:
            shopping_cart = self.session[settings.CART_SESSION_ID]
        self.shopping_cart = shopping_cart
        self.session_key = request.session.session_key



    def __len__(self):
        """
        计算购物车内商品的数量
        """
        return sum(item['quantity'] for item in self.shopping_cart.values())

    def __iter__(self):
        """
        遍历购物车中的商品,从数据库中得到所有商品的详细信息
        """
        product_ids = self.shopping_cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            # print(type(product))
            self.shopping_cart[str(product.id)]['product'] = product

        for item in self.shopping_cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item



    # def get_total_len(self):
    #     return sum(item['quantity'] for item in self.shopping_cart.values())


    def add(self,product,quantity=1,update_quantity=False):
        """
        将产品添加到购物车或更新其数量
        """
        product_id = str(product.id)
        # username_id = str(user.id)
        # username = User.objects.filter(id__in=username_id)
        # print(username)
        # if username_id not in self.shopping_cart:
        #     self.shopping_cart[product_id] = {'username':''}
        # else:
        #     self.shopping_cart[product_id] = {'username':username_id}
        #     print(username_id)
        if product_id not in self.shopping_cart:
            self.shopping_cart[product_id] = {'quantity': 0,
                                            'price': str(product.price)}

        if update_quantity:
            self.shopping_cart[product_id]['quantity'] = quantity
        else:
            self.shopping_cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        保存购物车和购物车改动
        """
        self.session[settings.CART_SESSION_ID] = self.shopping_cart
        # 把购物车所有改动都保存到会话中,modified用来标记改动过的会话
        self.session.modified = True

    def remove(self,product):
        """
        从购物车中删除商品
        """
        product_id = str(product.id)
        if product_id in self.shopping_cart:
            del self.shopping_cart[product_id]
            self.save()



    def get_total_price(self):
        """
        计算购物车内商品的总价
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.shopping_cart.values())

    # def clear(self):
    #     """
    #     清空购物车会话 设为空的购物车
    #     """
    #     self.shopping_cart[settings.CART_SESSION_ID] = {}
    #     self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    # 使用property把coupon方法变成属性调用
    @property
    def coupon(self):
        if self.coupons_id:
            return Coupons.objects.get(id=self.coupons_id)
        return None

    # 返回被扣除折扣的总和
    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    # 返回减去折扣之后的总价
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()