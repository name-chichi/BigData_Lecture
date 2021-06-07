from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'css08.html')
def html5(request):
    centext = {
        'section':'html5.html',
    };
    return render(request, 'css08.html',centext);

