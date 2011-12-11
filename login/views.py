from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login
from forms import LoginForm
# Create your views here.

def index(request):
    
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('login/index.html', {'error':error, 'form':form,})
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render_to_response('login/success.html', {'username': username,})
                else:
                    error = 'Account disabled'
                    return errorHandle(error)
            else:
                error = 'invalid login'
                return errorHandle(error)
        else:
            error = 'Form invalid'
            return errorHandle(error)
    else:
        form = LoginForm()
        return render_to_response('login/index.html', {'form':form,})

