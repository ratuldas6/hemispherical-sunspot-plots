import csv
import matplotlib.pyplot as plt
import numpy as np

with open('SN_d_hem_V2.0.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)

