## Date: October 29, 2023

  At this point in the research project, I have taken one file from Connor Riley's research, getDeviceData.py, and used that program to create a new direction for part of Connor's original vision.
  Each file has a different purpose. getDeviceData.py is the main code being run for the eventual "graphical interface program" that I could create if time allows. It has redactions and additions from Connor's original code to better fit the direction for this project, namely not relying on Wireshark and pcap files.
  run_program.py is a simple program that runs getDeviceData.py every minute, so that a user could see updates about their network connection and other connections in real time.
  plot_data.py plots the data outputted from getDeviceData.py to display which access point the user is connected to at a given time.
  test_speed.py runs an Ookla Speedtest test for the user and outputs the data in files that display the timestamps and date.

More programs will be added to the project as it progresses.
