from django.contrib.auth.models import User,Group
from shop.models import Product
# from rest_framework import viewsets
from rest_framework import generics
from .serializers import ProductSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
class ProductListView(generics.ListAPIView):
    # 取回对象
    queryset = Product.objects.all().order_by('id')
    # 序列化对象
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer