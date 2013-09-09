from django.conf.urls import patterns, include, url

from accounts import views

urlpatterns = patterns('',
    # Examples:
    
    url(r'^login/$', views.login_user, name='login'),
    #url(r'^users/(?P<username>.+)', views.user_details, name = 'details')
)
