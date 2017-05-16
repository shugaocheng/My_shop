from django import forms
from django.contrib.auth.models import User

# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput)


# 注册表单
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次输入密码',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password(self):
        cd = self.cleand_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次密码输入不一致")
        return cd['password2']
