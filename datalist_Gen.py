import pandas as pd 
import csv

with open('mil_items.csv', 'rt')as f:
        with open('mil_items.txt', 'w+') as f2:
            for line in f:
                f2.write(f"<option value =\"{line.rstrip()}\"> \n")
                        
f2.close()
