
# coding: utf-8

# In[3]:

import time
import requests 
import csv
from bs4 import BeautifulSoup #hfür Datenimport aus html-Datei
from collections import Counter


# In[15]:

file=open('../Desktop/testfile.csv') 
writer = csv.writer(file, delimiter= ';' )
file


# In[19]:

page=requests.get('https://www.heise.de/thema/https') 
pageout=BeautifulSoup(page.text,'html.parser') #erstellt ein soup page object

content = pageout.find_all(class_="keywordliste")


# In[41]:

txt=[]
for c in content:
    c = c.findAll("header") 
for t in c:
    txt.append(t.text)
    writer.writerow(txt) #Ueberschriften sollen in neue csv Datei geschrieben werden 
print (txt)
file.close()
count= Counter(txt)
print(count.most_common(3))


# In[ ]:



