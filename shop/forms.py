from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='搜索',max_length=50)