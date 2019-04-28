from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect

from .models import Users,Histroys,Books

# Create your views here.

# 首页
def index(request):
    return render(request,'bookgli/index.html')

# 读者登录
def reader_login(request):
    return render(request, 'bookgli/reader_login.html')

# 注册
def register(request):
    return render(request, 'bookgli/register.html')


#注册的跳转
def zhuce(request):
        uname=request.POST['username']
        passwd=request.POST['password']
        passwd2=request.POST['password2']
        college = request.POST['college']  # 学院
        number = request.POST['number']  # 学号
        email = request.POST['email']  # 邮箱
        listu=Users.objects.all().filter(uname=uname)
        # print(listu,type(listu),len(listu))
        if len(listu)==0:
            if passwd==passwd2:
                a1=Users()
                a1.uname=uname
                a1.upwd=passwd
                a1.ucollege=college
                a1.unum=number
                a1.uemail=email
                a1.save()
                return HttpResponseRedirect('/bookgli/reader_login/')
            else:
                pwd='Password mismatch'
                return HttpResponseRedirect('/bookgli/register/',{'error':pwd})
        else:
            pwd = 'User already exists'
            return HttpResponseRedirect('/bookgli/register/', {'error': pwd})


# 登录
def reader(request):
    users=request.POST['username']
    pwd=request.POST['password']
    listu = Users.objects.all().filter(uname=users,upwd=pwd )
    print(listu,len(listu))
    if len(listu)==0:
        error='Wrong account or password'
        return HttpResponseRedirect('/bookgli/reader_login/',{'error':error})
    else:
        ida=listu[0].id
        user=Users.objects.get(pk=ida)
        return render(request,'bookgli/reader.html',{'g':user})