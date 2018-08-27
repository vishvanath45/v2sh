from django import forms
from v2sh.environment import db, experience, superuser, credentials
from django.contrib import messages 
'''
class RegisterForm(forms.Form):
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

'''
class RegisterForm(forms.Form):
    name = forms.CharField(label = 'Full Name' , widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'Email' , widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = 'Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
        
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email = cleaned_data.get('email')
        password2 = cleaned_data.get('password2')
        password1 = cleaned_data.get('password1')
        if password1 != password2:
            self.add_error('password1', 'Password and Confirm Password does not match.')
        
        split_email = email.split('@')[1]
        if split_email != 'btech.nitdgp.ac.in':
            self.add_error('email', 'Please enter the college email id')
        
        if credentials.find_one({'Email' : email}) != None:
            self.add_error('email', 'This email id already exists')
            
class LoginForm(forms.Form):
    email = forms.EmailField(label = 'Email' , widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = 'Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = credentials.find_one({'Email' : email})
        
        if user == None:
            self.add_error('email', 'This email id does not exist')
    
        elif user['Password']!=password:
            self.add_error('password', 'Invalid Credentials')
            
        