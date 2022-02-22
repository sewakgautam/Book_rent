from django import forms

class login_form(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-styling'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-styling'}))

    
    