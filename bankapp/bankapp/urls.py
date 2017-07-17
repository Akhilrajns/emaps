"""bankapp URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from bankapp.views import Login, Loan, AddressList, UpdateLatLong
from bankapp.generatepdf import MyPDFView
from home.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home,  name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/user/login/$', Login.as_view(), name='login'),
    url(r'^api/v1/user/loan/$', Loan.as_view(), name='loan'),
    url(r'^api/v1/user/address/$', AddressList.as_view(), name='address'),
    url(r'^api/v1/user/update-address/$', UpdateLatLong.as_view(), name='update-address'),
    url(r'^admin/pdf_generate/(?P<pk>[0-9]+)/$', MyPDFView.as_view(), name='pdf_generate')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
