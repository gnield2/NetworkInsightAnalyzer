# Network Insight Analyzer (NISA)
**Creator:** Gabriel Nield <br>
**Email:** gabrielnield@proton.me

Network Insight Analyzer, or NISA, is my individual undergraduate research project for my fall senior semester at the University of Notre Dame. In the spring of 2023, I approached my then-professor of Operating Systems Principles, Prof. Aaron Striegel, who suggested a wealth of different paths I could take for my research. We decided that it might be fun to take an existing research project done by another Notre Dame undergrad, Connor Riley, and make a tool different from the one he made to expand on his vision while also making it my own in some unique ways.

Connor created a tool that would take data from the network protocol analyzer [Wireshark](https://www.wireshark.org/) and display data that the packets would give him. My tool takes data about the current network and surrounding available networks and conducts a thorough analysis of the connection(s). This includes displaying data such as access points, BSSIDs, signal strength, and many more, including data received from conducting an Ookla Speedtest.

A link to Connor's project is [here](https://github.com/criley6nd/NetworkResearchSP2022).

Here is a brief rundown of each of the existing program files in this repo and what they do:<br>
**_getDeviceData.py_**: Named after a file of the same name in Connor's repo, the bulk of the code is largely the same, except for some additions and redactions made too fit this project. Namely, the code referring to Wireshark packet parsing and coordinates are taken out, while the additions include outputting each of the json files into a directory called data and ensuring that the files are organized by date. This code gathers information about the current network connection and other available connections and outputs the information into json files named after their timestamps.<br>
**_test_speed.py_**: Very much in the same vein as _getDeviceData.py_, except this program takes data from an Ookla Speedtest run and outputs data into a json file named after the timestamp, in a folder named after the date, which is in another folder called speedData.<br>
**_plot_data.py_**: Takes the data resulting from _getDeviceData.py_ and plots the BSSID connections at specific points in time to see how the connection may switch over time. Also displays numeric information regarding signal strength (mean, median, quartiles, std. dev).<br>
**_plot_speedData.py_**: Takes the data resulting from _test_speed.py_ and plots the down speed, up speed, and ping with respect time. Also displays numeric information regarding these stats (mean, median, quartiles, std. dev).<br>
**_run_program.py_**: A simple caller program that executes _getDeviceData.py_ and _test_speed.py_ every minute. This is effective for creating multiple data points to use for plotting and analyzing.

Additionally, **_setup.bat_** is the script that the user will need to run to ensure that the code will run on their machine. The user will need to install Python 3 beforehand, but this setup script ensures that pip3 is installed as well as all of the necessary Python libraries needed for each program.

As of December 8, 2023, this tool lies in a functional, yet unfinished state. The plotting code, in particular, does not plot the code perfectly. Specifically, the x-axis values for time appear more than once, and the BSSIDs are also numbered in a strange way. Instead of them being numbered 0, 1, 2, etc., they are numbered based on the last minute they held a connection. For example, in _plot_data.py_, the first BSSID is enumerated as 8 because it lasted until the 9th minute, and the second BSSID is enumerated as 24 because it lasted until minute 25. This will need a fix thta hopefully shouldn't be too major. The programs that gather the data work optimally.

This is an unfinished project and a work in progress, but I am happy with that. This has turned from a research project I am somewhat interested in to a passion project I can see myself editing, completing, finishing for weeks, months, even years down the line after this semester is over. I have learned a lot about how to analyze data and got a much-needed refresher in my Python knowledge.

## Setup Instructions - Windows 10 & 11
**Before running the setup script, ensure that Python 3 is installed on your machine. If it isn't, you can download it from the Microsoft Store [here](https://apps.microsoft.com/detail/9NRWMJP3717K?hl=en-us&gl=US).**

**1. Run _setup.bat_**<br>
Once Python 3 is installed on your machine, run the batch file _setup.bat_ included in the repo. This will ensure that the necessary Python libaries and tools are installed, along with pip if it has not yet been installed.

**2. Run _getDeviceData.py_ and _test_speed.py_**<br>
You can choose to run either of these programs individually at sporadic times to get just one json data file for each run, but what is recommended that you do is run _run_program.py_. This will execute both of the above programs once every minute so that you can create multiple files of data in the background. Just press **ctrl+c** in your terminal whenever you feel that you have enough data.

**3. Run _plot_data.py_ and _plot_speedData.py_**<br>
In order to run these programs correctly, you must specify a specific date to plot data from. For example, if you want to display the results from _test_speed.py_ runs from December 9, 2023, your terminal command should look like this:

    python3 plot_speedData.py 2023-12-09

In this case, "2023-12-09" is the name of the directory created when the program was run, and it holds all of the json files named after their timestamps. Similarly, if you want to display the results from _getDeviceData.py_ runs from April 16, 2024, input the following command:

    python3 plot_data.py 2024-04-16

As the complexity of this project grows, you can expect more setup instructions to be added.