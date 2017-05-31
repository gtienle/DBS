import xlrd
import pandas as pd
import csv
 
data = open("/home/celvic/DBS/Projekte/american-election-tweets.csv",'r') #wir oeffnen unseren Datensatz im leseModus
outFile = open("2.csv","r+") #wir oeffnen unseren verbesserten im schreib Modus
 
 
listLines = [] #wir kreieren eine leere liste in die spaeter die verbesserten daten reinkommen
for line in data:
	
	if line in listLines:
		continue
	else:
		outFile.write(line)
		listLines.append(line)
print len(listLines)
 
for line in outFile:
	
	if line == "": #wenn es sich um einen leeren string haelt weiter, wenn nicht kommt es in unseren datensatz
		continue
	else:
		outFile.write(line)
		
 
outFile.close()
data.close()