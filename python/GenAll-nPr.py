from itertools import permutations
import pandas as pd
import math 
import numpy as np

#function to convert a permutation list into vote
def listToVote(listgen, num):
    voteList=[]
    for j in range(num):
        voteList.append(np.NaN)
    #print(voteList)

    for k in range(len(listgen)):
        voteList[listgen[k]-1] =k+1 
    return(voteList)

# get the columns from the constituency election data  
def getColumns(constituency):
    #read in regular file to get column name
    #input file
    #constituency="DublinNorth2002"
    my_csv='../data/'+constituency+'.csv'
    #read in data (setting 1st row as header)
    dfR = pd.read_csv(my_csv, na_values=["Missing"], header=[0])

    #print(dfR.columns)

    #drop the numbers column (#df=df.drop(['No.'], 1))
    dfR = dfR.drop(dfR.columns[[0]], axis=1)  # df.columns is zero-based pd.Index
    #reset index to start a 1 and not 0
    dfR.index = dfR.index + 1
    print(dfR.columns)
    return(dfR.columns)

# main function
def main():
    (cons,n,r) =("DublinWest2002", 9 , 8)
    #(cons,n,r) =("DublinNorth2002", 12 , 7)
    #(cons,n,r) =("Meath2002", 14 , 7)


    print("Consituency " + cons + " candidates " + str(n) + " preferences cast " + str(r))
    listAllPermutations = list(range(1,n+1))
    allPermutations = list(permutations(listAllPermutations,r))
    print("nPr = ", int(math.factorial(n)/(math.factorial(n-r))))
    #print("All Permutations (candidates)!",len(allPermutations))
    #print("All Permutations (candidates)!",math.factorial(5))


    #convert each of the permutations generated into a vote
    votesGen=[]
    for row in allPermutations:
        #print(row)
        votesGen.append(listToVote(row,n))

    cols = getColumns(cons)
    #print(cols)

    df = pd.DataFrame(votesGen, columns=cols)
    print(df.head)

    #drop the old numbers column
    #df = df.drop(df.columns[[0]], axis=1)  # df.columns is zero-based pd.Index
    #reset index to start a 1 and not 0
    #df.index = df.index + 1

    # write to file
    out_csv = "../../data/processed/"+cons+"_"+str(n)+"P"+str(r)+"_Allgenerated.csv"
    print("Writing ", out_csv)
    df.to_csv(out_csv)

    print("Complete")

# call main
if __name__ == "__main__":
    main()
