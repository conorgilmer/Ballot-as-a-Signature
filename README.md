# Ballot-as-a-Signature
Ballot as a Signature in PR-STV elections
Using the permutaitons in a single transferrable vote to uniquely identify a ballot.


## Permutations (without repetition)
While the number of permutations of the completing a ballot for the all candidates is factorial(n) or
n!
The number of permutations(P) for r preferences cast, for an election with n candidates is

nPr = P(n,r) = n!/(n-r)!    

Calculate number of permutations **[PermutationsCalc.py](/python/PermutationsCalc.py)**  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/conorgilmer/Ballot-as-a-signature/blob/master/notebooks/PermutationsCalc.ipynb)

## Tasks
### Data Gathering and Generation
- plot irish political parites on the Political Compass ([politicalcompass.org](https://politicalcompass.org/ireland2020)), [Political Compas Data](/data/pc.csv)
- **[PoliticalCompassParties.ipynb](/notebooks/PoliticalCompassParties.ipynb)** - plot parties on political compass axes [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/conorgilmer/Ballot-as-a-signature/blob/master/notebooks/PoliticalCompassParties.ipynb)
- **[PlotRegularVoteTransfers.ipynb](/notebooks/PlotRegularVoteTransfers.ipynb)** - plot regular voting pattern (between similar ideologies) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/conorgilmer/Ballot-as-a-signature/blob/master/notebooks/PlotRegularVoteTransfers.ipynb)
- **[PlotIrregularVoteTransfers.ipynb](/notebooks/PlotIrregularVoteTransfers.ipynb)** - plot irregular voting pattern.  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/conorgilmer/Ballot-as-a-signature/blob/master/notebooks/PlotIrregularVoteTransfers.ipynb)

- **[VoteDataAnalysis.ipynb](/notebooks/VoteDataAnalysis.ipynb)** - analyse data from e-voting trial from 2002
  - number of preferences cast
  - mode
  - median
  - mean
  - calculate duplicates (remove duplicates)
  - calculate number of unique votes for each vote sequence
  - caclulate possible permutations for each pref nonPr and % used
  - generate histograms number of votes cast for each preference
  - generate pie breakdown of how many preferences voters cast
  - generate bar chart ratio of votes used to possible votes cast for each preference
  - calculate "votes" euclidean distance and average euclidean distance for each transfer
  - classify as "regular" write to *regular* csv file
- **[GenAll-nPr.py](/python/GenAll-nPr.py)** 
  - generate all permutations nPr (r=7)
- **[GenVoteDataAnalysis.ipynb](/notebooks/GenVoteDataAnalysis.ipynb)** - analyse generated data
  - calculate "votes" euclidean distance and average euclidean distance for each transfer
  - select rows with euclidean distance greater than max of "Regular" votes
  - classify as "Irregular" write to *irregular* csv file
- **[RandGen-nPr.ipynb](/notebooks/RandGen-nPr.ipynb)** 
  - generate random permutations nPr
- **[RandGen-nPr-O.ipynb](/notebooks/RandGen-nPr-O.ipynb)** 
  - generate O, random permutations nPr (n=candidates, r=preferences, O=number of permutations to generate)
  - calculate "votes" euclidean distance and average euclidean distance for each transfer
  - classify as "irregular" write to irregular csv file
- **[RandGen-nPr-range-of-r.ipynb](/notebooks/RandGen-nPr-range-of-r.ipynb)** 
  - generate random permutations for range r values
- **[concatBatch.py](/python/concatBatch.py)**
  - concatenate(merge) *regular* and *irregular* csv files
  - remove duplicates keeping sequence classified as regular
  - writes to merged csv file
- **[DataPrep.ipynb](/notebooks/DataPrep.ipynb)** 
  - format csv file (constituency2002_merged_dist.csv) from actual and generated data with euclidean distance calculated between each vote transfer


### Machine Learning LR, SVM, RF ([MLElectionData](/notebooks/MLElectionData.ipynb))
- split dataset into test and train
- test machine learning algorithms on dataset measure performance
- rebalance dataset/tune model
- evaluate performance
### Machine Learning KNN
- the unsupervised ML model is used K-Nearest Neighbour 
- - **[MLA_KNN_DublinNorth.ipynb](/notebooks/MLA_KNN_DublinNorth.ipynb)** 
- - **[MLA_KNN_DublinWest.ipynb](/notebooks/MLA_KNN_DublinWest.ipynb)** 
- - **[MLA_KNN_Meath.ipynb](/notebooks/MLA_KNN_Meath.ipynb)** 


### Simulated Election using Generated data(in the future)
- Run STV with generated data showing synthetic data alters election. Modify **[rcv.py](/python/rcv.py)** to use a fixed droop quota like in Irish Elections, to simulate election.

## Data Used from e-voting trial from 2002
- [Meath2002.csv](/data/Meath2002.csv)
- [DublinNorth2002.csv](/data/DublinNorth2002.csv)
- [DublinWest2002.csv](/data/DublinWest2002.csv)





# Political Compass
The politcal compass is tool used to position political opinions of an individual or party on a specturm, in this case a two dime
sional spectrum, with a left-right x-axis and authoritarian-libertarian y-axis, although other metrics could be used.
## Data for Irish parties on the Political Compass [pc.csv](/data/pc.csv)
Data from 2002, when eVoting trial was conducted.
| Parties as of 2002  |Initials| X    | Y     |
|:-------|:-----:|-----:|------:|
|Socialist Party | SP    | -7   | -2.5  |
|Sinn Fein | SF    | -4.5 | 1     |
|Green Party| GP    | -1   | -2    |
|Non-Party/Independent | NP    | 0    | 0     |
|Labour | LB    | 1.5  | -0.5  |
|Fianna Fail | FF    | 2.5  | 2.4   |
|Fine Gael | FG    | 3.5  | 2.5   |
|Progressive Democrats | PD    | 4    | 3     |

### Plot of Irish Political Compass.
![Irish parties on the political compass](/images/PCplot.png)


### Plot of transfers of a regular and irregular vote
Regular Vote Transfer Plot | Irregular Vote Transfer Plot.
:-------------------------:|:-------------------------:
![Plot of transfers of a regular vote](/images/RegularVoteTransferplot.png) | ![Plot of transfers of a irregular vote](/images/IrregularVoteTransfersplot.png)
