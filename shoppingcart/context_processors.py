from .shoppingcart import ShoppingCart

# 上下文处理器,添加到配置的TEMPLATE
def shopping_cart(request):
    return {'shopping_cart':ShoppingCart(request)}