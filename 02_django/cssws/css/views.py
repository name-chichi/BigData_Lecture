from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def login(request):
    context = {
        'section': 'login.html'
    }
    return render(request, 'base.html', context)

def loginimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    print('id : ', id, 'pwd : ', pwd)

    context = {}
    if id == 'qq' and pwd == '11':
        request.session['sessionid'] = id
        context['section'] = 'loginok.html'
        context['loginid'] = id
    else:
        context['section'] = 'loginfail.html'

    print('세션ID : ', request.session['sessionid'])
    return render(request, 'base.html', context)

def logout(request):
    if request.session['sessionid'] != None:
        del request.session['sessionid']
    return render(request, 'base.html')

def registerimpl(request):
    id = request.GET['id']
    pwd = request.GET['pwd']
    name = request.GET['name']
    print('id : ', id, 'pwd : ', pwd, 'name : ', name)

    context = {
        'section': 'registerok.html',
        'rname': name
    }
    return render(request, 'base.html', context)

def register(request):
    context = {
        'section': 'register.html'
    }
    return render(request, 'base.html', context)

def html5(request):
    context = {
        'section':'html5.html'
    }
    return render(request, 'base.html', context)

def css3(request):
    context = {
        'section': 'css3.html'
    }
    return render(request, 'base.html', context)

def javascript(request):
    context = {
        'section': 'javascript.html'
    }
    return render(request, 'base.html', context)

def jquery(request):
    context = {
        'section': 'jquery.html'
    }
    return render(request, 'base.html', context)

def ajax(request):
    context = {
        'section': 'ajax.html'
    }
    return render(request, 'base.html', context)