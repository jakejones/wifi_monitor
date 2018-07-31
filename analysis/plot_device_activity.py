#! /usr/bin/env python
"""
Plot Activity as a function of time.
Command line arguments:
:param 1: logfile_path
:param 2: MAC address to plot
"""
import sys
import matplotlib.pyplot as plt
import datetime
if len(sys.argv) < 3:
    raise ValueError('You must provide the path to the log file! AND the MAC address to plot')
data_path = sys.argv[1]
mac_addr = sys.argv[2]



# -- Init Variables --
activity = {}
timeAxis = {}
tempActivity = None
dT = 5.0*60.0 # 5 Minute Resolution
current_T = 0
start_T = 0


# -- Read Log File --
with open(data_path,'r') as logfile:
    for line in logfile:
        time, mac = line.split()
        T = float(int(float(time)/dT)*int(dT))

        # --- Record Start Time ---
        if (start_T == 0) & (current_T != 0):
            start_T = current_T

        # --- Append activity to plot, and clear tempActivity ---
        if not T == current_T:
            current_T = T
            if tempActivity is not None:
                for M in tempActivity:

                    if M in activity:
                        activity[M].append(tempActivity[M])
                        timeAxis[M].append((T-start_T)/3600.0)
                    else:
                        activity[M] = [tempActivity[M]]
                        timeAxis[M] = [(T-start_T)/3600.0]
            tempActivity = {}
        
        # --- Accumulate Activity ---
        if mac in tempActivity:
            tempActivity[mac] += 1
        else:
            tempActivity[mac] = 1
        
logfile.close()


print "Start Time:", datetime.datetime.fromtimestamp( int(start_T) ).strftime('%Y-%m-%d %H:%M:%S')
plt.bar(timeAxis[mac_addr],activity[mac_addr],dT/3600.0)
plt.title("Network Activity of '" + mac_addr + "'")
plt.xlabel("Time Since Start (Hours)")
plt.ylabel("Activity (Frames Detected)")
plt.show()
