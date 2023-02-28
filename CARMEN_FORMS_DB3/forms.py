from django import forms


class members_Reg(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
