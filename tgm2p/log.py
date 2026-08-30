#!/usr/bin/env python3

import datetime
import os

f = open('log.csv', 'a')
f.write(datetime.datetime.today().strftime("%Y-%m-%d"))

while line := input("enter level: "):
    f.write(',' + line)
    f.flush()
    os.fsync(f.fileno())

f.write('\n')
