###################################
#####    plot_speedData.py    #####
# Author: Gabriel Nield           #
# Email:  gabrielnield@proton.me  #
###################################
###############################################################################################
# This is a program that plots data from json files created from the program test_speed.py.
# The user must input a specific date in the function call so that only the data from that date 
# will be plotted. Right now the plotting method is somewhat crude, but one can expect this to 
# work with a tool such as d3js.
###############################################################################################

import os
import matplotlib.pyplot as plt
import json
import sys
import math
import statistics

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def plot_data(x, y, title, y_label):
    plt.scatter(x, y)
    plt.xlabel("Time of Day")
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid = True

def display_stats(data, data_name):
    print(data_name)
    print('Mean:                    ' + str(statistics.mean(data)))
    print('Median:                  ' + str(statistics.median(data)))
    print('Standard Deviation:      ' + str(statistics.stdev(data)))
    print('Quartiles:               ' + str(statistics.quantiles(data)))

def main():
    # The user must specify an argument for the particular folder/date they want to read from
    # i.e. "$> python3 plot_data.py 2023-10-02" to read data from October 02, 2023
    directory = '../speedData/' + sys.argv[1]
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    downloadSpeeds = []
    uploadSpeeds = []
    pings = []
    timestamps = []

    for file_name in json_files:
        # Use the name of each json file to pinpoint the time test_speed.py was run
        time_str = os.path.splitext(file_name)[0]
        hours, minutes = map(int, time_str.split('_'))
        decimal_time = hours + (minutes / 60.0)
        timestamps.append(decimal_time)

        # read the data from each json file
        file_path = os.path.join(directory, file_name)
        data = read_json_file(file_path)
        
        # Divide the data into three different arrays: Down Speed, Up Speed, and Ping
        ds = data.get("Download Speed (Mbps)")
        us = data.get("Upload Speed (Mbps)")
        p = data.get("Ping (ms)")
        downloadSpeeds.append(ds)
        uploadSpeeds.append(us)
        pings.append(p)

    # Print out the mean, median, std. dev, and quartiles for all parameters
    display_stats(downloadSpeeds, "Download Speed (Mbps)")
    display_stats(uploadSpeeds, "Upload Speed (Mbps)")
    display_stats(pings, "Ping (ms)")

    # plot the data for each parameter with respect to time
    plot_data(timestamps, downloadSpeeds, "Download Speed (Mbps)", "Download Speed (Mbps)")
    plot_data(timestamps, uploadSpeeds, "Upload Speed (Mbps)", "Upload Speed (Mbps)")
    plot_data(timestamps, pings, "Ping (ms)", "Ping (ms)")

    # this is so that the x-axis shows the time at which getDeviceData.py was run
    # it doesn't work perfectly--some values show up twice on the axis
    hour_labels = [f'{int(hour)}:{math.floor(int((hour % 1) * 60)):02}' for hour in timestamps]
    plt.xticks(timestamps, hour_labels)
    plt.show()

if __name__ == "__main__":
    main()