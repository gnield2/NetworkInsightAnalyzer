############################################
##########    getDeviceData.py    ##########
# Code originally created by Connor Riley  #
# Modifications by Gabriel Nield           #
# Email: gabrielnield@proton.me            #
############################################
#######################################################################################
# This program runs a comprehensive diagnostic test on your current Internet Connection
# and outputs that data into json files that represent the date and time the program
# was run. The json files show statistics such as signal strength, RSSI, current and
# available BSSIDs and Access Points, and more.
#######################################################################################
# All of the data that the program receives was thanks to Connor's original vision. I
# made modifications that include ensuring that any json files would be created in a
# "data" directory, and that the program had its own main call.
#######################################################################################

import sys
import os
import subprocess
import json
from datetime import datetime

def getDeviceData(dt, dirname):   
    #runs a process to get information about the current network connection
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode()
    # the next 2 lines are an addition by Gabriel Nield
    dirname = f"data/{dirname}"
    os.makedirs(dirname, exist_ok=True)

    output = results.split('\n')
    currConnection = {}
    data = {}

    #parses the data and gets various categories
    #more categorires can be added to this section in the future
    #if more data is required as not all are parsed out
    for line in output:
        line = line.strip()
        key = line.split(':')
        key[0] = key[0].strip()
        if key[0] == 'BSSID':
            tempkey = key[1:]
            tempkey = ':'.join(tempkey)
            key = ['BSSID', tempkey]
        elif key[0] == 'Physical address':
            tempkey = key[1:]
            tempkey = ':'.join(tempkey)
            key = ['Physical address', tempkey.strip()]
        elif key[0] == 'Signal':
            signal = key[1][1:-1]
            signal = int(signal)
            rssi = (signal/2) - 100
            data['RSSI'] = rssi
            continue
        if len(key[0]):
            if len(key[1]):
                key[1] = key[1].strip()
                data[key[0]] = key[1]


    #runs a process to see available networks and physical connections
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=bssid']).decode()
    output = results.split('\n')

    #parses data from all available networks command\
    #separates data by SSID and then by BSSID under the ssid
    linenum = 0
    currid = ''
    processbid = False
    ssids = {}
    for line in output:
        if line[:4] == 'SSID':
            currid = line.split(':')[1].strip()
            ssids[currid] = {} #dictionary of BSSIDs for each SSID
            processbid = False
            continue
        if not len(ssids):
            continue
        line = line.strip()
        if 'BSSID' in line:
            bid = line.split(':')
            bid = ':'.join(bid[1:]).strip()
            ssids[currid][bid] = {} #dictionary of attributes for each BSSID
            processbid = True
            continue
        if not processbid:
            continue
        #Can add sections to here to parse more data from each BSSID
        #
        #
        #
        if 'Signal' in line:
            signal = line.split(':')[1].strip()[:-1]
            signal = int(signal)
            rssi = (signal/2) - 100
            ssids[currid][bid]['RSSI'] = rssi
            ssids[currid][bid]['Signal'] = signal
        if 'Band'in line:
            band = line.split(':')[1].strip()
            ssids[currid][bid]['Band'] = band
        if 'Channel' in line and 'Utilization' not in line:
            channel = line.split(':')[1].strip()
            ssids[currid][bid]['Channel'] = channel
        elif 'Channel' in line:
            channel = line.split(':')[1].strip()
            ssids[currid][bid]['Utilization'] = channel

    #adds data to the current network connection section of the json file
    currConnection = ssids[data['SSID']][data['BSSID']]
    currConnection['SSID'] = data['SSID']
    currConnection['BSSID'] = data['BSSID']
    currConnection['Receive rate (Mbps)'] = data['Receive rate (Mbps)']
    currConnection['Transmit rate (Mbps)'] = data['Transmit rate (Mbps)']         

    jsonDump = {'Current Connection': currConnection, 'All Connections': ssids}


    
    #sets path for a powershell script that gets coordinates
    #must have coords.ps1 in same directory for this line to work
    #also must have powershell in the same spot
    #path = os.getcwd()
    #coordPath = path + '\\coords.ps1'
    #results = subprocess.check_output(['C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe',coordPath],).decode()

    #parses out the coordinates from the results of the script
    #output = results.split('\n')
    #for thing in output:
    #    if len(thing) > 0:
    #        if thing[0].isnumeric():
    #            latlng = thing.strip()
    #            lat, lng = latlng.split()

    #adds coordinates to the dataframe for the json dump
    #jsonDump['coords'] = {'Lat': float(lat), 'Lng': float(lng)}

    #prints a summary of the data including number of available connections and iformation about
    #the current connection
    print('Available connections:')
    heatCount = 0
    for key in jsonDump['All Connections']:
        count = 0
        for addr in ssids[key]:
            count += 1
            if key == currConnection['SSID']:
                heatCount+=1
        print(' ',key,' has ', count, ' physical addresses visable')
    
    print('\nYou are connected to ',currConnection['SSID'])
    print(' Physical address is ',currConnection['BSSID'])
    print(' Signal strength is ', currConnection['Signal'],'%\n')
    print('RSSI: ', currConnection['RSSI'])
    print('Channel: ', currConnection['Channel'])
    print('Bandwidth: ', currConnection['Band'])

    #Writes dataframe as a json file to the directory previously created
    time = dt[1][:5]
    time = time.split(':')
    time = '_'.join(time)
    title = '/' + time + '.json'
    with open(dirname+title, 'w') as f:
        f.write(json.dumps(jsonDump, sort_keys=False, indent=4))
    
    #-returns the number of availble connections on the current network
    #and the coordinates where the test was run
    #return heatCount, [float(lat), float(lng)]
    return heatCount

# Main call added in order to treat this program as its own entity -GN
# Arguments are the current date and time, and the directory the data will be inputted into
if __name__ == '__main__':
	getDeviceData(str(datetime.now()).split(), str(datetime.now()).split()[0])