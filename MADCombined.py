import csv
import numpy as np
import math
from scipy import stats

#Can change colum ranges within getAllMADCols() and getAllCheckerCols()

nameIn = input("Please enter the full file name: ")

#Returns only the numbers converted to doubles in a column without 'NA'
def getColData(colNum):
	with open(nameIn) as csv_file:
		reader = csv.reader(csv_file, delimiter=',');
		next(reader, None)
		dataSet = [];
		for row in reader:
			if (("na" in row[colNum].lower()) or (" " == row[colNum]) or ('' == row[colNum])):
				continue;
			else:
				dataSet.append(float(row[colNum]))
	return dataSet;

#Copies and removes NA
def dateCopy(colNum):
	with open(nameIn) as csv_file:
		reader = csv.reader(csv_file)
		dataSet = [];
		for row in reader:
			if "NA" in row[colNum]:
				dataSet.append(" ")
			else:
				dataSet.append(row[colNum])
	return dataSet;

#Returns entire column
def getCol(colNum):
	with open(nameIn) as csv_file:
		reader = csv.reader(csv_file, delimiter=',');
		dataSet = [];
		for row in reader:
			dataSet.append((row[colNum])) 
	return dataSet;

#Returns column with removed values
def createNewCol(colNum):
	newCol = []
	#Column without header
	colNums = getCol(colNum)
	newCol.append(colNums[0])
	colNums.pop(0)


	colMAD = stats.median_abs_deviation(getColData(colNum), scale = 1.4826)
	median = np.median(getColData(colNum))

	#Calculates the top and bottom range
	bottom = median - (2.5 * colMAD)
	top = median + (2.5 * colMAD)

	for num in colNums:
		if (("na" in num.lower()) or not num):
			newCol.append(" ")
		elif (float(num) <= top and float(num) >= bottom):
			newCol.append(num)
		else:
			newCol.append(" ")

	return newCol;


def createCheckerCol(colNum):
	newCol = []
	#Column without header
	colNums = getCol(colNum)
	newCol.append(colNums[0])

	colNums.pop(0)


	colMAD = stats.median_abs_deviation(getColData(colNum), scale = 1.4826)
	median = np.median(getColData(colNum))

	#Calculates the top and bottom range
	bottom = median - (2.5 * colMAD)
	top = median + (2.5 * colMAD)

	for num in colNums:
		if (("na" in num.lower()) or not num):
			newCol.append(" ")
		elif (float(num) <= top and float(num) >= bottom):
			newCol.append("0")
		else:
			newCol.append("1")

	return newCol;


#Returns list copied columns and MAD columns for columns with data
def getAllMADCols():
	allMAD = [];

	#Columns begin indexing at 0
	#Use dateCopy() function for columns which just need to be copied
	#Use createNewCol() function when want to run MAD on columns
	#Second number in functin parameter is non inclusive so ex: range(0,2) will only loop "i" 0-1
	for i in range(0,31):
		allMAD.append(dateCopy(i))

	for i in range(31,33):
		allMAD.append(createNewCol(i))

	for i in range(33,39):
		allMAD.append(dateCopy(i))

	for i in range(39,240):
		allMAD.append(createNewCol(i))

	for i in range(240,244):
		allMAD.append(dateCopy(i))

	for i in range(244,644):
		allMAD.append(createNewCol(i))

	allMAD.append(dateCopy(644));

	for i in range(645,765):
		allMAD.append(createNewCol(i))

	allMAD.append(dateCopy(765));

	for i in range(766,886):
		allMAD.append(createNewCol(i))

	allMAD.append(dateCopy(886));

	for i in range(887,1007):
		allMAD.append(createNewCol(i))
	
	allMAD.append(dateCopy(1007));

	for i in range(1008,1128):
		allMAD.append(createNewCol(i))

	allMAD.append(dateCopy(1128));

	for i in range(1129,1249):
		allMAD.append(createNewCol(i))

	allMAD.append(dateCopy(1249));

	for i in range(1250,1433):
		allMAD.append(createNewCol(i))

	allMAD.append(createNewCol(374))
	

	return allMAD;

def getAllCheckerCols():
	allChange = [];

	#Columns begin indexing at 0
	#Use dateCopy() function for columns which just need to be copied
	#Use createCheckerCol() function when want to change columns to "1" or "0"
	#Second number in functin parameter is non inclusive so ex: range(0,2) will only loop "i" 0-1
	for i in range(0,31):
		allChange.append(dateCopy(i))

	for i in range(31,33):
		allChange.append(createCheckerCol(i))

	for i in range(33,39):
		allChange.append(dateCopy(i))

	for i in range(39,240):
		allChange.append(createCheckerCol(i))

	for i in range(240,244):
		allChange.append(dateCopy(i))

	for i in range(244,644):
		allChange.append(createCheckerCol(i))

	allChange.append(dateCopy(644));

	for i in range(645,765):
		allChange.append(createCheckerCol(i))

	allChange.append(dateCopy(765));

	for i in range(766,886):
		allChange.append(createCheckerCol(i))

	allChange.append(dateCopy(886));

	for i in range(887,1007):
		allChange.append(createCheckerCol(i))
	
	allChange.append(dateCopy(1007));

	for i in range(1008,1128):
		allChange.append(createCheckerCol(i))

	allChange.append(dateCopy(1128));

	for i in range(1129,1249):
		allChange.append(createCheckerCol(i))

	allChange.append(dateCopy(1249));

	for i in range(1250,1433):
		allChange.append(createCheckerCol(i))

	for i in range(374,400):
		allChange.append(createCheckerCol(i))

	return allChange;



#Returns list of participant rows
def createRows(inList):
	allRows = [];
	with open(nameIn) as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		rowCount = len(list(reader))

	for i in range(0, rowCount):
		newRow = [];
		for x in inList:
			newRow.append(x[i])

		allRows.append(newRow)

	return allRows;

#Creates a csv file and writes the rows to file
def writeToFile(rowList, outName):
	with open(outName, 'w', newline="") as csvfile:
		printer = csv.writer(csvfile)

		for row in rowList:
			printer.writerow(row)

	print("Complete: " + outName)


print("Loading...")
writeToFile(createRows(getAllMADCols()), 'mindmaster_mad_new.csv');

print("Loading...")
writeToFile(createRows(getAllCheckerCols()), 'mindmaster_mad_checker_new.csv');