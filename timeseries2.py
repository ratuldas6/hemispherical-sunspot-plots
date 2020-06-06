import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('SN_m_hem_50-94.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

sunspot_date = data['Date']
sunspot_TSN = data['TSN']

plt.plot_date(sunspot_date, sunspot_TSN, markersize = 3, c=(0,0,0))

plt.gcf().autofmt_xdate()

plt.title('Monthly Hemispherical Sunspot Numbers (1950-1994)')
plt.xlabel('Time')
plt.ylabel('Sunspot Number')
  
plt.show()
