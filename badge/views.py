# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from BadgeGen import createBadges
#from django.contrib.auth import authenticate,login
from forms import BadgeForm
# Create your views here.

def get_details(request):

    def errorHandle(error):
       form = BadgeForm()
       return render_to_response('badge/input.html', {'error':error, 'form':form,})

    def handle_uploaded_file(f):
        #destination = open('./BadgeGen/sample.csv', 'wb+')
        #for chunk in f.chunks():
        #    destination.write(chunk)
        #destination.close()
        ob = createBadges.BadgeMaker(f,template = "badge/BadgeGen/badge_template_white.png",namecol = "black", fontname = "badge/BadgeGen/Trebucbd.ttf" )

        ob.generateBadges()


    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        fname = request.POST['fname']
        handle_uploaded_file(request.FILES['csvfile'])
       
        if form.is_valid():
            return render_to_response('badge/success.html', {'fname':fname})
        else:
           error = 'Form invalid'
           return errorHandle(error)
    else:
       form = BadgeForm()
       return render_to_response('badge/input.html', {'form':form,})

