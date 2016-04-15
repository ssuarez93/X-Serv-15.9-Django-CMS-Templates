from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', 'cms_templates.views.profile'),
    url(r'^pages$', 'cms_templates.views.lista_paginas'),
    url(r'^$', 'cms_templates.views.lista_paginas'),
    url(r'^annotated/(\d+)$', 'cms_templates.views.annotated_identificador'),
    url(r'^annotated/(.*)$', 'cms_templates.views.annotated_recurso'),
    url(r'^(\d+)$', 'cms_templates.views.identificador'),
    url(r'^(.*)$', 'cms_templates.views.recurso')
)
