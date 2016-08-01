from django.conf.urls import url
from ordering import views


urlpatterns = [
    url(r'^$', views.order_page, name='order'),
]
