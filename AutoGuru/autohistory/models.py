from django.db import models
import datetime

# Create your models here.

#Identification and Technical Specification
class Vin(models.Model):
	vin_number = models.IntegerField(default='1')
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	body_type = models.CharField(max_length=30)
	manufacture_year = models.IntegerField()
	engine_code = models.CharField(max_length=10)
	powertrain_power =  models.IntegerField()
	transmission_type = models.CharField(max_length=10)
	image = models.ImageField(upload_to='uploads/vin')

	def __str__(self):
		return self.vin_number


#160-Point-Check
class Inspection(models.Model):
	inspection_number = models.IntegerField()
	year = models.IntegerField()
	inspection_result = models.CharField(max_length=10)
	ag_rating = models.IntegerField()
	inspection_date = models.DateField()
	link_to_results = models.CharField(max_length=10)

	def __str__(self):
		return self.inspection_number

#Vehicle History
class History(models.Model):
	date_of_service = models.DateField(default=datetime.datetime.today)
	mileage_at_service = models.IntegerField()
	worked_performed = models.CharField(max_length=10)
	performed_by = models.CharField(max_length=10)
	cost = models.DecimalField(default=0, decimal_places=2)
	notes = models.CharField(max_length=2000)

	def __str__(self):
		return self.date_of_service
