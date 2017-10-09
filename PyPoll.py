import os	
import csv
#islice will allow to skip the first row
from itertools import islice


DataSet = input("Please type the number of the data set you would like to work with: ")

Filename = 'election_data_'+DataSet+'.csv'

candidate = {}
rowcount = 0

#create path to call csv files
csvpath = os.path.join('.' , 'Resources' , Filename)

with open(csvpath, newline = '') as electioncsv:
	electionreader = csv.reader(electioncsv, delimiter=',')

	for row in islice(electionreader, 1, None):
		rowcount += 1
		if not row[2] in candidate:
			candidate[row[2]] = 1
		else:
			candidate[row[2]] += 1
	print ('Election Results   ')
	print('---------------------------')
	print('Total Votes:  ' + str(rowcount))		
	print('---------------------------')
	winning_vote = 0
	winner = None

	for key in candidate:
		percent = (float(candidate[key] / rowcount))*100
		if candidate[key] > winning_vote:
			winning_vote = candidate[key]
			winner = key
		print(key +': ' + str(int(percent))+'.0%' + ' ('+str(candidate[key])+')')
	print('---------------------------')
	print('Winner: ' + winner)
	print('---------------------------')


	

