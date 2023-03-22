from django.shortcuts import render
from django.http import HttpResponse
from .models import Table, DataSchema
from .forms import CreateNewSchema
import csv

# Create your views here.
name = ""
n = 0
tableItems = ["Full Name","Id","E-mail","Phone Number","Address","Job","Company"]
message = ""


# Displays all tables in the database:
def index(response):
	table = Table.objects.all()
	return render(response, "main/home.html", {"table": table})

# Displays form, generates tables
def create(response):
	global message
	# Generating table
	if response.method == "POST":
		form = CreateNewSchema(response.POST)
		if form.is_valid():
			# Checking is table name has been taken:
			name = form.cleaned_data["name"]
			name = checkName(name)

			if name != "":
				# Create table
				schema = Table(name = name)

				# Cleaning data from the form (column_ids and number of records)
				b = ""
				for i in range(len(tableItems)):
					if form.cleaned_data["check"+str(i+1)]:
						b += "1"
					else:
						b += "0"
				if b == "0000000":
					b = "1111111"
				schema.col_ids = b

				schema.save()

				n = form.cleaned_data["n"]
				for r in range(n):
					record = schema.records.create()
					for i in range(len(b)):
						if b[i] == "1":
							record.CreateField(i)
					record.save()
			
				schema.save()

				# Displaying table info
				message = "Table " + name + " has been generated."
				label = True
			else: 
				message = "Failed to create table, name is invalid."
	else:
		# Creating a new form
		form = CreateNewSchema()
		message = ""
		label = False
	return render(response, "main/create.html", {"form": form, "message": message, "label":label})

def table_csv(request, name):
	# Accessing all table names
	names = []
	for T in Table.objects.all():
		names.append(T.name)
	# Checking if table with given name exists
	if names.count(name) == 0:
		return HttpResponse('')

	# Creating file
	fn = name+".csv"
	response = HttpResponse(
	    content_type='text/csv',
	    headers={'Content-Disposition': 'attachment; filename='+fn},
	    )
	writer = csv.writer(response)
	# Accessing table
	table = Table.objects.get(name = name)

	# Writing header to csv file
	selectedItems = []
	for i in range(len(table.col_ids)):
		if table.col_ids[i] == "1":
			selectedItems.append(tableItems[i])

	writer.writerow(selectedItems)

	# Writing table records
	for t in table.records.all():
		row = table.CreateRow(t)
		writer.writerow(row)
	return response


# Checks if name exists and if so, generates a new name
def checkName(n):
	names = []
	for T in Table.objects.all():
		names.append(T.name)
	if names.count(n) == 0:
		return n
	else:
		return generateName(names, n)

def generateName(names, n):
	for i in range(1,30):
		newName= n + "_" + str(i)
		if names.count(newName) == 0:
			return newName;
	return ""

