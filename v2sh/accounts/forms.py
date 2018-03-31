from django import forms

from .models import user
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = user
        fields = ('name','email','password','confirm_password')

    # Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = user
        fields = ('email','password')
