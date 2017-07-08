
# coding: utf-8

# In[ ]:

#importing libraries
import nltk
import re
import ast
import enchant
import glob
from nltk.tokenize import word_tokenize
from nltk.metrics import edit_distance
#getting the file path from initial round of cleaning
directory="C:\R1\*.txt"
files=glob.glob(directory)
wordlist=[]
for file in files:
    with open(file,"r")as f:
        #converting string list into list object
        listed=ast.literal_eval(f.read())
        #gettting the wordlist and appending it to the list "wordlist"
        wordlist.append(listed)
#getting the powerplant names from the filenames which includes the path
filenames=[]
for name in files:
    name=re.sub(r"\w\:\\\w+\\([^\s]+)\.\w+",r"\1",name)
    filenames.append(name)
#correcting the spelling mistakes by using Enchant library
def correctingword(string):
    correctedwordlist=[]
    corrector=enchant.Dict("en-US")
    for word in string:
        if corrector.check(word):
            correctedwordlist.append(word)    
        else:
            suggestions=corrector.suggest(word)
            if len(suggestions)>0 and len(suggestions[0])>2 and edit_distance(word,suggestions[0])<=2:
                correctedwordlist.append(suggestions[0].lower())
            else:
                continue
    return correctedwordlist
#completelist contains the corrected word list
completelist=[]
for wlist in wordlist:
    completelist.append(correctingword(wlist))
#writing the corrected word list onto a new file with respective filnames for third stage of cleaning
for i in range(len(filenames)):
    with open("C:\\R3\\"+str(filenames[i])+".txt","w") as f:
        f.write(str(completelist[i]))


# In[11]:

import ast
ashish="[1,2,2,2,2,2]"
ashish=ast.literal_eval(ashish)
print (ashish)


# In[ ]:



