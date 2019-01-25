from django.db import models

# Create your models here.

class Test(models.Model):
    type1 = models.CharField(max_length=15)
    type2 = models.CharField(max_length=15)


class ABL_UPLOAD_DATA_FUNDPRICE(models.Model):
    strBasicDate = models.CharField(max_length=10, null=False)
    strClassFundCode = models.CharField(max_length=10, null=False)
    strModifyBasicPrice = models.CharField(max_length=10, null=True)
    strBasicPriceDayVariation = models.CharField(max_length=10, null=True)
    strBasicTablePrice = models.CharField(max_length=10, null=True)
    strBasicTablePriceDayVariation = models.CharField(max_length=10, null=True)
    strAssetTotal = models.CharField(max_length=10, null=True)
    strSetAccount = models.CharField(max_length=10, null=True)
    strBasicPrice = models.CharField(max_length=10, null=True)


class ABL_UPLOAD_DATA_DISTRIBUTORINFO(models.Model):
    strBasicDate =  models.CharField(max_length=10)
    strClassFundCode = models.CharField(max_length=10, null=True, blank=True)
    strSellerCode = models.CharField(max_length=10, null=True, blank=True)

class ABL_UPLOAD_DATA_RISKANALYSIS(models.Model):
    strBasicDate 			= models.CharField(max_length=10, null=False)
    strClassFundCode 		= models.CharField(max_length=10, null=False)
    strMonthBase 			= models.CharField(max_length=10, null=True)
    strStandardDeviation 	= models.CharField(max_length=10, null=True)
    strMarketSensitive 		= models.CharField(max_length=10, null=True)
    strSharpRatio 			= models.CharField(max_length=10, null=True)
    strIR 					= models.CharField(max_length=10, null=True)
    strStandardDeviation2 	= models.CharField(max_length=10, null=True)
    
    
class ABL_UPLOAD_DATA_FUNDPERFORMANCE(models.Model):
    strBasicDate 				= models.CharField(max_length=10, null=False)
    strClassFundCode 			= models.CharField(max_length=10, null=False)
    strStock 					= models.CharField(max_length=10, null=True)
    strBond 					= models.CharField(max_length=10, null=True)
    strBeneficiaryCertificate 	= models.CharField(max_length=10, null=True)
    stShortTerm 				= models.CharField(max_length=10, null=True)
    strPF1D 					= models.CharField(max_length=10, null=True)
    strBM1D 					= models.CharField(max_length=10, null=True)
    strPF1M 					= models.CharField(max_length=10, null=True)
    strBM1M 					= models.CharField(max_length=10, null=True)
    strPF3M 					= models.CharField(max_length=10, null=True)
    strBM3M 					= models.CharField(max_length=10, null=True)
    strPF6M 					= models.CharField(max_length=10, null=True)
    strBM6M 					= models.CharField(max_length=10, null=True)
    strPF1Y 					= models.CharField(max_length=10, null=True)
    strBM1Y 					= models.CharField(max_length=10, null=True)
    strPF2Y 					= models.CharField(max_length=10, null=True)
    strBM2Y 					= models.CharField(max_length=10, null=True)
    strPF3Y 					= models.CharField(max_length=10, null=True)
    strBM3Y 					= models.CharField(max_length=10, null=True)
    strPF5Y 					= models.CharField(max_length=10, null=True)
    strBM5Y 					= models.CharField(max_length=10, null=True)
    strPFYTD 					= models.CharField(max_length=10, null=True)
    strBMYTD 					= models.CharField(max_length=10, null=True)
    strPFSINCE 					= models.CharField(max_length=10, null=True)
    strBMSINCE 					= models.CharField(max_length=10, null=True)

class ABL_UPLOAD_DATA_HOLDINGTOP5SECTOR(models.Model):
    strBasicDate 		= models.CharField(max_length=10, null=False)
    strClassFundCode 	= models.CharField(max_length=10, null=False)
    strSectorType 		= models.CharField(max_length=10, null=False)
    StrOrder 			= models.CharField(max_length=10, null=False)
    strSectorNAme 		= models.CharField(max_length=100, null=True)
    strImportance 		= models.CharField(max_length=10, null=True)



