from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apply/$',views.coupons_apply,name='apply'),
]