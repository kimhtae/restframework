"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'test', views.TestViewSet)
router.register(r'ABL_UPLOAD_DATA_FUNDPRICE', views.ABL_UPLOAD_DATA_FUNDPRICEViewSet)
router.register(r'ABL_UPLOAD_DATA_DISTRIBUTORINFO', views.ABL_UPLOAD_DATA_DISTRIBUTORINFOViewSet)
router.register(r'ABL_UPLOAD_DATA_RISKANALYSIS', views.ABL_UPLOAD_DATA_RISKANALYSISViewSet)
router.register(r'ABL_UPLOAD_DATA_FUNDPERFORMANCE', views.ABL_UPLOAD_DATA_FUNDPERFORMANCEViewSet)
router.register(r'ABL_UPLOAD_DATA_HOLDINGTOP5SECTOR', views.ABL_UPLOAD_DATA_HOLDINGTOP5SECTORViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]
