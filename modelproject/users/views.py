from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .filters import *

def home(request):
    use = User.objects.all()
    orders = Order.objects.all()
    context = {'use':use,'orders':orders}
    return render(request,'account/dashbord.html',context)
def product(request):

    products = Product.objects.all()
    myfilter = filterProduct(request.GET, queryset=products)
    products = myfilter.qs

    context = {'products':products, 'myfilter':myfilter}
    return render(request,'account/product.html',context)
def users(request):



    return render(request,'account/user.html')

def createOrder(request):


    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form }
    return render(request, 'account/order.html',context)

def updateOrder(request, pk):


    order =Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {'form':form}
    return render(request, 'account/update.html',context)

def deleteOrder(request, pk):
    item= Order.objects.get(id=pk)

    if request.method== 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'account/delete.html', context)







# Create your views here.
