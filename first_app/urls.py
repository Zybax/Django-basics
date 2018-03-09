from django.conf.urls import url
from first_app import views

urlpatterns= [
    url(r'^$',views.index,name = 'index'),
    url(r'^$',views.template2,name = 'template2'),
    url(r'^$',views.userview, name='userview'),
]