import os
import matplotlib as plt
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
    directory = 'speedData/' + sys.argv[1]
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    downloadSpeeds = []
    uploadSpeeds = []
    pings = []
    timestamps = []

    for file_name in json_files:
        time_str = os.path.splitext(file_name)[0]
        hours, minutes = map(int, time_str.split('_'))
        decimal_time = hours + (minutes / 60.0)
        timestamps.append(decimal_time)

        file_path = os.path.join(directory, file_name)
        data = read_json_file(file_path)

        ds = data.get("Download Speed (Mbps)")
        us = data.get("Upload Speed (Mbps)")
        p = data.get("Ping (ms)")

        downloadSpeeds.append(ds)
        uploadSpeeds.append(us)
        pings.append(p)

    display_stats(downloadSpeeds, "Download Speed (Mbps)")
    display_stats(uploadSpeeds, "Upload Speed (Mbps)")
    display_stats(pings, "Ping (ms)")

    plot_data(timestamps, downloadSpeeds, "Download Speed (Mbps)")
    plot_data(timestamps, uploadSpeeds, "Upload Speed (Mbps)")
    plot_data(timestamps, pings, "Ping (ms)")

    hour_labels = [f'{int(hour)}:{math.floor(int((hour % 1) * 60)):02}' for hour in timestamps]
    plt.xticks(timestamps, hour_labels)
    plt.show()

if __name__ == "__main__":
    main()