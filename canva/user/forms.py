from django import forms
from django.contrib.auth.models import User
import re


user_compiler=re.compile(r'^\w{5,}$')


class registerForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    password_again=forms.CharField()



    def save(self):
        first_name=self.cleaned_data.get('first_name')
        last_name=self.cleaned_data.get('last_name')
        username=self.cleaned_data.get('username')
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        password_again=self.cleaned_data('password_again')
        user=User.objects.create_user(
            username=username,
            first_name=first_name,
            email=email,
            last_name=last_name,
            password=password,
            password_again=password_again
        )
        return user
    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if not user_compiler.match(username):
            raise forms.ValidationError("Username dogru deyil")
        elif User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username movcuddur")
        return username
    
    def clean_email(self):
        email=self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email artiq movcuddur')
        return email
    

    def clean(self):
        super().clean()
        password=self.cleaned_data.get('password')
        password_again=self.cleaned_data.get('password_again')
        if password and password_again and password !=password_again:
            raise forms.ValidationError('sifreler eyni deyil')
        
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super().clean()