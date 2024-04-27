from django import forms
from .models import Customer, Product, Category
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignInForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))

class CustomUserCreationForm(UserCreationForm):
    phone_number=forms.CharField(max_length=30)

class Meta(UserCreationForm.Meta):
    model=User
    fields=('username','email','password1','password2','firstname')
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'unit', 'image', 'category']
        widgets = {
            'unit': forms.Select(choices=Product.unit_choices),
            'category': forms.Select(), 
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

