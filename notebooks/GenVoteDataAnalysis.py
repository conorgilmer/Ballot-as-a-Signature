#!/usr/bin/env python
# coding: utf-8

# # Vote Data Analysis from 2002 Irish General Election e-voting trial

#read vote data from csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math 

#get_ipython().run_line_magic('matplotlib', 'inline')

#input file
constituency="DublinWest2002_9P7_Allgenerated"
#constituency="DublinNorth2002_12P7_Allgenerated"
#constituency="Meath2002_14P7_Allgenerated"
my_csv='../data/processed/'+constituency+'.csv'

#read in data (setting 1st row as header)
df = pd.read_csv(my_csv, na_values=["Missing"], header=[0])

#set column names as first line

#df.head()
print("Print Data Frame (df.head)")
print(df.head(10))
print("Print Column names")
print(df.columns)

#drop the numbers column (#df=df.drop(['No.'], 1))
df = df.drop(df.columns[[0]], axis=1)  # df.columns is zero-based pd.Index
#reset index to start a 1 and not 0
df.index = df.index + 1


# # Election Dataset Describe and Info

df.info()

df.describe()


# # Statistics on election - candidates and votes

#Stats No. of Candidates(columns) and Votes(rows), all combinations of candidates = candidates!
print("Statistics on Dataframe")
candidates = len(df.columns)
print("No. of Candidates = ", candidates)
votes = len(df.index)
print("No. of Votes = ", votes)
print("No. of all possible Combinations (candidates)! = ", math.factorial(candidates))


# ## Additional Statistics on Actual Vote Data

# In[53]:


import statistics as stats
df.head()
#print(df.describe())
df.max()
# find the maximum values of each row (the highest vote preference cast)
maxValues = df.max(axis = 1)
#print(maxValues)
#mean - average 
print(f"Average(Mean) value = {stats.mean(maxValues)}")
#mode - most frequent occuring value
print(f"Mode(most often number of votes cast = {stats.mode(maxValues)}")
#median - middle value
print(f"Middle value of votes cast = {stats.median(maxValues)}")


# ## Calculate maximum values (number of preferences) for each vote(row)

#add a column of the maximum count of the rows(highest preference vote cast)
df['maxValues'] = df.max(axis = 1)
df.shape

mval=(df['maxValues'].value_counts())
mval.sort_index(ascending=True, inplace=True)
print(mval.values)
print(mval.index)


# # Plot Histogram of the number of transfers a voter casts

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#counts = Counter(word_list)
#labels, values = zip(*counts.items())
# sort your values in descending order
#indSort = np.argsort(values)[::-1]

# rearrange your data
labels=mval.index
values=mval.values
indexes = np.arange(len(labels))
print(labels)
print(values)
print(indexes)

bar_width = 0.35

# Add title and axis names
plt.title(constituency+' - Preference votes cast')
plt.xlabel('Preferences')
plt.ylabel('votes')

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)


# Save the histogram
#plt.savefig('../images/'+constituency+'hist.png')

#show histogram
#plt.show()


# ###Pie Chart of how many preferences a voter uses

# In[57]:


import matplotlib.pyplot as plt
import numpy as np
# Set the figure size - handy for larger output
#from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
# Set up with a higher resolution screen (useful on Mac)
#get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

pieLabels=[]
for lab in indexes:
    pieLabels.append(lab+1)

plt.pie(values, labels = pieLabels)

# Save the Pie
plt.savefig('../images/'+constituency+'_pref_cast_pie.png')

#plt.show()


# In[58]:


nPrList =[]
for i in range(1,candidates+1):
    nPrList.append(int(math.factorial(candidates)/(math.factorial(candidates-i))))
print(nPrList)


# ## Print number of preferences cast, and calculate percentage

# In[59]:


# creating the dataframe from dictionary
d={"Pref": labels, "Votes": values}    
dfpref = pd.DataFrame(d)

#calculate percentage of preferences cast and add to dataframe
votz = dfpref.Votes.sum()  
dfpref['Percentage'] = round(((dfpref['Votes']/votz)*100), 1)


# In[60]:


print(candidates, votz)
print(df.columns)
print(dfpref)


# In[61]:


print(candidates, 7)


# In[62]:


#calculate possible nPr = n!/(n-r)! values for each preference vote
# candidates = n. No. of pref = r
#nPrList =[]
#for i in range(1,candidates+1):
#    nPrList.append(int(math.factorial(candidates)/(math.factorial(candidates-i))))
#add nPr to dataframe    
dfpref['nPr'] = int(math.factorial(candidates)/(math.factorial(candidates-7)))

# printing the dataframe
print(dfpref)


# # Calculate number of duplicated vote sequences

# In[63]:


print((~df.duplicated()).sum())
print(df.duplicated(keep='last').value_counts())


# In[64]:


#drop all dublicate rows keeping last one
df.drop_duplicates(keep='last', inplace=True, subset=df.columns.difference(['maxValues']))


# In[65]:


#print the number of votes, and the number of unique votes
print(f"Number of votes {votes}")
print(f"Number of unique vote patterns (after removing duplicates) {len(df)}")


# In[66]:


# after removal of duplicates
#add a column of the maximum count of the rows(highest preference vote cast)
df['maxValues'] = df.max(axis = 1)

mval=(df['maxValues'].value_counts())
mval.sort_index(ascending=True, inplace=True)
print(dfpref)


# ### calculate unique vote combinations for each preference cast 

# In[67]:


#calculate unique vote combinations for each preference cast 
dfpref['Unique Votes'] = mval.values

dfpref['Percentage Used'] = round(((dfpref['Unique Votes']/dfpref['nPr'])*100), 5)

# printing the dataframe
print(dfpref)


# In[68]:


#just checking 
print(sum(mval.values))
nPr=dfpref['nPr']


# ## Import in Political Compass data for Irish Parties

# In[69]:


#download compass data positioning irish political parties on the political spectrum
pcData='../data/pc.csv'

#set column names
col_names = ['party', 'xaxis', 'yaxis']
#read in political compass data
dfPC = pd.read_csv(pcData, na_values=["Missing"], names=col_names)
print("Irish Parties on Political Compass")
print(dfPC)
points=[]
points = dfPC.party
x=[] #x-axis coordinates
y=[] #y-axis coordinates
pt=[]

#populate two lists with the x and y - coordinates
for p in points:
    pt.append(dfPC.party)
    x.append(dfPC.xaxis)
    y.append(dfPC.yaxis)


# In[70]:


# get the party initials (1 characters) from the column names i.e. remove .1 .2 L Retc
#print(df.columns)
partiesList= list(df.columns)
del partiesList[-1]
print(partiesList)
partiesList2=[]
for pl in partiesList:
    #print(pl[:2] )
    partiesList2.append(pl[:2])
print(partiesList2)


# In[71]:


def getEuclidVoteDetails(voteRow, dfPC):
    #populate 3 lists with text, x co-ord and y co-ord
    partyPCList = dfPC.party.tolist()
   # print("partyList",partyPCList)
    xi=[]
    yi=[]
    pp=[]
    for d in voteRow:
        inx=partyPCList.index(d)
        pp.append(dfPC.iloc[inx].tolist()[0])
        xi.append(dfPC.iloc[inx].tolist()[1])
        yi.append(dfPC.iloc[inx].tolist()[2])

   # for ip in range(len(pp)):
   #     print(f"{ip+1} - {pp[ip]} ({xi[ip]}, {yi[ip]})")

    #Calculate the eculidean distance a vote travels on the political spectrum
    dist = 0
    total_dist=0
    for pl in range(len(pp)):
    # initializing points in # numpy arrays      
        if pl != (len(pp)-1):
            point1 = np.array((xi[pl],yi[pl]))
            point2 = np.array((xi[pl+1],yi[pl+1]))

    #calculating Euclidean distance # using linalg.norm()
            dist = np.linalg.norm(point1 - point2)
            #print(f"Euclidean distance between vote {pl+1} and {pl+2} is {dist}")
            total_dist = total_dist + dist
 #   print(total_dist, len(pp))
    if len(pp) > 1:
        avg_dist = total_dist/(len(pp)-1)    
    else:
        avg_dist = total_dist
    #print("Total Distance Travelled on Political Compass as a vote transfers ", total_dist)
    #print("Average Distance Travelled on Political Compass of each vote transfers ", avg_dist)

    return(total_dist, avg_dist)

def getVotesParty(voterow, partieslegend):
    #convert a vote row into parties initials
    voteP=[]
    for v in range(len(voterow)):
        for w in range(len(voterow)):
            if voterow[w] == v+1:
                voteP.append(partieslegend[w])
    return(voteP)

#calculate the euclidean distance for all rows
EuclidDist = []
AvgEucDist =[]
for dft5 in range(len(df)):
    #print(dft5)
    dftR = list(df.iloc[dft5])
    del dftR[-1]
    #print("Call get Votes for Party in row")
    votePList=getVotesParty(dftR, partiesList2)
    #print(votePList)
    (tD, aD) = getEuclidVoteDetails(votePList, dfPC)
    #print(tD, aD)
    EuclidDist.append(tD)
    AvgEucDist.append(aD)
    
#print(EuclidDist)
#print(AvgEucDist)
#print(type(EuclidDist))
df['Euclid Dist'] = np.array(EuclidDist)
df['Avg. Euc. Dist'] = np.array(AvgEucDist)
print(df.tail(10))

# Import the libraries
import matplotlib.pyplot as plt
import seaborn as sns

# matplotlib histogram
dfmh = pd.DataFrame()
dfmh = df.loc[df['maxValues']==5.0]

plt.hist(dfmh['Euclid Dist'], color = 'blue', edgecolor = 'black',
         bins = int(180/5))

dfh= pd.DataFrame()
dfh['maxValues'] = df['maxValues']
dfh['Euclid Dist'] = df['Euclid Dist']
dfh['Avg. Euc. Dist'] = df['Avg. Euc. Dist']

# Plot Histogram
#sns.histplot(data = dfh, x = dfh['Euclid Dist'], kde = True, hue = dfh['maxValues'])


# seaborn histogram
#sns.distplot(df['Euclid Dist'], hist=True, kde=False, 
#             bins=int(180/5), color = 'blue',
#             hist_kws={'edgecolor':'black'})

#sns.histplot(data = df['Euclid Dist'])



# Add labels
plt.title('Histogram of Votes v Euclid Dist')
plt.ylabel('Votes')
plt.xlabel('Euclid Distance')


# calculate the avg, mean median min and max of the euclidean distance for each preference 
dfeucmean =  df.groupby('maxValues')['Euclid Dist'].mean()
dfeucmedian =  df.groupby('maxValues')['Euclid Dist'].median()
#dfeucmode =  df.groupby('maxValues')['Euclid Dist'].mode() # no mode

dfeucmin =  df.groupby('maxValues')['Euclid Dist'].min()
dfeucmax =  df.groupby('maxValues')['Euclid Dist'].max()

#convert list to numpy array since lists seem to add at row 1 not 0
dfpref['Euc Mean'] = np.array(dfeucmean)
dfpref['Euc Median'] = np.array(dfeucmedian)
dfpref['Euc Min']  = np.array(dfeucmin)
dfpref['Euc Max']  = np.array(dfeucmax)


# ## Display the Statistics Table of the Vote

# printing the dataframe
print(dfpref)


# ### Write Statistics table to csv file


#filename and dir
out_csv='../data/stats/'+constituency+'_statistics.csv'

#write to csv file
dfpref.to_csv(out_csv)


# ### write out the dataframe with generated fields, categorise sequence as regular (1)

#add column with 
df['Seq']=0

#filename and dir
out_csv='../data/processed/'+constituency+'_gen_irreg1.csv'
print(df.head(10))

#write to csv file
#print("write to ", out_csv)
#df.to_csv(out_csv)


# ### Bar Plot of the Percentages of Preferenes Cast v Possible Preferences


# Set the figure size - handy for larger output
plt.rcParams["figure.figsize"] = [10, 6]
# Set up with a higher resolution screen (useful on Mac)
#get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

#create data frame for bar chart
plotdata = pd.DataFrame([], 
    index=pieLabels
)
plotdata['Cast']=list(dfpref['Unique Votes'])
plotdata['nPr']=list(dfpref['nPr'])


stacked_data = plotdata.apply(lambda x: x*100/sum(x), axis=1)
stacked_data.plot(kind="bar", stacked=True)
plt.title(constituency + " Votes cast to Possible Votes, Candidates(n)=9")
plt.xlabel("Votes Cast (r)")
plt.ylabel("Percentage of votes cast to possible votes (%)")

# Save the bar
plt.savefig('../images/'+constituency+'_pref_percent_bar.png')
plt.show()


print(dfpref['Euc Max'])

#df.loc[(df['Avg. Euc. Dist'] > 5.0) & (df['maxValues']==7.0)]

df.loc[(df['Euclid Dist'] > 46.3) & (df['maxValues']==7.0)]

#write to csv file
print("write to ", out_csv)
df.to_csv(out_csv)






