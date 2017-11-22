"""autoSearch URL Configuration

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
from carros import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^prueba/', views.home),
    url(r'^list/$', views.car_list.as_view(), name='CarList'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.car_detail.as_view(), name='carDetail'),
    url(r'^detail/(?P<pk>[0-9]+)/delete/$',views.CarDeleteView.as_view(), name='carDelete'),
    url(r'^create$',views.CarCreateView.as_view(), name='carCreate'),
    url(r'^detail/(?P<pk>[0-9]+)/edit/$',views.CarUpdateView.as_view(), name='carUpdate'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
