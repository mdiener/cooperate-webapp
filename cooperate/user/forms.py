from django import forms


class SignupForm(forms.Form):
  first_name = forms.CharField(label="First Name", max_length=200)
  last_name = forms.CharField(label="Last Name", max_length=200)
  email = forms.EmailField(label="Email", max_length=200)
  password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput)


class LoginForm(forms.Form):
  email = forms.EmailField(label="Email", max_length=200)
  password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput)
