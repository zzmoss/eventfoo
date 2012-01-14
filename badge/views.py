# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from BadgeGen import createBadges
import random, os, glob, zipfile
from PIL import Image
from django.contrib.auth import authenticate,login
from forms import BadgeForm
# Create your views here.

@login_required(login_url="/login")
def get_details(request):

    def errorHandle(error):
        form = BadgeForm()
        return render_to_response('badge/input.html', {'error':error, 'form':form, 'login':'true'}, context_instance=RequestContext(request))

    def handle_uploaded_file(cfh, ifh, dirname, rand, nfcol, cfcol):

        ob = createBadges.BadgeMaker(cfh, ifh, namecol = nfcol, compcol = cfcol, fontname = "badge/BadgeGen/nevis.ttf", dirname = dirname+"/"+rand )
        ob.generateBadges()
        
        filewriter = zipfile.ZipFile("media/"+dirname+rand+".zip", "w")
        for name in glob.glob("outputPNGs/"+dirname+"/"+rand+"/*"):
            filewriter.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
        filewriter.close()


    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        
        dirname = request.POST['csrfmiddlewaretoken']
        rand = random.randint(1000,9999)
        namefontcol = '#'+str(request.POST['namefontcol'])
        compfontcol = '#'+str(request.POST['compfontcol'])

        if form.is_valid():      
            uploadedImage = form.cleaned_data['templatefile']
            imageData = Image.open(uploadedImage)
            handle_uploaded_file(request.FILES['csvfile'], imageData, dirname, str(rand), namefontcol, compfontcol)
            zipfilename = dirname+str(rand)+".zip"
            filezip = open("media/"+zipfilename)
          #  response = HttpResponse(filezip, mimetype = "application/x-zip-compressed")
          #  value = 'attachment; filename=badges_'+str(rand)+'.zip'
          #  response['Content-Disposition'] = value
            return render_to_response('badge/input.html',{'login':'true','zipfile':zipfilename}, context_instance=RequestContext(request))
        else:
            error = 'Form invalid'
            return errorHandle(error)
   
    else:
       form = BadgeForm()
       return render_to_response('badge/input.html', {'form':form, 'login':'true'}, context_instance=RequestContext(request))
