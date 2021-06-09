from django.shortcuts import render

# Create your views here.
def loginimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    print(id, pwd)
    return render(request, 'jq04.html')


def registerimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    age = request.POST['age']
    print(id, pwd, name, age)
    return render(request, 'jq05.html')