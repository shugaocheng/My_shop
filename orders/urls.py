from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$',views.order_create,name='order_create'),
    url(r'^order_detail/$',views.order_detail,name='order_detail'),
    url(r'^remove/(?P<order_id>\d+)/$',views.order_delete,name='order_delete'),
]
