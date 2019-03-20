from django import forms

class Signup(forms.Form):
	fullname = forms.CharField(label='Fullname',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Fullname','style':'width:50%;'}))
	username = forms.CharField(label='Username',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','style':'width:50%;'}))
	email = forms.EmailField(label='Email-ID',max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email-ID','style':'width:50%;'}))
	password = forms.CharField(label='Password',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','style':'width:50%;'}))
	