import csv

# "with Open" wird die Eingabe Datei und die Ausgabedatei geoeffnet,r = nur lesen der Datei ,w = nur schreiben in der Datei
# für python 3 benoetigt open die Anweisung newline=''
with open('danke.csv', 'r',newline='') as csv_in, open('hatman.csv', 'w',newline='') as csv_out:
    # Der reader erhaelt mit 'fieldnames' alle in der csv_in Datei enthaltenen Spalten 
    # delimiter gibt mir das Trennzeichen für die Spalten,da unsere csv Datei schon ";" als Trennzeichen hat, nehmen wir das
    #die csv_out Datei war fehlerhaft deshalb wurde eine txt Datei bei ausführen des Codes im Terminal erstellt
    # und mit dieser wurde dann weiter gearbeitet  
    DataCaptured = csv.reader(csv_in, delimiter=';', skipinitialspace=True) 
    #initialisiere den csv.reader mit der csv_in Datei und delimiter=';', skipinitialspace soll die "\t"überspringen
    hashtags = []
    #erstellen einer leeren Liste
    for row in DataCaptured:
        if row[1] not in hashtags:
            hashtags.append(row[1])
            warum=' '.join(hashtags)
            csv_out.write(warum)
            # so lange in der Liste "hashtags" dieses Element noch nicht vorhanden ist wird es eingefuegt
            #row[1] bezieht sich auf die hashtag Spalte, da Python mit 0 anfaengt zuzaehlen    

print (hashtags)        
