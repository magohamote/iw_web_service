from django.conf.urls import url
from intelliwineApp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^bottles/$', views.bottle_list),
    url(r'bottles/(?P<pk>[0-9]+)', views.bottle_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
