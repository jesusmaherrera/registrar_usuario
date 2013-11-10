from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^registrar/', 'registrar_usuario.apps.usuarios.views.registrar', name='registrar'),
    url(r'^$', 'registrar_usuario.apps.usuarios.views.usuarios', name='usuarios'),
    # url(r'^registrar_usuario/', include('registrar_usuario.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
