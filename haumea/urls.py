"""haumea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token


# admin.site.index_template = 'admin/haumea_index.html'
# admin.site.site_header = '买卖通'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^store/', include('store.urls.web')),
    url(r'^goods/', include('scrapy.urls.web')),
]

urlpatterns += [
    url(r'^api/auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^api/get-token/', obtain_auth_token),
    url(r'^api/scrapy/', include('scrapy.urls.api')),
    url(r'^api/', include('store.urls.api')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
