from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'^minisclad/scltov_new/$', views.scladtov_new, name='scladtov_new'),
    url(r'^minisclad/(?P<pk>\d+)/scledit/$', views.scladtov_edit, name='scladtov_edit'),
    url(r'^minisclad/(?P<pk>\d+)$', views.scladtov_del, name='scladtov_minus'), 
    url(r'^minisclad/minus/(?P<pk>\d+)$', views.scladtov_minus, name='scladtov_minus'),
    url(r'^minisclad/plus/(?P<pk>\d+)$', views.scladtov_plus, name='scladtov_plus'),
    url(r'^minisclad/srok_god/$', views.scladtov_srokgod, name='scladtov_srokgod'),
    url(r'^minisclad/srok_2god/$', views.scladtov_srok2god, name='scladtov_srok2god'),
    url(r'^minisclad/prosrocheno/$', views.scladtov_prosrocheno, name='scladtov_prosrocheno'),
    url(r'^sclad/tov/$', views.tovar, name='sclad_tovar'),
    url(r'^sclad/tov_new/$', views.tov_new, name='tov_new'),
    url(r'^tovar/(?P<pk>\d+)/edit/$', views.tov_edit, name='tov_edit'),
    url(r'^tovar/(?P<pk>\d+)$', views.tov_del, name='tov_minus'),
    url(r'^auth/login/$', views.login, name='myloginsys'),  
    url(r'^auth/logout/$', views.logout, name='mylogoutsys'),  
    url(r'^$', views.myminisclad, name='minisclad'), 

]