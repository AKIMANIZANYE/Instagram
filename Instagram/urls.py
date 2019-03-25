from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^Instagram/image$', views.new_image, name='new-image'),
    
]