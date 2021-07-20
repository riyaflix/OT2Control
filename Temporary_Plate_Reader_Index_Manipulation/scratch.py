from bidict import bidict
import pandas as pd

d = {"loc": {"A1": "E1", "A2": "D1", "A3": "C1", "A4": "B1", "A5": "A1", "A12": "A1", "A11": "B1", "A10": "C1", "A9": "D1", "A8": "E1", "A7": "F1", "A6": "G1", "B1": "E2", "B2": "D2", "B3": "C2", "B4": "B2", "B5": "A2", "B6": "G2", "B7": "F2", "B8": "E2", "B9": "D2", "B10": "C2", "B11": "B2", "B12": "A2", "C1": "E3", "C2": "D3", "C3": "C3", "C4": "B3", "C5": "A3", "C6": "G3", "C7": "F3", "C8": "E3", "C9": "D3", "C10": "C3", "C11": "B3", "C12": "A3", "D1": "E4", "D2": "D4", "D3": "C4", "D4": "B4", "D5": "A4", "D6": "G4", "D7": "F4", "D8": "E4", "D9": "D4", "D10": "C4", "D11": "B4", "D12": "A4", "E1": "E5", "E2": "D5", "E3": "C5", "E4": "B5", "E5": "A5", "E6": "G5", "E7": "F5", "E8": "E5", "E9": "D5", "E10": "C5", "E11": "B5", "E12": "A5", "F1": "E6", "F2": "D6", "F3": "C6", "F4": "B6", "F5": "A6", "F6": "G6", "F7": "F6", "F8": "E6", "F9": "D6", "F10": "C6", "F11": "B6", "F12": "A6", "G1": "E7", "G2": "D7", "G3": "C7", "G4": "B7", "G5": "A7", "G6": "G7", "G7": "F7", "G8": "E7", "G9": "D7", "G10": "C7", "G11": "B7", "G12": "A7", "H1": "E8", "H2": "D8", "H3": "C8", "H4": "B8", "H5": "A8", "H6": "G8", "H7": "F8", "H8": "E8", "H9": "D8", "H10": "C8", "H11": "B8", "H12": "A8"}, "platereader": {"A1": "p4", "A2": "p4", "A3": "p4", "A4": "p4", "A5": "p4", "A12": "p7", "A11": "p7", "A10": "p7", "A9": "p7", "A8": "p7", "A7": "p7", "A6": "p7", "B1": "p4", "B2": "p4", "B3": "p4", "B4": "p4", "B5": "p4", "B6": "p7", "B7": "p7", "B8": "p7", "B9": "p7", "B10": "p7", "B11": "p7", "B12": "p7", "C1": "p4", "C2": "p4", "C3": "p4", "C4": "p4", "C5": "p4", "C6": "p7", "C7": "p7", "C8": "p7", "C9": "p7", "C10": "p7", "C11": "p7", "C12": "p7", "D1": "p4", "D2": "p4", "D3": "p4", "D4": "p4", "D5": "p4", "D6": "p7", "D7": "p7", "D8": "p7", "D9": "p7", "D10": "p7", "D11": "p7", "D12": "p7", "E1": "p4", "E2": "p4", "E3": "p4", "E4": "p4", "E5": "p4", "E6": "p7", "E7": "p7", "E8": "p7", "E9": "p7", "E10": "p7", "E11": "p7", "E12": "p7", "F1": "p4", "F2": "p4", "F3": "p4", "F4": "p4", "F5": "p4", "F6": "p7", "F7": "p7", "F8": "p7", "F9": "p7", "F10": "p7", "F11": "p7", "F12": "p7", "G1": "p4", "G2": "p4", "G3": "p4", "G4": "p4", "G5": "p4", "G6": "p7", "G7": "p7", "G8": "p7", "G9": "p7", "G10": "p7", "G11": "p7", "G12": "p7", "H1": "p4", "H2": "p4", "H3": "p4", "H4": "p4", "H5": "p4", "H6": "p7", "H7": "p7", "H8": "p7", "H9": "p7", "H10": "p7", "H11": "p7", "H12": "p7"}}
 
df = pd.DataFrame(d)
d = bidict(df.apply(lambda r: (r['loc'], r['platereader']),axis=1).to_dict())


labware_order_dict = {'order':[],'loc':[],'platereader':[]}
for i in range(1,13,1):
    for a in list('ABCDEFGH'):
        loc = a+str(i)
        print("{}: {}".format(loc,d[loc]))
        labware_order_dict['order'].append(loc)
        labware_order_dict['loc'].append(d[loc][0])
        labware_order_dict['platereader'].append(d[loc][1])
labware_order_df = pd.DataFrame(labware_order_dict)
labware_order_df.set_index('order',inplace=True)
labware_order_df['row'] = labware_order_df['loc'].apply(lambda x: x[0])

result4 = []
result7 = []
i = 0
while i < labware_order_df.shape[0]:
    row = labware_order_df.iloc[i]
    iter_alph = curr_alph = row['row']
    accum = []
    while iter_alph == curr_alph:
        accum.append(row['loc'])
        i+=1
        try:
            row = labware_order_df.iloc[i]
        except:
            break
        curr_alph = row['row']
    if row['platereader'] == 'p4':
        result4.append(accum)
    else:
        result7.append(accum)
from pprint import pprint
pprint(result4)
print()
for x in result4:
    for y in x:
        print(y)
pprint(result7)
print(labware_order_df)
for x in result7:
    for y in x:
        print(y)