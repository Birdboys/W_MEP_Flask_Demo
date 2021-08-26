import csv
import pandas
import ast
from itertools import chain, combinations
import ast 
import pandas 
def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


rules = pandas.read_csv("mil_rules.csv", header=0)
thingy = set(["1 PVC COND COUPLING"])
thingy2 = set(["big fucking chungus"])
thingy3 = set(['what the fuck please'])
thingies = list(powerset(["1 PVC COND COUPLING", "big fucking chungus", "peepee"]))
thingies = list(map(set, thingies))
print(thingies, '\n')

print(type(thingies[6]))
"""
for index, row in rules.head().iterrows():
        print(set(ast.literal_eval(row['antecedent']))== thingy)
        if set(ast.literal_eval(row['antecedent']),) in thingies:
                print(row['consequent'])"""

        
