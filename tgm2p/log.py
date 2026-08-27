#!/usr/bin/env python3

import datetime

f = open('log.csv', 'a')
f.write(datetime.datetime.today().strftime("%Y-%m-%d"))

while line := input("enter level: "):
    f.write(',' + line)

f.write('\n')
