#editdistance.eval(['spam', 'egg'], ['spam', 'ham'])
#1L

#DBS 3. Projektiteration
#1.Aufgabe Datamining:Clustering
#a)Metrik fuer Aehnlichkeiten von Hashtags
#pip install editdistance
import editdistance
import csv
with open('hashtag.csv', 'rb') as csvfile:
	file=csv.reader(csvfile, delimiter=' ')
	reader = csv.reader(file)
	row_count=sum(1 for row in file) #Zeilenanzahl
	col_2=list(zip(*reader))[1] #alles aus der zweiten Spalte

#for line in file:
#    columns = line.split(' ')
#    if len(columns) >= 2:
#        print columns[1]

#for line in csv:
			#ncol = line.split() # split line into cols
		#ncol=len(next(reader)) # Read first line and count columns
    	


	allhashtags=[] #Erstellen Liste aller Hashtags
	i=0
	while i<row_count: #for row in file:
		#for l in col_2: #2nd col only
		x=col_2[i]
		allhashtags.append(x)	
		i=i+1
		print allhashtags

	editdis=[]	
	j=0
	k=0
	
	for j in range(len(allhashtags)):
		for k in range(j+1, len(allhashtags)): #fuer hashtag an der Stelle k mit allen hashtags
			d=editdistance.eval(allhashtags[j], allhashtags[k])
			editdis.append(d) #alle Editdistanzen fuer je hashtag in Liste einfuegen
		print editdis
	

#Problem Hashtags, die schon verglichen wurden, werden im Laufe nochmal verglichen