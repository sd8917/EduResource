from django.shortcuts import render,redirect

def cantAccessAfterLogin(get_response):

    def middleware(request,product_id=None):
        user = request.session.get('user')
        #print('user', user)
        if user:
            return redirect('home')
        else:
            return get_response(request)

    return middleware

