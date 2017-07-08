
# coding: utf-8

# In[10]:

#Importing the libraries
import pandas as pd
import seaborn as sns
import glob
import matplotlib.pyplot as plt
import re
#Getting the file paths
directory="C:\\HeatMaps\\*.xlsx"
files=glob.glob(directory)
#Initializing i to store dataframes in dictionary
i=0
df={}
for file in files:
    df[i]=pd.read_excel(file,sheetname="cs")
    i=i+1
#Getting the filnames using regular expressions
filenames=[]
for name in files:
    name=re.sub(r"\w:\\\w+\\([\w\s-]+)\.\w+",r"\1",name)
    filenames.append(name)
#Converting the datframe index into decades "1980-1989","1990-1999","2000-2009","2010-2016"
for key in df.keys():
    df[key]=df[key].fillna(0)
    df[key]["Years"]=df[key]["Years"].apply(lambda x:int(x/10))
    df[key].index=df[key]["Years"]
    del df[key]["Years"]
    df[key]=df[key].fillna(0)
    df[key]=df[key].groupby(df[key].index).sum()
    df[key].index=["1980-1989","1990-1999","2000-2009","2010-2016"]
#Generating axes to draw heatmaps for all the 62 powerplants
fig, ax= plt.subplots(nrows=7, ncols=9,
                           sharex=True, sharey=True,
                           figsize=(15,10))
fig.subplots_adjust(wspace=0.01,hspace=0.01)
#Flattening the numpy array
ax=ax.ravel()
#Initalizing a=0 to loop through ax which consists of axes
a=0
for key in df.keys():
    sns.heatmap(df[key].T,ax=ax[a],cbar=False,)
    ax[a].set_title(filenames[a],fontweight="light",size=10)
    a=a+1
#Saving the figure in the png format
plt.savefig("C:\\Users\\athotaku\\Desktop\\images\\Decade.png",dpi=1000,bbox_inches='tight', pad_inches=1)


# In[ ]:




# In[ ]:



