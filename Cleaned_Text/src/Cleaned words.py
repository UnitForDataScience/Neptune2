
# coding: utf-8

# In[ ]:

#importing libraries
import nltk
import re
import ast 
#getting the file paths from thirdstage cleaning
directory="C:\R4\*.txt"
files=glob.glob(directory)
#getting the names of the nuclearpower plant from filenames
filenames=[]
for name in files:
    name=re.sub(r"\w\:\\\w+\\([^\s]+)\.\w+",r"\1",name)
    filenames.append(name)
#getting the data into rows list
rows=[]
for file in files:
    with open(file,"r")as f:
            #converting string list into list object and appending it to list "rows"
            listed=ast.literal_eval(f.read())
            rows.append(listed)
#writing each word from list onto a new line 
for i in range(len(rows)):
    #writing onto new file the elements from the rows list
    with open("C:\\R5\\"+str(filenames[i])+".txt","w") as f:
        for word in rows[i]:
            f.write(str(word)+"\n")

