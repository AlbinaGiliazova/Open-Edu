"""
Definition of urls for DjangoWebProject3.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.views.generic.base import RedirectView

import app.forms
import app.views

from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Войти',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

     url(r'^favicon\.ico$', RedirectView.as_view(url='/static/app/img/favicon.ico', permanent=True)),
     url(r'^pool$', app.views.pool, name='pool'),
     url(r'^pool_post$', app.views.pool, name='pool_post'),
     url(r'^registration$', app.views.registration, name='registration'),
     url(r'^blog$', app.views.blog, name='blog'),
     url(r'^newpost$', app.views.newpost, name='newpost'),
     url(r'^video$', app.views.videopost, name='video'),
     url(r'^(?P<parameter>\d+)/$', app.views.blogpost, name='blogpost'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()