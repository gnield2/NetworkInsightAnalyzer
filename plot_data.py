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

def plot_data(x, y, title):
    plt.scatter(x, y)
    plt.xlabel("Time of Day")
    plt.ylabel("Access Point")
    plt.title(title)
    plt.grid = True

def display_stats(data):
    print('Mean:                    ' + str(statistics.mean(data)))
    print('Median:                  ' + str(statistics.median(data)))
    print('Standard Deviation:      ' + str(statistics.stdev(data)))
    print('Quartiles:               ' + str(statistics.quantiles(data)))

def main():
    directory = 'data/' + sys.argv[1]
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    bssids = []
    timestamps = []
    signals = []

    for file_name in json_files:
        time_str = os.path.splitext(file_name)[0]
        hours, minutes = map(int, time_str.split('_'))
        decimal_time = hours + (minutes / 60.0)
        timestamps.append(decimal_time)

        file_path = os.path.join(directory, file_name)
        data = read_json_file(file_path)

        current_connection = data.get("Current Connection", {})
        bssid = current_connection.get("BSSID")
        signal = current_connection.get("Signal")

        bssids.append(bssid)
        signals.append(signal)

    display_stats(signals)

    bssid_to_index = {bssid: index for index, bssid in enumerate(bssids)}

    y_values = [bssid_to_index[bssid] for bssid in bssids]
    plot_data(timestamps, y_values, "Nieuwland 184")
    
    hour_labels = [f'{int(hour)}:{math.floor(int((hour % 1) * 60)):02}' for hour in timestamps]
    plt.xticks(timestamps, hour_labels)
    plt.show()
    
if __name__ == "__main__":
    main()