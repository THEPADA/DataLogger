from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.waterLogList, name='waterLogList'),
    url(r'^logIt/$',views.waterLogReciever, name='waterLogReciever')
]
