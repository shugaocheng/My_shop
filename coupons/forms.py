from django import forms

class CouponsForm(forms.Form):
    code = forms.CharField(label='优惠券')