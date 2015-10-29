import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook

print "This script runs"
wb = load_workbook(filename="Spring.xlsx")
sheet_ranges = wb['Sheet1']
f = open('max_run_four.txt', 'w')
xdata = [][]
ydata = [][]
for i in range(3, 20000):
	collum = 'K'
	xcollum = 'J'
	var1 = collum+str(i)
	var2 = collum+str(i+1)
	varx = xcollum+str(i)
	var0 = collum+str(i-1)
	first = (sheet_ranges[var1].value)
	xfirst = sheet_ranges[varx].value
	second = (sheet_ranges[var2].value)
	last = (sheet_ranges[var0].value)
	#TODO: Make sure that the max and the min actually work-- seems like the problem is the casting
	#TODO: The problem could also be that the points zig zag as the time goes on... I can not tell
	if((first > second) and (first > last)):
		xdata.append(xfirst)
		ydata.append(first)
		#s = str(sheet_ranges[varx].value) + ",\t" + str(sheet_ranges[var1].value)+",\n"
		#f.write(s)
#print xdata
#print ydata
f.close()
plt.plot(xdata, ydata, 'k.')
plt.show()
