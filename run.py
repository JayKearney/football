import pandas as pd
import prettytable as pt

df = pd.read_csv('Top-Football-Leagues-Scorers.csv')

# User input

year = input('Enter a year from 2016 to 2020: ')
year = int(year)

# If value not accepted has been enter - error message and print again - else if

#Output

result = df[df['Year'] == year]
print(result)

#result = df[df['Player Names'] == 'Luis Suarez']
#print(result)

