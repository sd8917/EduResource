from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from shop.models import Product,ProductImages,User
from django.shortcuts import render,redirect
from django.http import HttpResponse


class LoginView(View):

    def get(self,request):
        print("class based views")
        return render(request, 'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password  = request.POST.get('password')
        print(email,password)
        try:
            user = User.objects.get(email=email)
            flag = check_password(password=password, encoded=user.password)
            
            if flag:
                #collect products;
                return redirect('home')
            else:
                return render(request, 'login.html',{'error': 'Email or password is not valid '} )
        except:
            return render(request, 'login.html' ,{'error': 'Email or password is not valid '})

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html') 

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            hashedPassword = make_password(password=password)
            user = User(name=name,email=email,password=hashedPassword,phone=phone)

            result = user.save()
            return render(request, 'login.html')
        except:
            return render(request, 'signup.html',{'error': 'User already registered .'})   