
# coding: utf-8

# In[ ]:

#importing the necessary libraries
import nltk
import re
import ast
from nltk.corpus import stopwords
import glob
#getting the file path from the second stage of cleaning
directory="C:\R3\*.txt"
files=glob.glob(directory)
#getting the nuclear power plant names from the files
filenames=[]
for name in files:
    name=re.sub(r"\w\:\\\w+\\([^\s]+)\.\w+",r"\1",name)
    filenames.append(name)
#reading the file and converting the list format in the string into list object
rows=[]
for file in files:
    with open(file,"r")as f:
            listed=ast.literal_eval(f.read())
            rows.append(listed)
#removing the stopwords
def stopwordsremoval(string):
    stop_words=set(stopwords.words("english"))
    featurewords=[]
    for word in string:
        if word in stop_words:
            continue
        else:
            featurewords.append(word)
    return featurewords
#storing the wordlist after stopword removal into list "featuredwordlist"
featuredwordlist=[]
for row in rows:
    featuredwordlist.append(stopwordsremoval(row))
#writing wordlist from featuredwordlist onto new files with respective filnames
for i in range(len(filenames)):
    with open("C:\\R4\\"+str(filenames[i])+".txt","w") as f:
        f.write(str(featuredwordlist[i]))

