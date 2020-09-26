from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer,Order

#import order forms
from .forms import OrderForm,CustomerForm

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
  
def createOrder(request):
  #get the value from database
  form  = OrderForm()
  if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
      # save the form into database
      form.save()
      # redirect to main templates
      return redirect('/')
  context = {'form':form}
  return render(request,'managment/order_form.html',context)
 
def updateOrder(request,pk):
  order = Order.objects.get(id = pk)
  
  form  = OrderForm(instance = order)
  if request.method == 'POST':
    form = OrderForm(request.POST,instance =order)
    if form.is_valid():
      # save the form into database
      form.save()
      # redirect to main templates
      return redirect('/')
  context = {'form':form}
  return render(request,'managment/order_form.html',context)


def deleteOrder(request,pk):
  order = Order.objects.get(id = pk)
  if request.method == 'POST':
    order.delete()
    return redirect('/')
  context = {'item':order}
  return render(request, 'managment/delete.html', context)
  
  
def createCustomer(request):
  form  = CustomerForm()
  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
      # save the form into database
      form.save()
      # redirect to main templates
      return redirect('/')
  context = {'form':form}
  return render(request,'managment/customer_form.html',context)