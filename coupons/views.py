from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupons
from .forms import CouponsForm
# Create your views here.

# 验证优惠券 将符合的优惠券保存在session中
@require_POST
def coupons_apply(request):
    now = timezone.now()
    form = CouponsForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupons = Coupons.objects.get(code__iexact=code,
                                          valid_form__lte=now,
                                          valid_to__gte=now,
                                          active=True)
            request.session['coupons_id'] = coupons.id
        except Coupons.DoesNotExist:
            request.session['coupons_id'] = None
    return redirect('shopping_cart:shopping_cart_detail')