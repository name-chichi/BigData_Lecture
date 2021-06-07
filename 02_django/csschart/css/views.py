from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def html5(request):
    context = {
        'section':'html5.html'
    };
    return render(request, 'base.html',context);
def css3(request):
    context = {
        'section': 'css3.html'
    };
    return render(request, 'base.html',context);
def javascript(request):
    context = {
        'section': 'javascript.html'
    };
    return render(request, 'base.html',context);
def jquery(request):
    context = {
        'section': 'jquery.html'
    };
    return render(request, 'base.html',context);
def ajax(request):
    context = {
        'section': 'ajax.html'
    };
    return render(request, 'base.html',context);