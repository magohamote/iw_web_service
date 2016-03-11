from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'intelliwineProject.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', intelliwineApp.views.index, name='index'),
    url(r'^db', intelliwineApp.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
