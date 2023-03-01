from django.shortcuts import render
from django.http import HttpResponse
from web.models import Monuments

# Create your views here.
def get_monument(request,id):
    template = "web\index.html"
    try:
        monument = Monuments.objects.get(id=id)
    except:
        return HttpResponse("Model does not exist")
    context = {
        'monument':monument
    }
    return render(request,template_name=template,context=context)
