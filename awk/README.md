# Generate some random permutations
This uses the Knuth shuffle (thank you Don) to randomly shuffle an array.
we pass into the programme the number of possible candidates, how many preferences we want gerenetated and how many votes we want generated, we then send this output to a file which is csv since we are serparating the elements with a comma nd t and a new vote with a new line


awk -v n=12 -v m=7 -v o=10 -f donrand.awk > randvotes.csv

where 
n= the number of possible candidates
m= the number of preferences used
o= the number of votes generated
