from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),
)
