from openpyxl import load_workbook

wb = load_workbook(filename="Spring.xlsx")
sheet_ranges = wb['Sheet1']
f = open('max.txt', 'w')
collum = raw_input("Please enter the Collum of the max that you want to find...\n")
for i in range(3, 20000):
	collum = str(collum)
	var1 = collum+str(i)
	var2 = collum+str(i+1)
	first = sheet_ranges[var1].value
	second = sheet_ranges[var2].value
	if(first > second):
		s = str(sheet_ranges[var1].value)+",\n"
		f.write(s)
f.close()
