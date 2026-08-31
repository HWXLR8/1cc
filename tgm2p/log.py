#!/usr/bin/env python3

import datetime
import os

date = datetime.datetime.today().strftime("%Y-%m-%d")
f = open('log.csv', 'a+')
f.seek(0)
lines = f.readlines()
last = lines[-1] if lines else ''
if last.startswith(date):
    if last.endswith('\n'):
        f.truncate(f.tell() - 1)
else:
    if last and not last.endswith('\n'):
        f.write('\n')
    f.write(date)

while line := input("enter level: "):
    f.write(',' + line)
    f.flush()
    os.fsync(f.fileno())

f.write('\n')
