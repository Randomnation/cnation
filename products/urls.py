from django.conf.urls import url
from products import views


urlpatterns = [
    url(r'^$', views.products_page, name='products'),
]
