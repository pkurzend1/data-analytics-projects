#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:12:12 2018

@author: Philipp Kurzendorfer, Friedemann Schestag
"""


import csv
import numpy as np
import pandas as pd

data_path = "../sportsbetting/data/raw/raw_sample.csv"
parsed_data_path = "../sportsbetting/data/clean/clean_sample.csv"

# Infos:
# http://blog.tennisscoretracker.com/

X = []

def myInt(sth):
    if isinstance(sth, str):
        if sth == " " or sth=="":
            return np.nan
        else: 
            try:
                return int(sth)
            except:
                return np.nan


def myFloat(sth):
    if isinstance(sth, str):
        if sth == " " or sth=="":
            return np.nan
        else: 
            try:
                return float(sth)
            except:
                return np.nan
            
def myDiv(nom, denom):
    if denom == 0:
        if nom == 0:
            return 0
        else:
            return np.nan

    else:
        return nom / denom

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

        "FirstIn1" : np.nan,
        "ServedPoints1" : np.nan,
        "FirstIn2" : np.nan,
        "ServedPoints2" : np.nan,

        "FirstWon1" : np.nan,
        "FirstWon1_max" : np.nan,
        "FirstWon2" : np.nan,
        "FirstWon2_max" : np.nan,

        "SecondWon1" : np.nan,
        "SecondWon1_max" : np.nan,
        "SecondWon2" : np.nan,
        "SecondWon2_max" : np.nan,

        "receiving_points_won1" : np.nan,
        "receiving_points_won1_max" : np.nan,
        "receiving_points_won2" : np.nan,
        "receiving_points_won2_max" : np.nan,

        "winners1" : np.nan,
        "winners2" : np.nan,

        "breakpoint_conversions1" : np.nan,
        "breakpoint_conversions2" : np.nan,

        "net_approach_won1" : np.nan,
        "net_approach_total1" : np.nan,
        "net_approach_won2" : np.nan,
        "net_approach_total2" : np.nan,

        "total_points1" : np.nan,
        "total_points2" : np.nan,

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

            # from 1st_serve
            "FirstIn1" :      str(stats[3].split(":")[1]).strip().split("[")[0],
            "ServedPoints1" : str(stats[3].split(":")[1]).strip().split("[")[1].strip("]"),
            "FirstIn2" :      str(stats[3].split(":")[2]).strip().split("[")[0],
            "ServedPoints2" : str(stats[3].split(":")[2]).strip().split("[")[1].strip("]"),
            
            # from win_on_1st_serve
            "FirstWon1" :             str(stats[4].split(":")[1]).strip().split("[")[0],
            "FirstWon1_max" :         str(stats[4].split(":")[1]).strip().split("[")[1].strip("]"),
            "FirstWon2" :             str(stats[4].split(":")[2]).strip().split("[")[0],
            "FirstWon2_max" :         str(stats[4].split(":")[2]).strip().split("[")[1].strip("]"),
            
            # from win_on_2nd_serve
            "SecondWon1" :     str(stats[5].split(":")[1]).strip().split("[")[0],
            "SecondWon1_max" : str(stats[5].split(":")[1]).strip().split("[")[1].strip("]"),
            "SecondWon2" :     str(stats[5].split(":")[2]).strip().split("[")[0],
            "SecondWon2_max" : str(stats[5].split(":")[2]).strip().split("[")[1].strip("]"),

            "receiving_points_won1" :     str(stats[6].split(":")[1]).strip().split("[")[0],
            "receiving_points_won1_max" : str(stats[6].split(":")[1]).strip().split("[")[1].strip("]"),
            "receiving_points_won2" :     str(stats[6].split(":")[2]).strip().split("[")[0],
            "receiving_points_won2_max" : str(stats[6].split(":")[2]).strip().split("[")[1].strip("]"),
            
            
            "winners1" : myInt(stats[7].split(":")[1]),
            "winners2" : myInt(stats[7].split(":")[2]), 

            "breakpoints_won1" : myInt(str(stats[8].split(":")[1]).strip().split("[")[0]),
            "breakpoints_played1":      myInt(str(stats[8].split(":")[1]).strip().split("[")[1].strip("]")),
            "breakpoints_won2" : myInt(str(stats[8].split(":")[2]).strip().split("[")[0]),
            "breakpoints_played2":      myInt(str(stats[8].split(":")[2]).strip().split("[")[1].strip("]")),
            
            # net approaches won & net approaches of that player
            "net_approach_won1" :     str(stats[9].split(":")[1]).strip().split("[")[0],
            "net_approach_total1" :   str(stats[9].split(":")[1]).strip().split("[")[1].strip("]"),
            "net_approach_won2" :     str(stats[9].split(":")[2]).strip().split("[")[0],
            "net_approach_total2" :   str(stats[9].split(":")[2]).strip().split("[")[1].strip("]"),
            
            "total_points1" : myInt(stats[10].split(":")[1]),
            "total_points2" : myInt(stats[10].split(":")[2]), 

            "fastest_serve1" : str(stats[11].split(":")[1]),
            "fastest_serve2" : str(stats[11].split(":")[2]), 

            "avg_1st_serve_speed1" : str(stats[12].split(":")[1]),
            "avg_1st_serve_speed2" : str(stats[12].split(":")[2]), 

            "avg_2nd_serve_speed1" : str(stats[13].split(":")[1]),
            "avg_2nd_serve_speed2" : str(stats[13].split(":")[2]), 

            "time" : sum(np.array(list(map(int, stats[14].strip().split(":")[1:])))*
                                   np.array([3600, 60, 1])),
        }
 
    return stats_dict


with open(data_path) as f:

    reader = csv.reader(f)
    for row in reader:
#        print("ROW:")
#        print(row)
#        print(len(row))
        if "K1" in row:
            continue
        row_dict = {
            "player1" : str(row[0]).strip(),
            "player2" : str(row[1]).strip(),
            "tournament" : str(row[2]).strip(),
            "data" : str(row[3]).strip(),
            "round" : str(row[4]).strip(),
            "surface" : str(row[5]).strip(),
            "result" : str(row[6]).strip(),
            "k1" : myFloat(row[7]),
            "k2" : myFloat(row[8]),
            "sets" : str(row[9]).strip(),
            "hcp" : str(row[10]).strip(),
            "total" : str(row[11]).strip(),            
        }


        container = row[-1] # all stats as string
        stats_dict = parse(container)
        row_dict = {**row_dict, **stats_dict}

        #print(row_dict)
        X.append(row_dict)

df = pd.DataFrame(X, columns = X[0].keys(), dtype=object)

df.to_csv(parsed_data_path, index=None)





        
















