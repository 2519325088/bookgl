from django.conf.urls import url

from . import views

app_name='bookgli'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^reader_login/$',views.reader_login,name='reader_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^zhuce/$',views.zhuce,name='zhuce'),
    url(r'^reader/$',views.reader,name='reader'),
]