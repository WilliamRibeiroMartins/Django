from django.conf.urls import url
from coredrca import views

urlpatterns = [
    url(r'^artigo/', views.artigo),
]

'''
urlpatterns = patterns('',
(r'^$', views.artigo()),'')
'''