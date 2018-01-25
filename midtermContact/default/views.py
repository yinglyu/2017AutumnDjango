from django.shortcuts import render
from default.models import Contact
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def getlist(request):


    if request.method == 'GET':
        #print(request.session.keys())
        request.session['color'] ="red"
        #print(request.session['_auth_user_id'])
        contact = Contact.objects.filter(user = request.user)
        return render(request, 'ContactsList.html', {'contact':contact})#templates 需要放在app里面 setting 里面把  demo 加入到installed app
    elif request.method == 'POST':
        searchName = request.POST['name']

        contact = Contact.objects.filter(name__contains=searchName,user = request.user)
        # con = Contact(name=newname)  # new
        # con.save()#new
        # todolist = Todolist.objects.all()#new
        return render(request, 'Outcome.html', {'contact': contact})

@login_required
def addlist(request):
    if request.method == 'GET':#处理用户加载添加页面的请求

        return render(request, 'NewContactJs.html')
    elif request.method == 'POST':
        newname = request.POST['name']
        newtel = request.POST['tel']
        newemail = request.POST['email']
        newaddr = request.POST['addr']
        newQQnum = request.POST['QQnum']

        con = Contact.objects.create(name=newname, tel=newtel,email=newemail,addr=newaddr,QQnum=newQQnum,user = request.user)#new
        con.user = request.user
        return HttpResponseRedirect("/") #重定向


#@login_required
#def search(request):






@login_required
def updatelist(request):
    if request.method == 'GET':#处理用户加载编辑页面的请求
        conid = request.GET['conid']  # 获取删除条目的编号
        '''todo = todolist[int(todoid)-1]'''
        con = Contact.objects.get(id=conid)
        return render(request,'Update.html',{'con':con})
    elif request.method == 'POST':#处理用户提交编辑日程的表单
        conid = request.POST['id']#获取更新条目的编号及内容
        #content = request.POST['content']
        #todolist[int(todoid) - 1]['content']=content
        newname = request.POST['name']
        newtel = request.POST['tel']
        newemail = request.POST['email']
        newaddr = request.POST['addr']
        newQQnum = request.POST['QQnum']
        con = Contact.objects.get(id=conid)#5.3 P31
        con.name =  newname#5.3 P31
        con.tel = newtel
        con.addr = newaddr
        con.email = newemail
        con.QQnum = newQQnum
        con.save()#5.3 P31
        #todolist = Todolist.objects.all()#5.3 P31
        #return render(request, 'getlist.html', {'todolist': todolist})
        return HttpResponseRedirect("/")



def login_view(request):
    if request.method == 'GET':
        return render(request,"Login.html")
    elif request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pswd']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "Login.html")

@login_required
def dellist(request):
    conid = request.GET['conid']#获取删除条目的编号
    #out of date todolist.pop(int(todoid) - 1)#删除
    #out of date for i in range(len(todolist)):
     #out of date    todolist[i]['id'] = i + 1#重新编号

    #out of date return render(request, 'getlist.html', {'todolist': todolist})
    Contact.objects.get(id=conid).delete()
    #for i in range(len(Todolist)):
    #    Todolist(i).id = i +1

    #todolist = Todolist.objects.all()
    #return render(request, 'getlist.html', {'todolist': todolist})
    return HttpResponseRedirect("/")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")




#def new(request):

 #   return render(request, 'default/NewContactJs.html', locals())#templates 需要放在app里面 setting 里面把  demo 加入到installed app
