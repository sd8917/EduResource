from shop.models import Product,ProductImages,User,Payment
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def my_orders(request):
    user_id = request.session.get('user').get('id')
    user  = User(id=user_id)
    payments = Payment.objects.filter(~Q(status ="failed") ,user = user)
    return render(request, 'orders.html',{'orders':payments})

