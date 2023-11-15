import time
import datetime
from matplotlib import pyplot as plt
from matplotlib import ticker
import csv
import numpy as np
import pandas as pd
import matplotlib.dates as mdates


fig, ax = plt.subplots()

df = pd.read_csv('/Users/qingjie/Library/Mobile Documents/com~apple~CloudDocs/documents/project_apple/macatv/j604/p1/smt_combine/SMT_station_utility.csv')

grouped_1 = df.groupby(["STATION_TYPE", "STATION_NUMBER"], as_index=False).count()
df1 = df.sort_values(by=['STATION_TYPE','STATION_NUMBER','Test Start Time'], ignore_index=True)

# transfer Test_Start_Time column from object to datetime so we could do calculation
TS_start_time_df1 = pd.to_datetime(df1['Test Start Time'], format='%Y/%m/%d %H:%M')
num_TS_start_time_df1 = mdates.date2num(TS_start_time_df1)
# print(df1.columns.get_loc('Test Start Time'))
df1.insert(df1.columns.get_loc('Test Start Time'), "TS_start_time", TS_start_time_df1, True)
df1.insert(df1.columns.get_loc('TS_start_time'), "num_TS_start_time", num_TS_start_time_df1, True)


TS_stop_time_df1 = pd.to_datetime(df1['Test Stop Time'], format='%Y/%m/%d %H:%M')
num_TS_stop_time_df1 = mdates.date2num(TS_stop_time_df1)
df1.insert(df1.columns.get_loc('Test Stop Time'), "TS_stop_time", TS_stop_time_df1, True)
df1.insert(df1.columns.get_loc('TS_stop_time'), "num_TS_stop_time", num_TS_stop_time_df1, True)



# time_delta column is test time duration for each test
time_delta_df1 = TS_stop_time_df1 - TS_start_time_df1
df1.insert(df1.columns.get_loc('Test Stop Time')+1, "time_delta", time_delta_df1, True)

num_time_delta_df1_in_day = time_delta_df1

for index in num_time_delta_df1_in_day.index:
    num_time_delta_df1_in_day.iloc[index] = num_time_delta_df1_in_day.iloc[index].total_seconds()/60/60/24


df1.insert(df1.columns.get_loc('time_delta'), "num_time_delta_in_day", num_time_delta_df1_in_day, True)

# # conver time_delta column dtype from object to float
# df1['time_delta'] = pd.to_numeric(df1['time_delta'])

# df1.loc[:,'time_delta']

# total_test_time_span is the total test time in minutes from first DUT of first day to last DUT of last day
# this will be the x-axis
total_test_time_span = (TS_stop_time_df1.max() - TS_start_time_df1.min()).total_seconds()/60

print('df1 start time min is:', TS_start_time_df1.min())

df1.to_csv('/Users/qingjie/Library/Mobile Documents/com~apple~CloudDocs/documents/project_apple/macatv/j604/p1/smt_combine/SMT_station_utility_df1.csv')


# ============= set y axis below ================

ylabels = [] 

for index in grouped_1.index:
    ylabels.append(grouped_1.loc[index, 'STATION_TYPE'] + "_" + str(grouped_1.loc[index, 'STATION_NUMBER']))
        

# print(ylabels)
# print(len(ylabels))

ylim_bottom = 0
yaxis_unit  = 1
yaxis_step = 3 * yaxis_unit
ylim_top = ylim_bottom + len(ylabels) * yaxis_step + 1 * yaxis_unit

ax.set_ylim(ylim_bottom, ylim_top)

yticks_position = []
for i in range (ylim_bottom + 2 * yaxis_unit, ylim_top, yaxis_step):
    yticks_position.append(i)

ax.set_yticks(yticks_position, labels=ylabels)

# ============= set x axis below ================

# xlim_left = 0
# xlim_right = total_test_time_span

# ax.set_xlim(xlim_left, xlim_right)
# ax.set_xlabel('minutes since first unit')

broken_barh_all_stations = []

# df1


df2 =  df1.loc[(df1['STATION_TYPE'] == 'SMT-COEX1') & (df1['STATION_NUMBER'] == 2)]

# get all broken barh xragens for each station
for index in grouped_1.index:
    df2 = df1.loc[(df1['STATION_TYPE'] == grouped_1.loc[index, 'STATION_TYPE']) & (df1['STATION_NUMBER'] == grouped_1.loc[index, 'STATION_NUMBER'])]
    # initialize one station barh to clear last staion barh data
    broken_barh_one_station = []

    for index_2 in df2.index:
        xrange_xmin = df2.loc[index_2, 'num_TS_start_time']
        xrange_xwidth = df2.loc[index_2, 'num_time_delta_in_day']
        broken_barh_one_station.append((xrange_xmin, xrange_xwidth))

    broken_barh_all_stations.append(broken_barh_one_station)

# yrange setting for broken barh
yranges = []
for label_index, lable in enumerate(ylabels):
    yrange_ymin = yticks_position[label_index] - yaxis_unit
    yrange_yheight = 2 * yaxis_unit
    yrange = (yrange_ymin, yrange_yheight)
    yranges.append(yrange)

# plot broken barh for each station
for label_index, lable in enumerate(ylabels):
    ax.broken_barh(broken_barh_all_stations[label_index], yranges[label_index])

ax.grid(True)

ax.autoscale()
loc = mdates.DayLocator()
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))

plt.xticks(rotation=90, ha='right')

plt.show()


# =========== get and combine csv ============

import os

directory_path = input('Enter a directory path: ')




