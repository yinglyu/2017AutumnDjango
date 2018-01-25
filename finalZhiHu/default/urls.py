from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^logup/$', views.logup),#注册部分
    url(r'^logout/$', views.logoutView),#登出
    url(r'^login/$', views.loginView),#登录


    url(r'^focusquestion/$', views.focusquestion),  # 关注问题
    url(r'^myfocusedhome/$', views.myfocusedhome),  # 查看关注问题页面
    url(r'^focusedquestiondel/$', views.focusedquestiondel),  # 取消关注 ok


    url(r'^myquestion/$', views.myquestion),  # 编辑自己的问题，可以删除回答 OK
    url(r'^questiondel/$',views.questiondel),#删除自己的问题 ok
    url(r'^questionadminedit/$',views.questionadminedit),#编辑自己提问的问题 OK
    url(r'^answeradmindel/$', views.answeradmindel),  # 删除自己问题的回答 ok

    url(r'^myanswer/$', views.myanswer),  # 查看自己的回答ok，可以编辑，删除
    url(r'^answerdel/$', views.answerdel),  # 删除自己的某个回答 ok
    url(r'^answeredit/$',views.answeredit),# 编辑自己的某个回答 ok

    url(r'^myprofile/$', views.myprofile),  #查看自己的资料，可以编辑 ok
    url(r'^editpassword/$', views.editpassword),  #查看自己的资料，可以编辑 ok
    url(r'^editprofile/$', views.editprofile),  #查看自己的资料，可以编辑 ok
    #url(r'^profile/$', views.user),#滢 查看其他用户信息

    url(r'^myhome/$', views.myhome),  # 列出自己的问题列表 可以删除，查看（进入myquestion）ok
    url(r'^home/$',views.home),#茜
    url(r'^search/$',views.search),#茜
    url(r'^question/$',views.question),#茜
    url(r'^mynewanswer/$',views.mynewanswer),

    #url(r'^update/$', views.updatelist),#茜
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #url(r'^search/$', views.search),#茜
    #url(r'^del/$',views.dellist)#茜
    url(r'^$', views.home),#茜
]