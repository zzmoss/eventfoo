from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('login/index.html', {'error':error, 'form':form,}, context_instance=RequestContext(request) )
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render_to_response('login/success.html', {'username': username, 'login':user.is_active}, context_instance=RequestContext(request))
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
        return render_to_response('login/index.html', {'form':form,}, context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        if form.is_valid():
            new_user = form.save()
            return render_to_response("login/success.html",{'username':username,}, context_instance=RequestContext(request))

    else:
        form = UserCreationForm()
        return render_to_response("login/register.html", {'form':form,}, context_instance=RequestContext(request))	

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")
