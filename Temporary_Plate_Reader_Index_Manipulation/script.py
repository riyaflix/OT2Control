import os
import re
import pandas as pd
import json
import numpy as np

plate_reader_index = {
    'A1':'p4[[4]]','A2':'p4[[3]]','A3':'p4[[2]]','A4':'p4[[1]]','A5':'p4[[0]]',
    'A13':'p7[[0]]','A11':'p7[[1]]','A10':'p7[[2]]','A9':'p7[[3]]','A8':'p7[[4]]',
    'A7':'p7[[5]]','A6':'p7[[6]]',
         
    'B1':'p4[[9]]','B2':'p4[[8]]','B3':'p4[[7]]','B4':'p4[[6]]',
    'B5':'p4[[5]]','B6':'p7[[13]]','B7':'p7[[12]]','B8':'p7[[11]]','B9':'p7[[10]]',
    'B10':'p7[[9]]','B11':'p7[[8]]','B12':'p7[[7]]',
         
    'C1':'p4[[14]]','C2':'p4[[13]]','C3':'p4[[12]]','C4':'p4[[11]]',
    'C5':'p4[[10]]','C6':'p7[[20]]','C7':'p7[[19]]','C8':'p7[[18]]','C9':'p7[[17]]',
    'C10':'p7[[16]]','C11':'p7[[15]]','C12':'p7[[14]]',
         
    'D1':'p4[[19]]','D2':'p4[[18]]','D3':'p4[[17]]','D4':'p4[[16]]','D5':'p4[[15]]',
    'D6':'p7[[27]]','D7':'p7[[26]]',"D8":'p7[[25]]','D9':'p7[[24]]','D10':'p7[[23]]',
    'D11':'p7[[22]]','D12':'p7[[21]]',
    
    'E1':'p4[[24]]','E2':'p4[[23]]','E3':'p4[[22]]','E4':'p4[[21]]','E5':'p4[[20]]',
    'E6':'p7[[34]]','E7':'p7[[33]]','E8':'p7[[32]]','E9':'p7[[31]]','E10':'p7[[30]]',
    'E11':'p7[[29]]','E12':'p7[[28]]',
          
    'F1':'p4[[29]]','F2':'p4[[28]]','F3':'p4[[27]]','F4':'p4[[26]]','F5':'p4[[25]]',
    'F6':'p7[[41]]','F7':'p7[[40]]','F8':'p7[[39]]','F9':'p7[[38]]','F10':'p7[[37]]',
    'F11':'p7[[36]]','F12':'p7[[35]]',
        
    'G1':'p4[[34]]','G2':'p4[[33]]','G3':'p4[[32]]','G4':'p4[[31]]','G5':'p4[[30]]',
    'G6':'p7[[48]]','G7':'p7[[47]]','G8':'p7[[46]]','G9':'p7[[45]]','G10':'p7[[44]]',
    'G11':'p7[[43]]','G12':'p7[[42]]',
          
    'H1':'p4[[39]]','H2':'p4[[38]]','H3':'p4[[37]]','H4':'p4[[36]]','H5':'p4[[35]]',
    'H6':'p7[[55]]','H7':'p7[[54]]','H8':'p7[[53]]','H9':'p7[[52]]','H10':'p7[[51]]',
    'H11':'p7[[50]]','H12':'p7[[49]]'
}
X = pd.Series(plate_reader_index).T
deck_pos = X.apply(lambda x: x[:2])
index = X.apply(lambda x: eval(x[2:])[0][0])
deck_pos.name = 'deck_pos'
index.name = 'int_loc'
X = pd.concat((deck_pos, index), axis=1)
with open('../LabwareDefs/plate_reader_4.json') as json_file:
    plate_reader_4_raw_json = json.load(json_file)
    ordered_wells4 = np.array(plate_reader_4_raw_json['ordering']).flatten()
with open('../LabwareDefs/plate_reader_7.json') as json_file:
    plate_reader_7_raw_json = json.load(json_file)
    ordered_wells7 = np.array(plate_reader_7_raw_json['ordering']).flatten()
print(X.columns)
X['loc'] = X.apply(lambda r: ordered_wells4[r['int_loc']] if r['deck_pos']=='p4' else ordered_wells7[r['int_loc']],axis=1)
breakpoint()
print(plate_reader_index)
