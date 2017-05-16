from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class ShoppingCartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int) # 转换成int
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)