from django import forms

# 抵挡用户名少于两位，密码少于3位的
class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)