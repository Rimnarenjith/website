from django.shortcuts import render,get_object_or_404
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

def get_monuments_from_slug(request,slug):
    try:
        monument = get_object_or_404(Monuments, slug=slug)
    except:
        return HttpResponse(slug+" Model does not exist")
    context = {'monument': monument}
    return render(request, 'web\index.html', context)
