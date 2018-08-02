#! /usr/bin/env python
import sys
import os
import datetime

if len(sys.argv) < 2:
    raise ValueError('You must provide the directory to save data to!')
data_dir = sys.argv[1]


def get_file(p):
        path = data_dir + "/" + p
        if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
        return open(path,"a+")

current_hour = 0
for line in sys.stdin:
        try:
                time,mac = line.split()
                hour = int(float(time)/3600.0)*3600
                if current_hour != hour:
                        current_hour = hour
                        try:
                                f.close()
                        except Exception:
                                pass
                        f = get_file(datetime.datetime.fromtimestamp(current_hour))
                f.write(line)
        except Exception:
                pass
                