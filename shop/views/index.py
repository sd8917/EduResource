from shop.models import Product,ProductImages,User
from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    #sendEmail(name="Sujeet",email='sudhanshuraj8917@gmail.com', subject="test",htmlContent="<h1>hey !! Email from Test mail check up</h1>")
    products = Product.objects.filter(active=True)
    context = {
        'products' :products
    }
    return render(request, 'index.html',context)

def logout(request):
    request.session.clear()
    return redirect('home')