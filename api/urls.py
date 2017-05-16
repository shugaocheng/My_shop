from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'product/$',views.ProductListView.as_view(),name='product_list'),
    url(r'product/(?P<pk>\d+)/$',views.ProductDetailView.as_view(),name='detail'),
]