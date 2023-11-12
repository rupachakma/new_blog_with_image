from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

from app.models import Post


class SignupForm(UserCreationForm):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
  
    class Meta:
        model = User
        fields =['username','email']
        labels ={'email':'Email'}
        widgets={
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))

class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','image','file']
        labels = {'title':'Title','description':'Description','image':'Image','file':'File'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }
