from  django.conf.urls import url
from . import  views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$','django.contrib.auth.views.login',name='login'),
    # url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',name='logout1'),
    # url(r'^logout/$',views.logout,name='logout1'),
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),
]
