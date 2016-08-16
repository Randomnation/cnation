from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^order/', include('ordering.urls', namespace='order')),
]
