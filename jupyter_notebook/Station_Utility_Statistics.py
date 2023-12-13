import time
import datetime
import os, glob
from matplotlib import pyplot as plt
from matplotlib import ticker
import csv
import numpy as np
import pandas as pd
import matplotlib.dates as mdates


def station_utility_calulation(df):

    fig, ax = plt.subplots(figsize=(30,10))

    # df = pd.read_csv('/Users/qingjie/Library/Mobile Documents/com~apple~CloudDocs/documents/project_apple/macatv/j604/p1/smt_combine/SMT_station_utility.csv')
    project_name = df.loc[0, 'product']
    station_type = df.loc[0, 'STATION_TYPE'].split('-')[0]

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

    plt.title(project_name + " " + station_type + " station utility plot")

    plt.show()

    fig.savefig(dir_path + "_station_utility.pdf", bbox_inches='tight')

    # print(len(broken_barh_all_stations))
    # grouped_1

# =========== mlb_rf_vendor_distribution ============

def mlb_rf_vendor_distribution(df):

    fig, ax = plt.subplots(figsize=(30,10))

    grouped_1 = df.groupby(["STATION_TYPE", "STATION_NUMBER"], as_index=False).count()
    grouped_2 = df.groupby(["STATION_TYPE", "STATION_NUMBER", "ATL_WF_MREV"], as_index=False).count()
    df1 = df.sort_values(by=['STATION_TYPE','STATION_NUMBER','Test Start Time'], ignore_index=True)

    list_mlb_rf_vendor = list(grouped_2['ATL_WF_MREV'].value_counts().index)
    # ['4.7   V=a', '4.7   V=u']

    xlabels = [] 

    for index in grouped_1.index:
        xlabels.append(grouped_1.loc[index, 'STATION_TYPE'] + "_" + str(grouped_1.loc[index, 'STATION_NUMBER']))

    # xlabels = ['SMT-COEX1_1', 'SMT-COEX1_2', 'SMT-COEX1_3', 'SMT-COEX1_1', 'SMT-COEX1_2', 'SMT-COEX1_3', 'SMT-COEX2_1']


    # V=a for each station 
    unit_number_each_vendor = []
    for index, vendor in enumerate(list_mlb_rf_vendor):
        for label in xlabels:
            for index_gropued_1 in grouped_1.index:
                unit_number_each_vendor.append(grouped_2.loc[(grouped_2['ATL_WF_MREV']==vendor), (grouped_2['Serial Number'])])
            










# =========== find and combine csv ============
def find_and_combinie_csv():
    global dir_path
    # dir_path = '/Users/qingjie/Library/Application Support/Radar/Downloads/Problem/107771556/Final_0607_PWYS_SMT_P1_Coex_offline_daily_report/SMT_All'
    dir_path = input("drag the folder which contains all SMT/FATP data: ").replace("'", "")

    to_be_combined_csv_path = []

    # with os.scandir(dir_path) as dir1:
    #     for entry1 in dir1:
    #         if entry1.is_dir():
    #             with os.scandir(entry1) as dir2:
    #                 for entry2 in dir2:
    #                     if entry2.name[0].isdigit() & entry2.name.endswith(".csv") :
    #                         to_be_combined_csv_path.append(entry2.path)

    # find all resut csv in a ceratin foler and its sub folder
    to_be_find_path = dir_path + "/**/[0-9]*.csv"
    for f in glob.glob(to_be_find_path, recursive=True):
        to_be_combined_csv_path.append(f)

    # The first file set as base to be merged with others
    # read only certain columns we want
    wanted_columns = []
    for i in range (0,28,1):
        wanted_columns.append(i)

    # for rest of csv, we only want the index = 7 row, which contains needed data
    wanted_rows = [5]

    # # The scond row as header, header = 1
    # df_csv_1 = pd.read_csv(to_be_combined_csv_path[0], header=1, usecols = wanted_columns, skiprows=lambda x: x not in wanted_rows)
    # # df_csv_1

    # initialize df_concat as the first csv datafrme, 
    df_concat = pd.read_csv(to_be_combined_csv_path[0], header=1, usecols = wanted_columns, skiprows=[2,3,4,5,6])

    # df_csv_next = pd.read_csv(to_be_combined_csv_path[1], header=1, usecols = wanted_columns, skiprows=[2,3,4,5,6])
    # df_concat = pd.concat([df_concat, df_csv_next], ignore_index=True)

    for file_index, file in enumerate(to_be_combined_csv_path):
        if file_index + 1 < len(to_be_combined_csv_path):
            df_csv_next = pd.read_csv(to_be_combined_csv_path[file_index+1], header=1, usecols = wanted_columns, skiprows=[2,3,4,5,6])
            df_concat = pd.concat([df_concat, df_csv_next], ignore_index=True)

    return df_concat


def main():
    dfconcat = find_and_combinie_csv()
    station_utility_calulation(dfconcat)
    mlb_rf_vendor_distribution(dfconcat)


if __name__ == "__main__":
    main()



    


