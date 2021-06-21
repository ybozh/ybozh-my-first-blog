# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'^$', views.post_list, name='post_list'),
# ]


from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path(r'^post/new/$', views.post_new, name='post_new'),
    path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]