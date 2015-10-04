from api.models import store, storeItem
from random import randint

names = ['Shukla', 'Anand', 'Raja', 'Agarwal']
categoryNames = ['', ' Photographers', ' Textiles', ' Emporium', ' Book Store', ' Electronics', ' Repair Store', 'Foods' ]
lat = 22.319876
lng = 87.317657

def populateStores(categoryID):

	id = 0

	for name in names:
		q = store(storeID = ("ST" + str(categoryID) + str(id)) , storeName = name + categoryNames[categoryID], storeCategoryID = str(categoryID), storeLat = (lat + 0.001*randint(-9,9)), storeLong = (lng + 0.001*randint(-9,9)), storeAddress = ("Test Address " + str(categoryID) + str(id)), storeOpenTime = "0930", storeCloseTime = "1730", storePhone = str(9999900000 + 1000*randint(-9,9)))


		q.save()

		id += 1

def populateStoreItems(sID, storeObject):

	id = 0

	for i in range(15):
		q = storeItem(itemID = str(sID) + str(id), storeID = storeObject, itemName = "Test Item I" + str(sID) + str(id), 
			itemPrice = randint(100, 500), availableUnits = randint(1,15))
		q.save()

		id += 1


def popStoreItems():

	for c in range(1,8):
		for s in range(4):
			populateStoreItems(("ST"+str(c)+str(s)), store.objects.get(storeID = "ST"+str(c)+str(s)))


def popStores():

	for c in range(1,8):
		populateStores(c)

if __name__ == "__main__":
	main()


