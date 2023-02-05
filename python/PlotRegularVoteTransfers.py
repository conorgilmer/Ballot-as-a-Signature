#!/usr/bin/env python
# coding: utf-8

# # Plot Vote Transfers on the Political Compass

# In[1]:


#draw a graph of the political compass, tracking a PR-STV vote
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#set up the paramaters of the graph, axes and background.
xmin, xmax, ymin, ymax = -8, 8, -8, 8
ticks_frequency = 1
fig, ax = plt.subplots(figsize=(7,7), num="PR-STV Vote Traced") 
fig.patch.set_facecolor('#ffffff')
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('$Left/Right$', size=14, labelpad=-24, x=1.04, y=1)
ax.set_ylabel('$Authoritarian/Libertarian$', size=14, labelpad=-21, y=1.02, rotation=0)
 
plt.text(0.49, 0.49, r"$O$", ha='right', va='top',
    transform=ax.transAxes,
         horizontalalignment='center', fontsize=14)

x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# Add title
#fig.canvas.set_window_title('PR-STV Vote') #set above
fig.suptitle('STV Regular Vote Transfer plot', fontsize=16)

#download compass data positioning irish political parties on the political spectrum
indata='../data/pc.csv'

#set column names
col_names = ['party', 'xaxis', 'yaxis']
#read in data
df = pd.read_csv(indata, na_values=["Missing"], names=col_names)
print(df)
points=[]
points = df.party
x=[] #x-axis coordinates
y=[] #y-axis coordinates
pt=[]

#populate two lists with the x and y - coordinates
for p in points:
    pt.append(df.party)
    x.append(df.xaxis)
    y.append(df.yaxis)

#Irregular Vote
#dVote= ['NP', 'SP', 'LB', 'SF', 'FF', 'GP', 'FG']
#Regular Vote
dVote =['FG','FF','LB', 'GP', 'SF']

#populate 3 lists with text, x co-ord and y co-ord
dfi = df.party.tolist()
print("dfi",dfi)
xi=[]
yi=[]
pp=[]
for d in dVote:
    inx=dfi.index(d)
    pp.append(df.iloc[inx].tolist()[0])
    xi.append(df.iloc[inx].tolist()[1])
    yi.append(df.iloc[inx].tolist()[2])
#print(df.iloc[inx].tolist()[2])
for ip in range(len(pp)):
    print(f"{ip+1} - {pp[ip]} ({xi[ip]}, {yi[ip]})")


#plt.plot((-6.0,-3.5,1,-1.2,1.5,1.5),(-3.5, 1.5,0.2,-1,-1.5,1.5), 'ro-')
#plt.plot(df.xaxis.to_numpy(),df.yaxis.to_numpy(), 'ro-')
plt.plot(xi,yi, color='green', linewidth=2, linestyle='solid')

#Calculate the eculidean distance a vote travels on the political spectrum
dist = 0
total_dist=0
for pl in range(len(pp)):
# initializing points in
# numpy arrays      
    if pl != (len(pp)-1):
        point1 = np.array((xi[pl],yi[pl]))
        point2 = np.array((xi[pl+1],yi[pl+1]))

#calculating Euclidean distance
# using linalg.norm()
        dist = np.linalg.norm(point1 - point2)
        print(f"Euclidean distance between vote {pl+1} and {pl+2} is {dist}")
        total_dist = total_dist + dist
        
avg_dist = total_dist/(len(pp)-1)    
print("Total Distance Travelled on Political Compass as a vote transfers ", total_dist)
print("Average Distance Travelled on Political Compass of each vote transfers ", avg_dist)


#print the vote number above/below the point on the plot
pt=df.party.to_numpy()
for m in range(len(pp)):
    n = xi[m]
    o = yi[m]
    ptext=pp[m]
    vno = "("+str(m+1)+")"

    if o >= 0:
        plt.text(n -0.4, o +0.5, ptext, fontsize=10)
        plt.text(n -0.4, o +1.0, vno, fontsize=10)      

    else:
        plt.text(n -0.4, o -0.9, ptext, fontsize=10)
        plt.text(n -0.4, o -1.4, vno, fontsize=10)      

#plot all the points
plt.scatter(xi,yi)


# Save the political compass plot
plt.savefig('../images/RegularVoteTransferplot.png')

#show political compass
plt.show()


# In[ ]:




