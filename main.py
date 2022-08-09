#!/usr/bin/env python3

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import json
import sys

counter = 60
if len(sys.argv)>1:
    filepath = sys.argv[1]
else:
    filepath = "log.json"
with open(filepath) as json_file:
    data = json.load(json_file)

# get only timestamps
# get without seconds part
# convert to datetime
timestamp_arr = [x["timestamp"] for x in data]
clear_timestamp_arr = [":".join(x.split(":")[:-1]) for x in timestamp_arr]
xarr = [datetime.strptime(x, "%Y-%m-%dT%H:%M") for x in clear_timestamp_arr]

# get first, last elements, and their difference
lastel = xarr[0]  # + timedelta(hours=1, minutes=0)
firstel = xarr[-1]  # - timedelta(hours=1, minutes=0)
total_seconds = lastel - firstel

# filling x array for plot
time = firstel
arrayx = []
while time < lastel:
    arrayx.append(time)
    time = time + timedelta(hours=0, minutes=0, seconds=counter)

# filling y array for plot
arrayy = []
totalarr = [[i, 0] for i in arrayx]  # array for filling all together
for timestamp in xarr:
    for i in range(len(totalarr)):
        if i != len(totalarr) - 1 and i != 0:
            if totalarr[i - 1][0] < timestamp < totalarr[i + 1][0]:
                totalarr[i][1] += 1
arrayy = [oneel[1] for oneel in totalarr]

# generate plot
x = np.array(arrayx)
y = np.array(arrayy)

plt.plot(x, y)
plt.show()
