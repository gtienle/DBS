Aufgabe 1
election=# 
1)
CREATE TABLE Tweets 
(T_ID INT NOT NULL , handel CHAR(20), text CHAR(300),is_retweet CHAR(5) NOT NULL, original_author CHAR(40), time CHAR(20), retweet_count INT, favorit_count INT);
 
ALTER TABLE Tweets 
ADD PRIMARY KEY (T_ID);

2)
CREATE TABLE Hashtag
(H_ID INT, H_Name CHAR(20)
);


ALTER TABLE Hashtag
ADD PRIMARY KEY (H_ID);

3)
CREATE TABLE Has_a
(index INT NOT NULL, T_ID INT, H_ID INT,
FOREIGN KEY (H_ID) REFERENCES Hashtag(H_ID),
FOREIGN KEY (T_ID) REFERENCES Tweets(T_ID)
); 

ALTER TABLE Has_a 
ADD PRIMARY KEY (index, T_ID, H_ID);












