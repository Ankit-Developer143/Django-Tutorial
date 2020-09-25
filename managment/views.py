from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Order

# Create your views here.

def home(request):
    
  customer = Customer.objects.all()
  order =  Order.objects.all()
  
  pending = Order.objects.filter(status = 'Pending').count()
  delivered = Order.objects.filter(status = 'delivered').count()
  total = Order.objects.all().count()
  context = {
	  'customer':customer,'order':order,'pending':pending,'delivered':delivered,'total':total,
  }
  return render(request, 'managment/dashboard.html', context)


def product(request):
    product =  Product.objects.all()
    
    return render(request,'managment/product.html',{'product':product})


def customer(request,pk_test):
    
    customer = Customer.objects.get(id = pk_test)
    orders = customer.order_set.all()
    
    order = customer.order_set.all()
    order_count = order.count()
    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request,'managment/customer.html',context)