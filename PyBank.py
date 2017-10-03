 #import modules needed to call csv files
import os	
import csv
from itertools import islice

#user input for which csv file to work with
#possible to set csv names as variables?
DataSet = input("Please type the number of the data set you would like to work with: ")

Filename = 'budget_data_'+DataSet+'.csv'



#create path to call csv files
csvpath = os.path.join('.' , 'Resources' , Filename)

with open(csvpath, newline = '') as budgetcsv:
	budgetreader = csv.reader(budgetcsv, delimiter=',')
	print('                   ')
	print ('Financial Analysis')
	print(' ------------------------')

	rownumber = 0
	revenue = 0
	prevMonth = None
	currentMonth = None
	highestMonth = None
	lowestMonth = None
	# difference = budgetreader[0][1]
	difference =None	
	highestDiff = 0
	lowestDiff = 0

	for row in islice(budgetreader, 1, None):
		rownumber += 1
		revenue = (int(row[1])) + revenue
		if prevMonth == None:
			prevMonth = row
			continue 
		currentMonth = row
		difference = int(currentMonth[1]) - int(prevMonth[1])
		if difference > highestDiff:
			highestDiff = difference
			highestMonth = row[0]
		elif difference < lowestDiff:
			lowestDiff = difference
			lowestMonth = row[0]
		prevMonth = row
		
		


	avgrev = revenue / rownumber

	print ('Total Months: ' + str(rownumber))
	print ('Total Revenue: ' + '$'+str(revenue)+'.00')
	print ('Average Revenue Change: ' + '$'+ str(int(avgrev)) +'.00')
	print ('Greatest Increase in Revenue: ' + highestMonth + ' ($'+ str(highestDiff) +'.00)')
	print ('Greatest Decrease in Revenue: ' + lowestMonth + ' ($'+ str(lowestDiff) +'.00)')
	print('										')
	print('-------------------------------------')
	
