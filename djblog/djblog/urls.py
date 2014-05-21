from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', include('blog.urls')),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^post/(?P<pk>\d+$)', 'blog.views.post', name='post'),
)
