from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.shopping_cart_detail,
        name='shopping_cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$',
        views.shopping_cart_add,
        name='shopping_cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$',
        views.shopping_cart_remove,
        name='shopping_cart_remove'),
]