from django.contrib.auth.models import User, Group
from rest_framework import viewsets, serializers
from .serializers import UserSerializer, GroupSerializer, TestSerializer, ABL_UPLOAD_DATA_FUNDPRICESerializer, ABL_UPLOAD_DATA_DISTRIBUTORINFOSerializer, ABL_UPLOAD_DATA_RISKANALYSISSerializer, ABL_UPLOAD_DATA_FUNDPERFORMANCESerializer, ABL_UPLOAD_DATA_HOLDINGTOP5SECTORSerializer
from quickstart.models import Test, ABL_UPLOAD_DATA_FUNDPRICE, ABL_UPLOAD_DATA_DISTRIBUTORINFO, ABL_UPLOAD_DATA_RISKANALYSIS, ABL_UPLOAD_DATA_FUNDPERFORMANCE, ABL_UPLOAD_DATA_HOLDINGTOP5SECTOR

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class ABL_UPLOAD_DATA_FUNDPRICEViewSet(viewsets.ModelViewSet):
    queryset = ABL_UPLOAD_DATA_FUNDPRICE.objects.all()
    serializer_class = ABL_UPLOAD_DATA_FUNDPRICESerializer


class ABL_UPLOAD_DATA_DISTRIBUTORINFOViewSet(viewsets.ModelViewSet):
    queryset = ABL_UPLOAD_DATA_DISTRIBUTORINFO.objects.all()
    serializer_class = ABL_UPLOAD_DATA_DISTRIBUTORINFOSerializer

class ABL_UPLOAD_DATA_RISKANALYSISViewSet(viewsets.ModelViewSet):
    queryset = ABL_UPLOAD_DATA_RISKANALYSIS.objects.all()
    serializer_class = ABL_UPLOAD_DATA_RISKANALYSISSerializer

class ABL_UPLOAD_DATA_FUNDPERFORMANCEViewSet(viewsets.ModelViewSet):
    queryset = ABL_UPLOAD_DATA_FUNDPERFORMANCE.objects.all()
    serializer_class = ABL_UPLOAD_DATA_FUNDPERFORMANCESerializer

class ABL_UPLOAD_DATA_HOLDINGTOP5SECTORViewSet(viewsets.ModelViewSet):
    queryset = ABL_UPLOAD_DATA_HOLDINGTOP5SECTOR.objects.all()
    serializer_class = ABL_UPLOAD_DATA_HOLDINGTOP5SECTORSerializer