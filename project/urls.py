
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'nombres/$', "cms_put.views.dame_nombres"),
    url(r'^admin/', (admin.site.urls)),
    url(r'^(.*)$', "cms_put.views.mostrar"),
]
