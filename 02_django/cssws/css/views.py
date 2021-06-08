from django.shortcuts import render

from db.dao.userdb import UserDB
from db.frame.sqlitedao import SqliteDao
from db.vo.uservo import UserVO

sqlitedao = SqliteDao('shop')
sqlitedao.makeTable()
udb = UserDB('shop')

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
    try:
        dbuser = udb.select(id)
        print(dbuser)
        if pwd == dbuser.getPwd():
            request.session['sessionid'] = id
            context['section'] = 'loginok.html'
            context['loginuser'] = dbuser
        else:
            raise Exception
    except:
        context['section'] = 'loginfail.html'
        print("Error..")

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

    # 회원정보를 디비에 저장
    user = UserVO(id,pwd,name)
    udb.insert(user)

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


def userlist(request):
    users = udb.selectall()
    context = {
        'section': 'userlist.html',
        'users': users
    }
    return render(request, 'base.html', context)

def additem(request):


    return

def itemlist(request):
    return