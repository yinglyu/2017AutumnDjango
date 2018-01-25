from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.getlist), #获取todolist列表，在views里面会写这个怎么搞
    #    url(r'login/$',views.login),http://127.0.0.1:8000/login/ js css 放入templates没有格式

    url(r'^contact/$', views.getlist),
    url(r'^add/$', views.addlist),
    url(r'^update/$', views.updatelist),
    #url(r'^search/$', views.search),
    url(r'^del/$',views.dellist),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view)
]