import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def divideRow(line):
    linedata = line.split(';')
    reqdata = [linedata[0],linedata[1],linedata[2],linedata[4]]
    return(reqdata)

x=[]
y=[]

with open('SN_d_hem_V2.0.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        row_data = divideRow(row[0])
        x.append(datetime(int(row_data[0]),int(row_data[1]),int(row_data[2])))
        N = float(row_data[3].strip())
        y.append(N)

area = np.pi*3/10
colors = (0,0,0)

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.title('Daily Hemispherical Sunspot Numbers (1992-2020)')
plt.xlabel('Time')
plt.ylabel('Number of sunspots')
plt.grid()

plt.show()
