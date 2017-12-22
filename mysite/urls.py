"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^', include('blog.urls', namespace = 'post', app_name = 'post')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/blog/', include('blog.api.urls', namespace = 'blog_api')),
    url(r'^api-token-auth', obtain_jwt_token),
    url(r'^api-token-verify', verify_jwt_token)
    # url(r'^api/account/', include('account.api.urls', namespace = 'account_api'))
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
