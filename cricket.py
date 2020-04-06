import pandas as pd
import numpy as np

def ReadExcel(FileName):
    e_data = pd.read_excel(FileName)
    df = pd.DataFrame(e_data)
    print(df)
    return df

def FindByTeam(em, key):
    Team = em[em.Team == key]
    print(Team)

def MaxOfScore(em):
    em.loc[em['runs scored'].idxmax()]
    
def NoOfBowlers(em):
    NO_B = em[em.Bowling_econ > 0]
    count = len(NO_B['Bowling_econ'])
    print("\nNumber of bowler is: ", count)

def MaxWkts(em):
    c = em['wkts_taken']
    maxW = max(c)
    print("\nMaximum Wickets are Taken: ", maxW)

def SortByStrikeRate(em):
    em = em.sort_values(by=['Strike rate'])
    print(em)

def PlayersWhoTake5W(em):     #players who has taken 5 week
    em = em[em['5w'] > 0]
    print(em)

def TeamMembers(em):        #sorting of players according to team
    grouped = grouped = em.groupby(['Team','IPL 4 Franchise']) ['IPL 4 Franchise'].count()
    print(grouped)

def main():
    data = ReadExcel('cricket.xls')
    MaxOfScore(data)
    NoOfBowlers(data)
    key = input("ENTER TEAM:")
    FindByTeam(data, key)
    x_max = lambda x, y: max(x[y])   #maximum run scored by using lambda function
    print(xMax(data, 'runs scored'))
    x_min = lambda x, y: min(x[y])   #minimum run scored by using lambda function
    print(xMin(data, 'runs scored'))
    MaxWkts(data)
    SortByStrikeRate(data)
    PlayersWhoTake5W(data)    #players who has taken 5 week
    TeamMembers(data)         #sorting of players according to team 

if __name__ == "__main__":
 main()
 main.__doc__
 
