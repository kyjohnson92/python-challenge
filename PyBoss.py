 #import modules needed to call csv files
import csv
import os
from itertools import islice
import datetime

#user input for which csv file to work with
#possible to set csv names as variables?
x = "Y"
empID =[]
empName =[]
empDOB = []
ssn = []
empSSN =[]
state = []
empFirstName =[]
empLastName =[]
DOB=[]
SSN =[]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

while x == "Y":


	DataSet = input("Please type the number of the data set you would like to import: ")

	Filename = 'employee_data'+DataSet+'.csv'



#create path to call csv files
	csvpath = os.path.join('.' , 'Resources' , Filename)

	with open(csvpath, newline = '') as employeecsv:
		employeereader = csv.reader(employeecsv, delimiter=',')

		for row in islice(employeereader,1, None):
			empID.append(row[0])
			
			empName.append(row[1])
			empDOB.append(row[2])
			ssn.append(row[3])
			state.append(us_state_abbrev[row[4]])

		empFirstName.append([i.split(' ',)[0] for i in empName])
		empLastName.append([i.split(' ',)[1] for i in empName])
		SSN = [i.split('-')[2] for i in ssn]
		for i in SSN:
			empSSN.append('***-**-'+ i)
		DOB.append([datetime.datetime.strptime(str(i), '%Y-%m-%d').strftime('%m/%d/%Y') for i in empDOB])

	print(SSN)		
	newEmployeeData = zip(empID,empFirstName,empLastName,empSSN,DOB,state)
	
		
	#export to new CSV
	newcsvpath = os.path.join('.', 'Resources' ,'newEmployeeData.csv' )
	with open(newcsvpath, 'w', newline ='') as newemployeecsv:
		wr = csv.writer(newemployeecsv, delimiter=',')
		wr.writerow(['ID','First Name', 'Last Name', 'SSN', 'DOB', 'State'])
		wr.writerows(empID)



		

	x = input('Would you like to continue? (Y) or (N) ')