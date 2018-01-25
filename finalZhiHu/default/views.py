
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from default.models import UserProfile,Question,Answer # 0109,Img
from .import urls
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.files.base import ContentFile # 0109
import os
# Create your views here.


def logup(request):#

    if request.method == 'GET':

        mode = request.GET['mode']
        return render(request, "logup.html",{'mode':mode})
    elif request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pswd']

        num_results = User.objects.filter(username=username).count()
        if num_results != 0:

            return render(request, "logup.html",{'mode':num_results,'existname':username})

        else:

            User.objects.create_user(username=username,email=None,password=password)
            user= User.objects.get(username=username)
            profile = UserProfile()  # e*************************
            profile.user_id = user.id
            profile.save()
            return render(request, "login.html")

def loginView(request):#

    if request.method == 'GET':

        return render(request, "login.html",{'mode':0})#首次登录
    elif request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pswd']
        user = authenticate(username = username, password = password)

        if user is not None:#已经有这个用户了
            login(request,user)
            return HttpResponseRedirect("/home/")
        else:
            return render(request, "login.html",{'mode':1})#登录失败


@login_required
def home(request):#
    if request.method == 'GET':
        userprofile = UserProfile.objects.get(user=request.user)
        for question in Question.objects.all():
            if userprofile.focusedquestion.filter(id=question.id).count() == 0:
                question.focus = 0
                question.save()
            else:
                question.focus = 1
                question.save()
        hotquestionlist = Question.objects.order_by('-answerNum')[:10]#0108ying
        questionlist = Question.objects.order_by('-answerNum')[11:]#0108ying
        #需要替换成真正首页
        return render(request, "home.html", {"hotquestionlist": hotquestionlist,"questionlist": questionlist})#0108ying
    elif request.method == 'POST':
        title=request.POST['question_to_add']
        Question.objects.create(title=title,user=request.user)
        return HttpResponseRedirect("/home/")


@login_required()
def search(request):#
    if request.method == 'POST':
        content=request.POST["question_to_search"]

        questionlist=Question.objects.filter(title__contains=content)
        return render(request,"home.html",{"questionlist":questionlist})

@login_required
def question(request):
    if request.method == "GET":
        questionid=request.GET["questionid"]
        question=Question.objects.get(id=questionid)
        answerlist=Answer.objects.filter(question=question)

        if question.user == request.user:#查看自己的问题 回到自己的页面
            question.mode = False
            question.save()
            return render(request, "myquestion.html", {"question": question, "answerlist": answerlist})

        return render(request,"question.html",{"question":question,"answerlist":answerlist})

    elif request.method == "POST":
        content=request.POST['content']
        questionid=request.POST['questionid']

        question = Question.objects.get(id=questionid)
        if question.user != request.user: #自己回答自己的问题不用提醒
            question.mode = True

        newanswer = Answer.objects.create(user=request.user,question=question,content=content)

        pic = request.FILES.get("pic")
        if not not pic:
            newanswer.imgname = request.FILES['pic'].name
            newanswer.img =request.FILES['pic']
            newanswer.save()

        answerlist = Answer.objects.filter(question=question)
        question.answerNum = answerlist.count() # 0108ying
        question.save() # 0108ying
        return render(request,'question.html',{"question":question,"answerlist":answerlist})

@login_required#
def logoutView(request):
    logout(request)
    return HttpResponseRedirect("/login/")


@login_required#
def myhome(request):
    if request.method == 'GET':
        questionlist = Question.objects.filter(user=request.user).order_by('-id')
        return render(request, "myhome.html", {"questionlist": questionlist})
    elif request.method == 'POST':
        title=request.POST['question_to_add']
        Question.objects.create(title=title,user=request.user)
        return HttpResponseRedirect("/myhome/")

@login_required#
def questiondel(request):
    questionid = request.GET['questionid']#获取删除条目的编号
    if Question.objects.filter(id = questionid).count() == 0:#防止多次请求
        return HttpResponseRedirect("/myhome/")

    Question.objects.get(id=questionid).delete()

    return HttpResponseRedirect("/myhome/")
@login_required
def myquestion(request):
    if request.method == "GET":
        questionid=request.GET["questionid"]
        question=Question.objects.get(id=questionid)
        question.mode = False
        question.save()
        answerlist=Answer.objects.filter(question=question)
        return render(request,"myquestion.html",{"question":question,"answerlist":answerlist})
    elif request.method == "POST":#
        content=request.POST['content']
        questionid=request.POST['questionid']
        question=Question.objects.get(id=questionid)
        #question.mode = True myquestion 不用 新信息
        newanswer=Answer.objects.create(user=request.user,question=question,content=content)
        pic = request.FILES.get("pic")
        if not not pic:
            newanswer.imgname = request.FILES['pic'].name
            newanswer.img =request.FILES['pic']
            newanswer.save()
        answerlist=Answer.objects.filter(question=question)
        question.answerNum = answerlist.count() # 0108ying
        question.save()# 0108ying
        return render(request,'myquestion.html',{"question":question,"answerlist":answerlist})


@login_required#
def answeradmindel(request):
    answerid = request.GET['answerid']#获取删除条目的编号
    question=Answer.objects.get(id=answerid).question
    if Answer.objects.filter(id = answerid).count() == 0:#防止多次请求
        answerlist = Answer.objects.filter(question=question)
        return render(request, 'myquestion.html', {"question": question, "answerlist": answerlist})
    Answer.objects.get(id=answerid).delete()
    answerlist = Answer.objects.filter(question=question)
    question.answerNum = answerlist.count()  # 0108ying
    question.save()  # 0108ying
    thisquestionid= question.id
    return render(request, 'myquestion.html', {"question": question, "answerlist": answerlist})


@login_required#
def questionadminedit(request):
    if request.method == 'GET':
        questionid = request.GET['questionid']
        question = Question.objects.get(id = questionid)
        answerlist = Answer.objects.filter(question = question )
        return render(request,"editquestion.html",{"question":question,"answerlist":answerlist})
    elif request.method == 'POST':
        newtitle = request.POST['new_title']
        questionid = request.POST['questionid']
        question = Question.objects.get(id = questionid)

        question.title  = newtitle
        question.save()
        answerlist = Answer.objects.filter(question=question)
        return render(request, 'myquestion.html', {"question": question, "answerlist": answerlist})

@login_required#
def myanswer(request):
    if request.method == 'GET':
        answerlist = Answer.objects.filter(user=request.user).order_by('-id')
        return render(request,"myanswer.html",{"answerlist":answerlist})

@login_required
def answerdel(request):#
    answerid = request.GET['answerid']
    if Answer.objects.filter(id = answerid).count() == 0:#防止多次请求
        return HttpResponseRedirect("/myanswer/")
    answer = Answer.objects.get(id = answerid)
    question = answer.question
    answer.delete()
    answerToThis = Answer.objects.filter(question=question)
    question.answerNum = answerToThis.count()  # 0108ying
    question.save()  # 0108ying
    return HttpResponseRedirect("/myanswer/")

@login_required
def answeredit(request):#
    if request.method == 'GET':
        answerid = request.GET['answerid']
        answer = Answer.objects.get(id = answerid)
        question = answer.question
        return render(request,"editanswer.html",{"question":question,"answer":answer})
    elif request.method == 'POST':
        content = request.POST['content']
        answerid = request.POST['answerid']
        answer = Answer.objects.get(id = answerid)
        answer.content = content
        pic = request.FILES.get("pic")
        if not not pic:
            answer.imgname = request.FILES['pic'].name
            answer.img =request.FILES['pic']
        answer.save()
        question = answer.question
        if question.user != request.user: #自己回答自己的问题不用提醒
            question.mode = True
        question.save()
        return HttpResponseRedirect("/myanswer/")

@login_required
def focusquestion(request):
        if request.method == 'GET':
            questionid = request.GET['questionid']
            question = Question.objects.get(id = questionid)
            userprofile = UserProfile.objects.get(user= request.user)
            userprofile.focusedquestion.add(question)

            return HttpResponseRedirect('/myfocusedhome/')

@login_required
def myfocusedhome(request):
    if request.method == 'GET':
        userprofile = UserProfile.objects.get(user=request.user)

        questionlist = userprofile.focusedquestion.all().order_by('-id')
        return render(request, "myfocusedhome.html", {"questionlist": questionlist})

@login_required
def focusedquestiondel(request):#改函数名0112
    questionid = request.GET['questionid']  # 获取删除条目的编号
    userprofile = UserProfile.objects.get(user=request.user)
    if userprofile.focusedquestion.filter(id = questionid).count() == 0:#防止多次请求
        return HttpResponseRedirect("/myfocusedhome/")

    userprofile.focusedquestion.get(id=questionid).delete()

    return HttpResponseRedirect("/myfocusedhome/")

@login_required
def myprofile(request):#
    if request.method == 'GET':
        userprofile = UserProfile.objects.get(user=request.user)

        return render(request, "myprofile.html", {"userprofile": userprofile})

@login_required
def editpassword(request):#
    if request.method == 'POST':
        userprofile = UserProfile.objects.get(user=request.user)
        password = request.POST['pswd']
        user=request.user
        user.set_password(password)
        user.save()
        return HttpResponseRedirect("/myprofile/")

@login_required
def editprofile(request):#
    if request.method == 'POST':
        newintroduction = request.POST['introduction']
        userprofile = UserProfile.objects.get(user=request.user)

        userprofile.introduction=newintroduction
        userprofile.save()

        return HttpResponseRedirect("/myprofile/")

@login_required()
def mynewanswer(request):
    if request.method == "GET":
        questionlist = Question.objects.filter(user = request.user, mode = True).order_by('-id')
        return render(request,"myhome.html",{"questionlist":questionlist})
