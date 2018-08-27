
import csv

import numpy as np

data = "../data/sportsbetting/tennis_sample.csv"
parsed_data = "../data/sportsbetting/parsed_data.csv"

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
    stats = s.split(",")
    

    
    if len(stats) == 1 and stats[0] == "":
        stats_dict = {

        # own stats 
        "firstIn1" : np.nan,
        "firstIn2" : np.nan,
        
        "servedPoints1" : np.nan,
        "servedPoints2" : np.nan,

        "firstWon1" : np.nan,
        "firstWon2" : np.nan,

        "secondWon1" : np.nan,
        "secondWon2" : np.nan,

        "naTot1" : np.nan,
        "naTot2" : np.nan,


        # stats on csv
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
        print(stats)
        FirstIn1 = myInt(str(stats[3].split(":")[1]).strip().split("[")[0])                     # from 1st_serve
        servedPoints1 = myInt(str(stats[3].split(":")[1]).strip().split("[")[1].strip("]"))     # from 1st_serve

        FirstIn2 = myInt(str(stats[3].split(":")[2]).strip().split("[")[0])                     # from 1st_serve
        servedPoints2 = myInt(str(stats[3].split(":")[2]).strip().split("[")[1].strip("]"))     # from 1st_serve

        __1st_serve1  = myDiv(FirstIn1, servedPoints1)
        __1st_serve2  = myDiv(FirstIn2, servedPoints2)

        
        FirstWon1 = myInt(str(stats[4].split(":")[1]).strip().split("[")[0])                    # from win_on_1st_serve
        FirstWon2 = myInt(str(stats[4].split(":")[2]).strip().split("[")[0])                    # from win_on_1st_serve

        __win_on_1st_serve1 = myDiv(FirstWon1, FirstIn1)
        __win_on_1st_serve2 = myDiv(FirstWon2, FirstIn2)

        SecondWon1 = myInt(str(stats[5].split(":")[1]).strip().split("[")[0])                   # from win_on_2nd_serve
        SecondWon2 = myInt(str(stats[5].split(":")[2]).strip().split("[")[0])                   # from win_on_2nd_serve

        __win_on_2nd_serve1 = myDiv(SecondWon1, (servedPoints1 - FirstIn1))
        __win_on_2nd_serve2 = myDiv(SecondWon2, (servedPoints2 - FirstIn2))

        __receiving_points_won1 = myDiv(servedPoints2 - FirstWon2 + SecondWon2, servedPoints2)
        __receiving_points_won2 = myDiv(servedPoints1 - FirstWon1 + SecondWon1, servedPoints1)

        naWon1 = myInt(str(stats[9].split(":")[1]).strip().split("[")[0]) # net approaches won
        naWon2 = myInt(str(stats[9].split(":")[2]).strip().split("[")[0])

        naTot1 = myInt(str(stats[9].split(":")[1]).strip().split("[")[1].strip("]")) # net approaches of that player
        naTot2 = myInt(str(stats[9].split(":")[2]).strip().split("[")[1].strip("]"))

        __na1 = myDiv(naWon1, naTot1)
        __na2 = myDiv(naWon2, naTot2)
        stats_dict = {
            # own stats 
            "firstIn1" : FirstIn1,
            "firstIn2" : FirstIn2,
            
            "servedPoints1" : servedPoints1,
            "servedPoints2" : servedPoints2,

            "firstWon1" : FirstWon1,
            "firstWon2" : FirstWon2,

            "secondWon1" : SecondWon1,
            "secondWon2" : SecondWon2,

            "naTot1" : naTot1,
            "naTot2" : naTot2,

            # stats on csv
            "aces1" : myInt(stats[0].split(":")[1]),
            "aces2" : myInt(stats[0].split(":")[2]),

            "df1" : myInt(stats[1].split(":")[1]),
            "df2" : myInt(stats[1].split(":")[2]),

            "unforced_errors1" : myInt(stats[2].split(":")[1]),
            "unforced_errors2" : myInt(stats[2].split(":")[2]),

            "1st_serve1" : __1st_serve1, #  37[71] : firstIn / served points
            "1st_serve2" : __1st_serve2, 

            "win_on_1st_serve1" : __win_on_1st_serve1, #  24[37] : First Won / FirstIn
            "win_on_1st_serve2" : __win_on_1st_serve2, 

            "win_on_2nd_serve1" : __win_on_2nd_serve1, #  17[34]  : Second Won / (served points - FirstIn)
            "win_on_2nd_serve2" : __win_on_2nd_serve2,       

            "receiving_points_won1" : __receiving_points_won1, # 30[71] : (Served points p2 - (First Won p2 + Second Won p2)) / served points p2
            "receiving_points_won2" : __receiving_points_won2,  

            "winners1" : myInt(stats[7].split(":")[1]), # Winners are points won by any player ?
            "winners2" : myInt(stats[7].split(":")[2]), 

            "bp_conversions1" : myDiv(myInt(str(stats[8].split(":")[1]).strip().split("[")[0]), myInt(str(stats[8].split(":")[1]).strip().split("[")[1].strip("]"))),  #  8[17] : number of break points won by the receiver / total number of break points played
            "bp_conversions2" : myDiv(myInt(str(stats[8].split(":")[2]).strip().split("[")[0]), myInt(str(stats[8].split(":")[2]).strip().split("[")[1].strip("]"))),  #         eg: break points saved = number of break points won by the server / total number of break points played

            "na1" : __na1, # 23[31]   net approaches won / number of net approaches of that player
            "na2" : __na2, 

            "tpw1" : myInt(stats[10].split(":")[1]),
            "tpw2" : myInt(stats[10].split(":")[2]), 

            "fastest_serve1" : str(stats[11].split(":")[1]).strip(),
            "fastest_serve2" : str(stats[11].split(":")[2]).strip(), 

            "avg_1st_serve_speed1" : str(stats[12].split(":")[1]).strip(),
            "avg_1st_serve_speed2" : str(stats[12].split(":")[2]).strip(), 

            "avg_2nd_serve_speed1" : str(stats[13].split(":")[1]).strip(),
            "avg_2nd_serve_speed2" : str(stats[13].split(":")[2]).strip(), 

            "time" : str(".".join(stats[14].strip().split(":")[1:])).strip()

        }

    return stats_dict





def dictsToCSV(dicts2csv, filepath=parsed_data): 
    keys = dicts2csv[0].keys()
    with open(filepath, 'w') as f:  
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dicts2csv)




with open(data) as f:

    reader = csv.reader(f)
    for row in reader:
        
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

dictsToCSV(X)





        
















