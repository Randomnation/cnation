from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.main_page, name='index'),
    url(r'^contact/$', views.contact_page, name='contact'),
]
