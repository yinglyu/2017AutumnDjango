from django.db import models
from django.contrib.auth.models import User

import os
# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)#问题标题最长10个字符
    mode =  models.BooleanField(default=False) #表示该问题是否有更新 True还没被查看过 False已经查看过了 增加回答时置为 True，点开问题时（question，myquestion）置为 False
    #content = models.CharField(max_length=200)#问题描述可以长一点
    answerNum = models.IntegerField(default=0) #用于首页显示热度，排序 增加（question，myquestion）删除回答（myquestion，myanswer）时利用当前问题的回答数赋值# 0108ying
    focus = models.IntegerField(default=0) #主页中显示是否关注

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    img = models.ImageField(upload_to='upload', null=False, blank=True, default = os.path.join ( '/','upload','empty.png'),)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    focusedquestion = models.ManyToManyField(Question)
    introduction = models.CharField(max_length=150)



            #def save(self, *args ,*kwargs):
    #   super(UserProfile,self).save()
    #    for i in self.foquestionlist:
    #        p,created = Question.objects.get_or_create(name = i)
    #        self.focusedquestion.add(p)
    #    self.foquestionlist[]
