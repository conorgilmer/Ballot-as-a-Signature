#!/usr/bin/env python
# coding: utf-8

# # Irish Parties on the Political Compass

#Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')


# ### Import in Political compass data

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

#generate markdown for README files
print("\nGenerate markdown Table \n")
print(df.to_markdown())


# ### Plot Political Compass Graph

#draw graph set up 
#set up the paramaters of the graph, axes and background.
xmin, xmax, ymin, ymax = -8, 8, -8, 8
ticks_frequency = 1
fig, ax = plt.subplots(figsize=(7,7), num="Irish Political Parties on the Political Compass") 
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
fig.suptitle('STV Voter plot', fontsize=16)

#add the party initials to the plot
pt=df.party.to_numpy()
for m in range(len(points)):
    n = x[1][m]
    o = y[1][m]
    ptext=pt[m]

    if o >= 0:
        plt.text(n -0.4, o +0.5, ptext, fontsize=10)      
    else:
        plt.text(n -0.4, o -0.9, ptext, fontsize=10) 

#plot all the points
plt.scatter(x,y)
#plt.figure(figsize=(432, 288))
plt.savefig("../images/PCplot.png")
plt.show()




