import pandas as pd
import prettytable as pt
from tabulate import tabulate

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
result = result.head(20)
print(tabulate(result, headers="keys",showindex="never", tablefmt="fancy_grid"))
#print(result.head(20))

league = input('Enter a League name: ')

leagues = df[(df['Year'] == year) & (df['League'] == league)]

leagues = leagues[['League','Player Names','Goals','OnTarget','Shots']]

leagues = leagues.sort_values(
     by="Goals",
     ascending=False
)
leagues = leagues.head(20)
print(tabulate(leagues, headers="keys", showindex="never", tablefmt="fancy_grid"))



