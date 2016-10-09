from django.conf.urls import url
from acount import  views

urlpatterns=[
    url(r'^$',views.register,name='register'),
    url(r'^register/$',views.register,name='register'),

]