import os
import json
import speedtest
from datetime import datetime

def main():
    dt = str(datetime.now()).split()
    date = dt[0]
    time = dt[1][:5]
    time_thing = time.split(':')
    time_str = '_'.join(time_thing)

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

    file_path = f"{directory}/{time_str}.json"

    with open(file_path, "w") as file:
        json.dump(results, file, indent=4)

    print('Ping (ms):           ' + str(s.results.ping))
    print('Download (Mbps):     ' + str(download))
    print('Upload (Mbps):       ' + str(upload))
    print("Speedtest results saved to:", file_path)

if __name__ == "__main__":
    main()