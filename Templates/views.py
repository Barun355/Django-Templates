from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')

def removepunc(request):
    return HttpResponse('removepunc')

def capitalizefirst(request):
    return HttpResponse('capfirst')

def newlineremove(request):
    return HttpResponse('newlineremove')

def spaceremove(request):
    return HttpResponse('spaceremove')

def charcount(request):
    return HttpResponse('charcount')

