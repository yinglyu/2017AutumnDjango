from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)  # 姓名
    tel = models.CharField(max_length=100)  # 电话
    email = models.CharField(max_length=100)  # 邮箱
    addr = models.CharField(max_length=100)  # 地址
    QQnum = models.CharField(max_length=100)  # 地址
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #CASCADE:默认值，model对象会和ForeignKey接洽关系对象一路被删除