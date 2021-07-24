from shop.models import Product,ProductImages,User,Payment
from django.shortcuts import render,redirect
from django.http import HttpResponse
from instamojo_wrapper import Instamojo
from digitatShop.settings import PAYMENT_API_KEY,PAYMENT_API_AUTH_TOKEN
    
import math
API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

def createPayment(request, product_id):

    user = request.session.get('user')
    product = Product.objects.get(id=product_id)
    userObject = User.objects.get(id=user.get('id'))
    amount = (product.price - (product.price*(product.discount/100)) )

    # Create a new Payment Requestexite
    response = API.payment_request_create(
        amount=math.floor(amount),
        purpose=f'Payment for { product.name }',
        send_email=True,
        email= user.get('email'),
        buyer_name = userObject.name,
        redirect_url="http://localhost:8000/complete-payment"

    )
    print(response)
    # print the long URL of the payment request.
    payment_request_id = response['payment_request']['id']
    
    payment  = Payment(user=User(id = user.get('id')) ,
                            product=product,
                                payment_request_id=payment_request_id)

    payment.save()

    url =  response['payment_request']['longurl']
    print(response)
    return redirect(url)

def verifyPayment(request):

    payment_id = request.GET.get('payment_id')
    payment_request_id = request.GET.get('payment_request_id')
    # Create a new Payment Request
    response = API.payment_request_payment_status(payment_request_id, payment_id)

    status = response['payment_request']['payment']['status']
    if status != "failed":
        payment = Payment.objects.get(payment_request_id = payment_request_id)
        payment.payment_id = response['payment_request']['payment']['payment_id']
        payment.status = status  
        payment.save() 

        return render(request, "download_product_after_payment.html",{'payment': payment})
    else:
        return render(request, 'payment_fail.html')
 