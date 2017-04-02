from django.conf.urls import  include, url
from django.contrib import admin
from speed_app import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]

