from django.forms import ModelForm 
from .models import Order,Customer

#import for login and registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        
        
        # fields = [customer] 
        fields = '__all__'
        
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        
        fields = '__all__'
        
        
        
#for login
