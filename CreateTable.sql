Aufgabe 1
election=# 
1)
CREATE TABLE Tweet 
(T_ID INT NOT NULL, handle CHAR(20), text CHAR(300), is_retweet CHAR(5) NOT NULL, original_author CHAR(40), time CHAR(20), retweet_count INT, favorit_count INT);
 
ALTER TABLE Tweet 
ADD PRIMARY KEY (T_ID);

2)
CREATE TABLE Hashtag
(H_ID INT, H_count INT, H_Name CHAR(20)
);

ALTER TABLE Hashtag
ADD PRIMARY KEY (H_ID);

3)
CREATE TABLE Has_a
(index INT NOT NULL, T_ID INT, H_ID INT,
FOREIGN KEY (H_ID) REFERENCES Hashtag(H_ID),
FOREIGN KEY (T_ID) REFERENCES Tweet(T_ID)
); 

ALTER TABLE Has_a 
ADD PRIMARY KEY (index, T_ID, H_ID);

4)
CREATE TABLE tritt_auf_mit
(T_ID INT, H_ID INT, 
FOREIGN KEY (H_ID) REFERENCES Hashtag(H_ID), 
FOREIGN KEY (T_ID) REFERENCES Tweet(T_ID)
); 





Aufgabe 3)
Daten einfügen:
- Befehl innerhalb der DB starten und Pfad zur Datei mit Daten angeben
\copy Tweet FROM '/home/lenzey/DBS_2017/e9.txt' DELIMITER ';' CSV
\copy Hashtag FROM '/home/lenzey/DBS_2017/projekt/elecNH.csv' DELIMITER ';' CSV
\copy Has_a FROM '/home/lenzey/DBS_2017/projekt/elecNH.csv' DELIMITER ';' CSV
\copy tritt_auf_mit FROM '/home/lenzey/DBS_2017/projekt/elecNH.csv' DELIMITER ';' CSV
