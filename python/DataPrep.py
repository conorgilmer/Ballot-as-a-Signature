#!/usr/bin/env python
# coding: utf-8

# # Data Prep

# ### format csv file from actual and generated data with euclidean distance calculated between each vote transfer 

# ## Read in csv vote details file into dataframe

# In[1]:


#read vote data from csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math 
#import seaborn as sns
import scipy as scp
get_ipython().run_line_magic('matplotlib', 'inline')

#input file
#constituency="DublinNorth2002_merged"
constituency="DublinWest2002_merged"
constituency="Meath2002_merged"
in_csv='../data/processed/'+constituency+'.csv'
#in_csv='../data/processed/'+constituency+'toptail.csv'
#in_csv='https://raw.githubusercontent.com/conorgilmer/Ballot-as-a-signature/master/data/processed/'+constituency+'toptail.csv'
#read in data (setting 1st row as header)
df = pd.read_csv(in_csv, na_values=["Missing"], header=[0])

#set column names as first line
print("Print Data Frame (df.head)")
print(df.head(5))
print("Print Column names")
print(df.columns)


# In[2]:


#drop the numbers column (#df=df.drop(['No.'], 1))
df = df.drop(df.columns[[0]], axis=1)  # df.columns is zero-based pd.Index


# In[3]:


#remove the generated columns
df=df.drop(columns=['maxValues','Euclid Dist', 'Avg. Euc. Dist'])
print(df.columns)
#print(df.head(4))


# In[4]:


#store the target column ('Seq') n a list
seqlist=(df['Seq'].tolist())
#print(seqlist)
display(df)
df= df.drop(columns=['Seq'], axis=1)  


# In[5]:


#convert all nan to 0
df=df.fillna(0)


# In[6]:


#store all columnname as a list
listcols=df.columns.tolist()
#print(listcols)
#convert values to a list
listdf= df.values.tolist()
#print(len(listdf))
#print(listdf)
listpref_nums=[]
listpref_parties=[]
for row in range(len(listdf)):
    #nu_lizt = [0.0] * len(listdf[row])
    #nu_plizt = [''] * len(listdf[row])
    nu_plizt=[]
    nu_lizt=[]
    print(listdf[row])
    lizt=listdf[row]

    n=len(lizt)

    for i in range(0,n):
        for j in range(0,n):
            if i == int(lizt[j])-1:
                #nu_lizt[int(lizt[i]-1)] =i+1
                if lizt[j] > 0:
                    #nu_lizt[i]=j+1
                    nu_lizt.append(j+1)
#    print(nu_lizt)
    listpref_nums.append(nu_lizt)
    # store party initials in order of pref vote
    for p in range(len(nu_lizt)):
        if nu_lizt[p] > 0.0:
            nu_plizt.append(listcols[(nu_lizt[p]-1)][:2])
#    print(nu_plizt)
    listpref_parties.append(nu_plizt)    
    


# In[7]:


#len(listpref_parties)
#for ls in range(len(listpref_parties)):
#    print(listpref_parties[ls])


# In[8]:


#display(listpref_parties)
dfpar = pd.DataFrame(listpref_parties)
dfnums = pd.DataFrame(listpref_nums)


# In[9]:


display(dfpar)


# In[10]:


#convert all nan to 0
dfnums=dfnums.fillna(0)
dfnums = dfnums.astype(int)
#display(dfnums)
dfnums.columns += 1
display(dfnums.head(5))


# In[11]:


dfnums['Seq'] = seqlist
display(dfnums)


# In[12]:


#download compass data positioning irish political parties on the political spectrum
#pcData='../data/pc.csv'
pcData='https://raw.githubusercontent.com/conorgilmer/Ballot-as-a-signature/master/data/pc.csv'

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


# In[13]:


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

    pref_dist=[]
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
            pref_dist.append(dist)
 #   print(total_dist, len(pp))
    if len(pp) > 1:
        avg_dist = total_dist/(len(pp)-1)    
    else:
        avg_dist = total_dist
    #print("Total Distance Travelled on Political Compass as a vote transfers ", total_dist)
    #print("Average Distance Travelled on Political Compass of each vote transfers ", avg_dist)

    return(total_dist, avg_dist, pref_dist)


# In[14]:


#save votes a list of the party initials to dataframe and csv file
dfparties = pd.DataFrame(listpref_parties)
#reset column names (transfers) to start at 1
dfparties.columns = pd.RangeIndex(1, len(dfparties.columns)+1) 
#dfparties.columns += 1
#add the target column (Sequence 0=irregular 1= regular) back in
dfparties['Seq'] = seqlist
display(dfparties)
#Save Dataframe to csv file
out_csv='../data/processed/'+constituency+'_parties.csv'
print("Saving  dataframe as ", out_csv)
dfparties.to_csv(out_csv)


# ## Create dataframe of votes with the tranfer euclidean distance travelled

# In[15]:


#create dataframe of votes with the tranfer euclidean distance travelled
list_transdist=[]
for ls in range(len(listpref_parties)):
    #print(listpref_parties[ls])
    (tD, aD, dist_row) = getEuclidVoteDetails(listpref_parties[ls], dfPC)
    list_transdist.append(dist_row)

dftrans = pd.DataFrame(list_transdist)
#display(dftrans)


# In[16]:


#reset column names (transfers) to start at 1
#dftrans.columns = pd.RangeIndex(1, len(dftrans.columns)+1) 
dftrans.columns += 1

#convert all NaN to 0
dftrans=dftrans.fillna(0)
display(dftrans)


# In[17]:


#add the target column (Sequence 0=irregular 1= regular) back in
dftrans['Seq'] = seqlist
display(dftrans)


# In[18]:


#Save Dataframe to csv file
out_csv='../data/processed/'+constituency+'_dist.csv'
print("Saving  dataframe as ", out_csv)
dftrans.to_csv(out_csv)


# In[19]:


from sklearn.preprocessing import StandardScaler
scaler =StandardScaler()
scaler.fit(dfnums.drop('Seq', axis=1))
scaled_features = scaler.transform(dfnums.drop('Seq', axis=1))


# In[20]:


import seaborn as sns
sns.pairplot(dfnums, hue = 'Seq')


# In[ ]:




