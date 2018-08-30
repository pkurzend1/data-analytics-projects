#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:18:46 2018

@author: Philipp Kurzendorfer, Friedemann Schestag
"""

import pandas as pd

parsed_data_path = '../sportsbetting/data/clean/clean_sample.csv'
feature_path = '../sportsbetting/data/features/feature_sample.csv'

df = pd.read_csv(parsed_data_path)

# comment saying what gets calculated here 
df.loc[:, '__1st_serve1'] = df.loc[:, 'FirstIn1']/df.loc[:, 'ServedPoints1']
df.loc[:, '__1st_serve2'] = df.loc[:, 'FirstIn2']/df.loc[:, 'ServedPoints2']

df.loc[:, '__win_on_1st_serve1'] = df.loc[:, 'FirstWon1']/df.loc[:, 'FirstIn1']
df.loc[:, '__win_on_1st_serve2'] = df.loc[:, 'FirstWon2']/df.loc[:, 'FirstIn2']

df.loc[:, '__win_on_2nd_serve1'] = df.loc[:, 'SecondWon1']/(df.loc[:, 'ServedPoints1'] - df.loc[:, 'FirstIn1'])
df.loc[:, '__win_on_2nd_serve2'] = df.loc[:, 'SecondWon2']/(df.loc[:, 'ServedPoints2'] - df.loc[:, 'FirstIn2'])

df.loc[:, '__receiving_points_won1'] = (df.loc[:, 'ServedPoints2'] - df.loc[:, 'FirstWon2'] + df.loc[:, 'SecondWon2']) / df.loc[:, 'ServedPoints2']
df.loc[:, '__receiving_points_won2'] = (df.loc[:, 'ServedPoints1'] - df.loc[:, 'FirstWon1'] + df.loc[:, 'SecondWon1']) / df.loc[:, 'ServedPoints1']

df.loc[:, '__na1'] = df.loc[:, 'net_approach_won1']/ df.loc[:, 'net_approach_total1']
df.loc[:, '__na2'] = df.loc[:, 'net_approach_won2']/ df.loc[:, 'net_approach_total2']

#  8[17] : number of break points won by the receiver / total number of break points played
df.loc[:, '__breakpoints_converted1'] = df.loc[:, 'breakpoints_won1']/df.loc[:, 'breakpoints_played1']
df.loc[:, '__breakpoints_converted2'] = df.loc[:, 'breakpoints_won2']/df.loc[:, 'breakpoints_played2']


df = df.astype('object')
df.to_csv(feature_path, index=None)
