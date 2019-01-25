from django.contrib.auth.models import User, Group
from .models import Test,  ABL_UPLOAD_DATA_FUNDPRICE, ABL_UPLOAD_DATA_DISTRIBUTORINFO, ABL_UPLOAD_DATA_RISKANALYSIS, ABL_UPLOAD_DATA_FUNDPERFORMANCE, ABL_UPLOAD_DATA_HOLDINGTOP5SECTOR
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields  = ('url', 'name')


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields  = ('type1', 'type2')

class ABL_UPLOAD_DATA_FUNDPRICESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ABL_UPLOAD_DATA_FUNDPRICE
        fields = ('strBasicDate', 
                'strClassFundCode', 
                'strModifyBasicPrice', 
                'strBasicPriceDayVariation', 
                'strBasicTablePrice', 
                'strBasicTablePriceDayVariation', 
                'strAssetTotal', 
                'strSetAccount',
                'strBasicPrice')

class ABL_UPLOAD_DATA_DISTRIBUTORINFOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ABL_UPLOAD_DATA_DISTRIBUTORINFO
        fields = ('strBasicDate', 'strClassFundCode', 'strSellerCode')

class ABL_UPLOAD_DATA_RISKANALYSISSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ABL_UPLOAD_DATA_RISKANALYSIS
        fields = ('strBasicDate', 
                'strClassFundCode', 
                'strModifyBasicPrice', 
                'strMonthBase', 
                'strStandardDeviation', 
                'strMarketSensitive', 
                'strSharpRatio', 
                'strIR',
                'strStandardDeviation2')

class ABL_UPLOAD_DATA_FUNDPERFORMANCESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ABL_UPLOAD_DATA_FUNDPERFORMANCE
        fields = ('strBasicDate', 
                'strClassFundCode', 
                'strStock', 
                'strBond', 
                'strBeneficiaryCertificate', 
                'stShortTerm', 
                'strPF1D', 
                'strBM1D',
                'strPF1M',
                'strBM1M', 
                'strPF3M', 
                'strBM3M', 
                'strPF6M', 
                'strBM6M', 
                'strPF1Y', 
                'strBM1Y',
                'strPF2Y',
                'strBM2Y', 
                'strPF3Y',
                'strBM3Y',
                'strPF5Y', 
                'strBM5Y', 
                'strPFYTD', 
                'strBMYTD', 
                'strPFSINCE', 
                'strBMSINCE')

class ABL_UPLOAD_DATA_HOLDINGTOP5SECTORSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ABL_UPLOAD_DATA_HOLDINGTOP5SECTOR
        fields = ('strBasicDate', 
                'strClassFundCode', 
                'strSectorType', 
                'StrOrder', 
                'strSectorNAme', 
                'strImportance')           