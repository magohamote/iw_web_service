import intelliwineApp
from django.conf.urls import include, url
from rest_framework import routers
from intelliwineApp import views
from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'bottles', views.BottleViewSet)

urlpatterns = [
    url(r'^$', intelliwineApp.views.index, name='index'),
    # url(r'^db', intelliwineApp.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('intelliwineApp.urls')),
]
