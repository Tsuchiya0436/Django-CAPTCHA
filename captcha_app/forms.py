from django import forms
from captcha.fields import CaptchaField

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    captcha = CaptchaField()