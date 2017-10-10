from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tovar, name='sclad_tovar'),
]