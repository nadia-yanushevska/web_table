from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from faker import Faker
import random, string

# Create your models here.

class Table(models.Model):
	name = models.CharField(max_length = 30, null = "True")
	col_ids = models.CharField(max_length = 7, null = "True")

	# Creates record according to column_ids
	def CreateRow(self, record):
		r = []
		for i in range(len(self.col_ids)):
			if self.col_ids[i] == "1":
				r.append(record.getField(i))
		return r

	def __str__(self):
		return self.name



class DataSchema(models.Model): #column names
	table = models.ForeignKey(Table, on_delete=models.CASCADE, null = "True", related_name ="records")
	fullName = models.CharField(max_length = 30, null = "True")
	personId = models.CharField(max_length = 30, null = "True")
	eMail = models.CharField( max_length = 50, null = "True")
	phoneNumber = models.CharField(max_length = 30, null = "True")
	address = models.CharField(max_length = 50, null = "True")
	job = models.CharField( max_length = 50, null = "True")
	companyName = models.CharField( max_length = 50, null = "True")

	# Access field by id
	def getField(self, col_id):
		match col_id:
			case 0:
				return self.fullName
			case 1:
				return self.personId
			case 2:
				return self.eMail
			case 3:
				return self.phoneNumber
			case 4:
				return self.address
			case 5:
				return self.job
			case 6:
				return self.companyName

	# Creates a fake data field according to col_id
	def CreateField(self, col_id):
		fake = Faker()
		tel_fake = Faker("uk-UA")
		match col_id:
			case 0:
				self.fullName = fake.name()
			case 1:
				self.personId = random.choice(string.ascii_uppercase) + str(random.randint(100,999))
			case 2:
				self.eMail = fake.ascii_free_email()
			case 3:
				self.phoneNumber = tel_fake.phone_number()
			case 4:
				self.address = fake.address()
			case 5:
				self.job = fake.job()
			case 6:
				self.companyName = fake.company()

	def __str__(self):
		return self.table.name
