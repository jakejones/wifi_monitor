#! /usr/bin/env python
"""
List all MAC addresses that were detected.
"""
import sys
import requests
if len(sys.argv) < 2:
    raise ValueError('You must provide the path to the log file!')
data_path = sys.argv[1]


# -- Read Log File --
activity = {}
with open(data_path,'r') as logfile:
    for line in logfile:
        time, mac = line.split()
        if mac in activity:
            activity[mac] += 1
        else:
            activity[mac] = 1 
logfile.close()


for mac in activity:
    vendor = requests.get('http://macvendors.co/api/vendorname/' + mac )
    info = ["MAC: "+mac,"Frames: "+str(activity[mac]),"Vendor: "+vendor.text]
    print "\t".join(info)