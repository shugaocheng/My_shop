from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.


# def logout(request):
#     auth.logout(request)
#     return redirect('account:logout')
# 登录认证视图
# @login_required
def user_login(request):
    user = request.user
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            username = cd['username']
            if user is not None:
                if user.is_active:
                    login(request,user)
                    request.session['username'] = username
                    return redirect('shop:product_list')
                else:
                    return HttpResponse('账户未启用')
            else:
                return HttpResponse('Invalid login')
    else:
        login_form = LoginForm()
    return render(request,'account/login.html',{'login_form':login_form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect("account:login")