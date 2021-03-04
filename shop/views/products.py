from shop.models import Product,ProductImages,User,Payment
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q 

def productDetails(request , product_id):
    product = Product.objects.get(id = product_id)
    images = ProductImages.objects.filter(product = product_id)
    can_download = False
    try:
        session_user = request.session.get('user')
        if session_user:
            user_id = session_user.get('id')
            user = User(id = user_id)
            payment = Payment.objects.filter(~Q(status = "failed"), product = product,user = user)

            if len(payment) != 0:
                can_download= True
    except:
        pass

    context = {
        'product': product,
        'images' : images,
        'can_download': can_download 
    }
    return render(request, 'product_details.html', context)
    