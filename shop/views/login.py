from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from shop.models import Product,ProductImages,User
from django.shortcuts import render,redirect
from django.http import HttpResponse


class LoginView(View):
    return_url = None
    def get(self,request):
        print("class based views")
        LoginView.return_url = request.GET.get('return_url')
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
                temp = {}
                temp['email'] = user.email
                temp['id'] = user.id
                request.session['user']  = temp
                #print(user.__dict__)
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                    
                return redirect('home')
            else:
                return render(request, 'login.html',{'error': 'Email or password is not valid '} )
        except:
            return render(request, 'login.html' ,{'error': 'Email or password is not valid '})
        