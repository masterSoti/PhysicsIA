from openpyxl import load_workbook

print "THis script runs"
wb = load_workbook(filename="Spring.xlsx")
sheet_ranges = wb['Sheet1']
f = open('max_run_four.txt', 'w')
for i in range(3, 20000):
	collum = 'K'
	xcollum = 'J'
	var1 = collum+str(i)
	var2 = collum+str(i+1)
	varx = xcollum+str(i)
	first = sheet_ranges[var1].value
	second = sheet_ranges[var2].value
	if(first > second):
		s = str(sheet_ranges[varx].value) + ",\t" + str(sheet_ranges[var1].value)+",\n"
		f.write(s)
f.close()
