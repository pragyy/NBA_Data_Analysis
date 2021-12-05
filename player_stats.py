# -*- coding: utf-8 -*-
"""Player_Stats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MLQneDyGsP5b5nTNYZt9izmIGezfgpg0

## Sraping Player Stats
"""

# import required packages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# https://www.basketball-reference.com/leagues/NBA_2020_totals.html

# NBA season we will be analyzing
years = []
for i in range(1985, 2019):
  years.append(i)

columns = ['Player','Pos','Age','Tm','G', 'GS','MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL', 'BLK','TOV','PF','PTS']

final_stats = pd.DataFrame(columns=columns)
data = []
for year in years:
  # URL page we will scraping 
  url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)

  # this is the HTML from the given URL
  html = urlopen(url)
  soup = BeautifulSoup(html)

  # avoid the first header row
  rows = soup.findAll('tr')[1:]
  player_stats = [[td.getText() for td in rows[i].findAll('td')]
              for i in range(len(rows))]
  #print(player_stats)
  #data.append(player_stats)
  #print(str(player_stats[0]))
  stats = pd.DataFrame(player_stats, columns = columns)
  stats['Year'] = year
  #print(stats)
  final_stats = pd.concat([final_stats, stats], ignore_index=True)
  #final_stats = pd.concat(stats, ignore_index=True)

print(final_stats.shape)

final_stats.dropna(subset=['Player'], inplace=True)

final_stats.to_csv (r'player_stats.csv', index = False, header=True)