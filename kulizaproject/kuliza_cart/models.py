from django.db import models

# Create your models here.
class ItemCategory(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_desc = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.cat_name

class ItemSubCategory(models.Model):
	subcat_name = models.CharField(max_length=50)
	subcat_desc = models.TextField(blank=True, null=True)
	category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.subcat_name

class Product(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField(blank=True, null=True)
	sub_category = models.ForeignKey(ItemSubCategory, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='productImages',blank=True, null=True)
	price = models.FloatField(default=0)

	def __str__(self): # use __unicode__ for python 2
		return self.name

class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	item_qty = models.IntegerField()
	user = models.IntegerField(blank=True,null=True)
	sold = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class MyCatalog(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField(blank=True, null=True)
	sub_category = models.ForeignKey(ItemSubCategory, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='catalogImages',blank=True, null=True)
	price = models.FloatField(default=0)
	user = models.IntegerField(blank=True,null=True)

	def __str__(self): # use __unicode__ for python 2
		return self.name

		
