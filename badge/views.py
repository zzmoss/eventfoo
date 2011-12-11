# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
#from django.contrib.auth import authenticate,login
from forms import BadgeForm
# Create your views here.

def get_details(request):

    def errorHandle(error):
       form = BadgeForm()
       return render_to_response('badge/input.html', {'error':error, 'form':form,})

    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        fname = request.POST['fname']
        #if form.is_valid():
        return render_to_response('badge/success.html', {'fname':fname})
        #else:
        #   error = 'Form invalid'
        #   return errorHandle(error)
    else:
       form = BadgeForm()
       return render_to_response('badge/input.html', {'form':form,})

