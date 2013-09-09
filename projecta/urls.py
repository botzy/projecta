from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projecta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('accounts.urls', namespace="accounts")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'accounts.views.login_user'),
    url(r'^login/$', 'accounts.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
)
