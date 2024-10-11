from django.db import models
import datetime

# Create your models here.

# Vin model
class Vin(models.Model):
	vin_number = models.CharField(max_length=20, default=None, unique= True)

	def __str__(self):
		return self.vin_number



#Identification and Technical Specification
class Specs(models.Model):
	vin_number = models.OneToOneField(Vin, on_delete=models.CASCADE, related_name='specs')
	vehicle_id = models.CharField(max_length=20, default='')
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	body_type = models.CharField(max_length=30)
	manufacture_year = models.CharField(max_length=4)
	engine_code = models.CharField(max_length=10)
	powertrain_power =  models.CharField(max_length=5)
	transmission_type = models.CharField(max_length=10)
	image = models.ImageField(upload_to='uploads/vin')

	def __str__(self):
		return self.vehicle_id


#160-Point-Check
class Inspection(models.Model):

	RESULT_CHOICES = [
		("PAS", "Passed"),
		("PMD",  "Passed with minor Defects"),
		("PJD", "Passed with major Defects"),
		("FMD",  "Failed due to minor Defects"),
		("FJD",  "Failed due to major Defects"),
		("FAI",  "Failed"),
	]

	vin_number = models.ForeignKey(Vin, on_delete=models.CASCADE, related_name='inspections')
	inspection_number = models.CharField(max_length=20)
	year = models.CharField(max_length=4)
	inspection_result = models.CharField(max_length=30, 
	choices=RESULT_CHOICES)
	ag_rating = models.CharField(max_length=30)
	inspection_date = models.DateField()
	link_to_results = models.CharField(max_length=200)

	def __str__(self):
		return self.inspection_number

#Vehicle History
class History(models.Model):
	vin_number = models.ForeignKey(Vin, on_delete=models.CASCADE, related_name='history')
	date_of_service = models.DateField()
	mileage_at_service = models.IntegerField()
	worked_performed = models.CharField(max_length=200)
	performed_by = models.CharField(max_length=50)
	cost = models.DecimalField(max_digits=6, default=0, decimal_places=2)
	notes = models.CharField(max_length=2000, blank=True)

	def __int__(self):
		return self.vin_number
