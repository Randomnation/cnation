from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.main_page, name='index'),
    url(r'^contact/$', views.contact_page, name='contact'),
    url(r'^user/profile/(?P<pk>\d+)/edit/$', views.profile_update, name='update_profile'),
    url(r'^user/profile/$', views.user_profile, name='user_profile'),


    # User Auth

    url(r'^login/', 'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'main/login.html'}),

    url(r'^logout/', 'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'template_name': 'main/index.html'}),


    # User registration

    url(r'^register/', 'main.views.register_user', name='register'),
]
