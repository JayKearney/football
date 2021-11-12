import pandas as pd
import prettytable as pt

df = pd.read_csv('Top-Football-Leagues-Scorers.csv')

# User input

year = input('Enter a year from 2016 to 2020: ')
year = int(year)

# If value not accepted has been enter - error message and print again - else if

#Output
table = df[df['Year'] == year]

result = table[['Player Names','Goals','League','Matches_Played','Shots']]

#print(result)

#sort by descending order of goals
result = result.sort_values(
     by="Goals",
     ascending=False
)
print(result.head(20))
