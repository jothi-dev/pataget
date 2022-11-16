from django.db import models

# Create your models here.
class Fund(models.Model):
	name = models.CharField(max_length=50)	
	allocation = models.IntegerField()

	# Queries
	def get_by_name(fund_name):
		Fund.objects.filter(name=fund_name)
