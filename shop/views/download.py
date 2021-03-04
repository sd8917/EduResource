from shop.models import Product,ProductImages,User,Payment
from django.shortcuts import render,redirect
from django.http import HttpResponse

def downloadFree(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.discount == 100:
            #download product
           return redirect(product.file.url)
        else:
            return redirect('home')

    except:
        return redirect('home')

def downloadPaidProduct(request, product_id):
    try:
        product =  Product.objects.get(id=product_id)
        sesssion_user = request.session.get('user')
        user = User(id = sesssion_user.get('id'))
        payment = Payment.objects.filter(user=user,product=product)

        if(len(payment)>0):
            print(len(payment))
            file = product.file
            if file:
                return redirect(product.file.url)
            else:
                return redirect(product.link)
        else:
            return redirect('home')

    except:
        return redirect('home')

    

    