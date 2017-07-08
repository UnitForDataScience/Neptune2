
# coding: utf-8

# In[ ]:

#importing libaries
import nltk
import glob
import codecs
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#getting the path to each file for a nuclear power plant
new_corpus=r"C:\AN\*.txt"
files=glob.glob(new_corpus)
#reading the entire file and storing it in the stringlist
stringlist=[]
for file in files:
      with codecs.open(file, "r",encoding='utf-8', errors='ignore') as f:
        stringlist.append(f.read())  
#getting the names of each nuclear power plant
filenames=[]
for name in files:
    name=re.sub(r"\w\:\\\w+\\([^\s]+)\.\w+",r"\1",name)
    filenames.append(name)
#cleaning the strings from the stringlist
def stringcleaning(term):
    #Converting into lowercase
    term=term.lower()
    #Removing the white spaces
    term=re.sub(r"[\s]+"," ",term)
    #removing the common sentences
    term=term.replace("power light company","")
    term=term.replace("nuclear one unit","")
    term=term.replace("licensee event report","")
    term=term.replace("post office box","")
    term=term.replace("rock arkansas","")
    term=term.replace("management program analysis","")
    term=term.replace("south utilities system","")
    term=term.replace("director office inspection enforcement","")
    #Removing the punctuations
    term=re.sub(r"[^a-zA-Z0-9\s]","",term)
    return term
#storing the cleaned strings into list cleanedstringlist
cleanedstringlist=[]
for term in stringlist:
    term=stringcleaning(term)
    cleanedstringlist.append(term)
#word tokenizing and stopwords removal
def stopwordsremoval(cleanedstring):
    stop_words=stopwords.words("english")
    wordlist=word_tokenize(cleanedstring)
    
    cleanedwordlist=[]
    for word in wordlist:
        value=re.search(r"^[a-zA-Z][a-zA-Z0-9]+$",word)#to start with only numbers and not alphabets
        if word in stop_words or len(word)<=2 or value is None:
            continue
        else:
            cleanedwordlist.append(word)
    return cleanedwordlist
#storing the tokenized words for each file into a list
cleanedwordlist=[]
for string in cleanedstringlist:
    cleanedwordlist.append(stopwordsremoval(string))
#writing cleanedwordlist on to a new file with respective nuclear power plant names and storing it in the Folder R1 for second step cleaning process
for i in range(len(filenames)):
    with open("C:\\R1\\"+str(filenames[i])+".txt","w") as f:
        f.write(str(cleanedwordlist[i]))

