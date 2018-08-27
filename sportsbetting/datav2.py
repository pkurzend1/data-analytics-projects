
import csv

import numpy as np

import pandas as pd

data = "../data/tennis_sample.csv"

X = []

def myInt(sth):
    if isinstance(sth, str):
        if sth == " ":
            return np.nan
        else: 
            try:
                return int(sth)
            except:
                return np.nan


def myFloat(sth):
    if isinstance(sth, str):
        if sth == " ":
            return np.nan
        else: 
            try:
                return float(sth)
            except:
                return np.nan



def parse(s):
    stats = s.split(";")

    
    if len(stats) == 1 and stats[0] == "":
        stats_dict = {
        "aces1" : np.nan,
        "aces2" : np.nan,

        "df1" : np.nan,
        "df2" : np.nan,

        "unforced_errors1" :np.nan,
        "unforced_errors2" : np.nan,

        "1st_serve1" : np.nan,
        "1st_serve2" : np.nan,

        "win_on_1st_serve1" : np.nan,
        "win_on_1st_serve2" : np.nan,

        "win_on_2nd_serve1" : np.nan,
        "win_on_2nd_serve2" : np.nan,   

        "receiving_points_won1" : np.nan,
        "receiving_points_won2" : np.nan,

        "winners1" : np.nan,
        "winners2" : np.nan,

        "bp_conversions1" : np.nan,
        "bp_conversions2" : np.nan,

        "na1" : np.nan,
        "na2" : np.nan,

        "tpw1" : np.nan,
        "tpw2" : np.nan,

        "fastest_serve1" : np.nan,
        "fastest_serve2" : np.nan,

        "avg_1st_serve_speed1" : np.nan,
        "avg_1st_serve_speed2" : np.nan,

        "avg_2nd_serve_speed1" : np.nan,
        "avg_2nd_serve_speed2" : np.nan,

        "time" : np.nan,

    }

    else:
        stats_dict = {
            "aces1" : myInt(stats[0].split(":")[1]),
            "aces2" : myInt(stats[0].split(":")[2]),

            "df1" : myInt(stats[1].split(":")[1]),
            "df2" : myInt(stats[1].split(":")[2]),

            "unforced_errors1" : myInt(stats[2].split(":")[1]),
            "unforced_errors2" : myInt(stats[2].split(":")[2]),

            "1st_serve1" :     str(stats[3].split(":")[1]).strip()[:-1].split("[")[0],
            "1st_serve1_max" : str(stats[3].split(":")[1]).strip()[:-1].split("[")[1],
            "1st_serve2" :     str(stats[3].split(":")[2]).strip()[:-1].split("[")[0],
            "1st_serve2_max" : str(stats[3].split(":")[2]).strip()[:-1].split("[")[1],

            "win_on_1st_serve1" : str(stats[4].split(":")[1]).strip()[:-1].split("[")[0],
            "win_on_1st_serve1_max" : str(stats[4].split(":")[1]).strip()[:-1].split("[")[1],
            "win_on_1st_serve2" : str(stats[4].split(":")[2]).strip()[:-1].split("[")[0],
            "win_on_1st_serve2_max" : str(stats[4].split(":")[2]).strip()[:-1].split("[")[1],

            "win_on_2nd_serve1" :     str(stats[5].split(":")[1]).strip()[:-1].split("[")[0],
            "win_on_2nd_serve1_max" : str(stats[5].split(":")[1]).strip()[:-1].split("[")[1],
            "win_on_2nd_serve2" :     str(stats[5].split(":")[2]).strip()[:-1].split("[")[0],    
            "win_on_2nd_serve2_max" : str(stats[5].split(":")[2]).strip()[:-1].split("[")[1],    

            "receiving_points_won1" :     str(stats[6].split(":")[1]).strip()[:-1].split("[")[0],
            "receiving_points_won1_max" : str(stats[6].split(":")[1]).strip()[:-1].split("[")[1],
            "receiving_points_won2" :     str(stats[6].split(":")[2]).strip()[:-1].split("[")[0],
            "receiving_points_won2_max" : str(stats[6].split(":")[2]).strip()[:-1].split("[")[1],
            
            
            "winners1" : myInt(stats[7].split(":")[1]),
            "winners2" : myInt(stats[7].split(":")[2]), 

            "bp_conversions1" : myInt(stats[8].split(":")[1]),
            "bp_conversions2" : myInt(stats[8].split(":")[2]), 
            
            "na1" :     str(stats[9].split(":")[1]).strip()[:-1].split("[")[0],
            "na1_max" : str(stats[9].split(":")[1]).strip()[:-1].split("[")[1],
            "na2" :     str(stats[9].split(":")[2]).strip()[:-1].split("[")[0],
            "na2_max" : str(stats[9].split(":")[2]).strip()[:-1].split("[")[1],
            
            "tpw1" : myInt(stats[10].split(":")[1]),
            "tpw2" : myInt(stats[10].split(":")[2]), 

            "fastest_serve1" : str(stats[11].split(":")[1]),
            "fastest_serve2" : str(stats[11].split(":")[2]), 

            "avg_1st_serve_speed1" : str(stats[12].split(":")[1]),
            "avg_1st_serve_speed2" : str(stats[12].split(":")[2]), 

            "avg_2nd_serve_speed1" : str(stats[13].split(":")[1]),
            "avg_2nd_serve_speed2" : str(stats[13].split(":")[2]), 

            "time" : str(":".join(stats[14].strip().split(":")[1:]))

        }
 
    return stats_dict






with open(data) as f:

    reader = csv.reader(f)
    for row in reader:
#        print(len(row))
        if "K1" in row:
            continue
        row_dict = {
            "player1" : str(row[0]),
            "player2" : str(row[1]),
            "tournament" : str(row[2]),
            "data" : str(row[3]),
            "round" : str(row[4]),
            "surface" : str(row[5]),
            "result" : str(row[6]),
            "k1" : myFloat(row[7]),
            "k2" : myFloat(row[8]),
            "sets" : str(row[9]),
            "hcp" : str(row[10]),
            "total" : str(row[11]),            
        }


        container = row[-1] # all stats as string
        stats_dict = parse(container)
        row_dict = {**row_dict, **stats_dict}

#        print(row_dict)
        X.append(row_dict)

df = pd.DataFrame(X, columns = X[0].keys(), dtype=object)

df.to_csv("../data/clean/data.csv")





        
















