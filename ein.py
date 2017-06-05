#paket zur Bearbeitung von csv Datei
import csv

# "with Open" wird die Eingabe Datei und die Ausgabedatei geoeffnet,r = nur lesen der Datei ,w = nur schreiben in der Datei
# für python 3 benoetigt open die Anweisung newline=''
with open('elecc.csv', 'r',newline='') as csv_in, open('Hashen.csv', 'w',newline='') as csv_out:
    # Der reader erhaelt mit 'fieldnames' alle in der csv_in Datei enthaltenen Spalten 
    # delimiter gibt mir das Trennzeichen für die Spalten,da unsere csv Datei schon ";" als Trennzeichen hat, nehmen wir das
    reader = csv.DictReader(
        csv_in,
        fieldnames =["id","handle","text","is_retweet","original_author","time","retweet_count","favorite_count"],
        delimiter=';'

    )
    # Dem writer uebergeben wir die Spalten(fieldnames) vom reader und die extra Spalte Hashtags 
    # geben auch an welchen dialect wir fuer die csv_out Datei verwenden wollen  
    # und auch hier das Spaltentrennzeichen:";"  
    writer = csv.DictWriter(
        csv_out, 
        fieldnames=reader.fieldnames + ['hashtags'],
        dialect=reader.dialect,
        delimiter=';'
    )
    # write schreibt den alten Header der csv_in Datei in die csv_out Datei
    writer.writeheader()

    # for Schleife fuer jede Zeile in der csv_in Datei,header Zeile ist 
    # header Zeile ist nicht teil davon,wenn wir csv.DictReader benutzen
    for row in reader:
        # Split trennt die Tweets in der Spalte text auf in 'words' mit str.split()
        words = row[ 'text' ].split()


        # Rausfiltern und vereinigen der 'words 'mit  str.startswith()
        row['text'] = ' '.join(
            w for w in words if not w.startswith('#'))

        # Herrausziehn der Hashtagsund entfernen von'#' 
        # dazu wird string slicing benutzt.
        row['hashtags'] = ','.join(
            w[1:] for w in words if w.startswith('#'))

        # writer.writerow schreib dann alle Aenderungenin die csv_out Datei
        writer.writerow(row)




