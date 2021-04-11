from django.conf.urls import url
from api import views

urlpatterns = [
    url('sunexposures', views.sunexposure_list),
    url(r'sunexposures/(?P<pk>[0-9A-Za-z]+)$', views.sunexposure_detail)
]