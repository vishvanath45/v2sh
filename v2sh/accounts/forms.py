from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('full_name','email','password1','password2')

    def cleanpassword2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print(password1 , password2)
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords dont match")

        return password1

    def save(self, commit=True):

        user = super(RegisterForm , self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()

        return user

    # Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    #
# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = user
#         fields = ('email','password')
