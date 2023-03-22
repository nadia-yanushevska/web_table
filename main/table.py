class Table:
	header = ["Record ID"]
	schemaItems = ["Full name","PersonId"] #,"E-mail","Phone number","Address","Job","Company name"]
	table = [] 

	def createTable(*cols): #cols as array of true false
		global header, table
		for i in range(len(cols)):
			if cols[i]:
				header.append(schemaItems[i])
		table.append(header)

	def populateTable(rows):
		global table
		# for loop throgh rows and populate them
		for r in range(rows):
			table.append(createRecord())

	def createRecord():
		global header
		# loop through columns and populate
		# findColType
		record = []
		for c in header:
			record.append(populateCell(c))
		return record

	def populateCell(s):
		colType = -1
		for i in range(len(schemaItems)):
			if schemaItems[i] == s:
				colType = i
		if colType == 1:
			return "FL Name"
		elif colType == 2:
			return 1
		return 3

	def getTable(self):
		return self.table

