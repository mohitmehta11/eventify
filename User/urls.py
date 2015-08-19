from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^auth-token/$',views.ObtainAuthToken.as_view()),
    url(r'^(?P<pk>[0-9a-zA-Z]+)/$', views.UserDetail.as_view()),
    url(r'^$', views.UserList.as_view()),
    url(r'^(?P<user>[0-9a-zA-Z]+)/favourite/(?P<id>[0-9a-zA-Z]+)$', views.FavouriteDetail.as_view()),
    url(r'^(?P<user>[0-9a-zA-Z]+)/favourite/$', views.FavouriteList.as_view()),
]