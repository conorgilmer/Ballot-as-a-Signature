import pandas as pd
from markdownTable import markdownTable

#input files
file = 'pc.csv'
#file = 'stats/Meath2002_statistics.csv'
#file = 'stats/DublinNorth2002_statistics.csv'
#file = 'stats/DublinWest2002_statistics.csv'

#read into data frame
df = pd.read_csv(file)
print(markdownTable(df.to_dict(orient='records')).getMarkdown())


#### STILL HAVE TO REPLACE "+" with "|"
