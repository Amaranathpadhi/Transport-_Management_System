from django import forms
from .models import Userprofileinfo,Employee,Driver,Addbooking
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model= User
        fields =('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Userprofileinfo
        fields = ('portfolio_site','profile_pic')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields ="__all__"

class DriverForm(forms.ModelForm):
    class Meta:
        model= Driver
        fields ="__all__"
class AddbookForm(forms.ModelForm):
    class Meta:
        model= Addbooking
        exclude = ['emp_name']