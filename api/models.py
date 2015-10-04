from django.db import models

class store(models.Model):
	storeID = models.CharField(max_length = 50, primary_key = True)
	storeName = models.CharField(max_length = 50)
	storeCategoryID = models.CharField(max_length = 2,default=None)
	storeLat = models.FloatField()
	storeLong = models.FloatField()
	storeAddress = models.TextField()
	storeOpenTime = models.CharField(max_length = 4)
	storeCloseTime = models.CharField(max_length = 4)
	storePhone = models.CharField(max_length = 10)
	
	#storePic = models.ImageField(upload_to="/home/aaniket/dev/storeDiscoveryAPI/media/images", default = 1)


class storeItem(models.Model):
	itemID = models.CharField(max_length = 50, primary_key = True)
	storeID = models.ForeignKey('store')
	itemName = models.CharField(max_length=50)
	itemPrice = models.FloatField()
	#itemPic = models.ImageField( upload_to = '/home/aaniket/dev/storeDiscoveryAPI/media/images', default = 1)
	availableUnits = models.IntegerField(default = 0)

