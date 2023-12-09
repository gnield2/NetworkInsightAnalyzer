###################################
#######    test_speed.py    #######
# Author: Gabriel Nield           #
# Email:  gabrielnield@proton.me  #
###################################
#################################################################################################
# This program was heavily inspired from getDeviceData.py, originally created by Connor Riley.
# This, however, uses Ookla Speedtest to acquire data such as Download Speed, Upload Speed, and
# Ping. Just like getDeviceData.py, the data is put into json files, this time beneath a
# directory titled "speedData".
#################################################################################################

import os
import json
import speedtest
from datetime import datetime

def main():
    # Get the time and date from datetime.now() and parse it into usable strings
    dt = str(datetime.now()).split()
    date = dt[0]
    time = dt[1][:5]
    time_thing = time.split(':')
    time_str = '_'.join(time_thing)

    # The data for these runs will go into a subdirectory containing the date they were run
    # i.e. if this program was run on October 02, 2023, the resulting data will be forwarded
    # to the directory speedData/2023-10-02
    directory = f"speedData/{date}"
    os.makedirs(directory, exist_ok=True)

    servers = []
    threads = None

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()

    download = s.download(threads=threads) / 1_000_000
    upload = s.upload(threads=threads) / 1_000_000

    results = {
        "Date": date,
        "Time": time,
        "Download Speed (Mbps)": download,
        "Upload Speed (Mbps)": upload,
        "Ping (ms)": s.results.ping,
    }

    # Each run will have a json file named after the time it was run in 24-hour time.
    # i.e. if this program is run at 9:35 AM, the data can be found in a file called "09_35.json"
    # and if this program is run at 5:45 PM, the data can be found in a file called "17_45.json"
    file_path = f"{directory}/{time_str}.json"

    with open(file_path, "w") as file:
        json.dump(results, file, indent=4)

    # This is the format that this program uses to input the data into each of the json files
    print('Ping (ms):           ' + str(s.results.ping))
    print('Download (Mbps):     ' + str(download))
    print('Upload (Mbps):       ' + str(upload))
    print("Speedtest results saved to:", file_path)

if __name__ == "__main__":
    main()