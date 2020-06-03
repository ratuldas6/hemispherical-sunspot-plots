import csv
import matplotlib.pyplot as plt
import numpy as np

def divideRow(line): #extracts data from each cell in the .csv file
    linedata = line.split(';')
    reqdata = [linedata[3],linedata[4]]
    return(reqdata)

x=[] #for time
y=[] #for sunspot numbers

with open('SN_d_hem_V2.0.csv', newline='') as File: 
    reader = csv.reader(File)
    for row in reader:
        row_data = divideRow(row[0])
        x.append(row_data[0]) #adds time data to x
        y.append(row_data[1]) #sunspot numbers data to y

plt.plot(x,y, marker='o')

plt.title('Hemispherical Sunspot Numbers (1992-2020)')

plt.xlabel('Time')
plt.ylabel('Number of sunspots')

plt.show()