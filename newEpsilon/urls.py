from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index, name = 'index'),
    url(r'registrationform$',views.registrationform, name = 'registrationform'),
    url(r'recorded',views.recorded, name = 'recorded'),
    url(r'loginform',views.loginform, name = 'loginform'),
    url(r'postregistration',views.postregistration, name = 'postregistration'),
    url(r'logout',views.logoutG, name = 'logoutG'),
    url(r'postlogin',views.postlogin, name = 'postlogin'),
    url(r'events',views.events, name = 'events'),
    url(r'about',views.about, name = 'about'),
    url(r'^save_record/(?:(?P<report_type>.+)/)?$', views.save_record, name='save_record'),
]
