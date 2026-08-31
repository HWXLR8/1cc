#!/usr/bin/env python3
import csv
import io
import matplotlib.pyplot as plt
import numpy as np

def _vals(text):
    for row in csv.reader(io.StringIO(text)):
        if not row or not row[0]:
            continue
        d = row[0]
        for v in row[1:]:
            try:
                yield d, int(v)
            except ValueError:
                continue

rows = list(_vals(open('log.csv').read()))

x = np.arange(len(rows))
y = np.array([v for _, v in rows])
dates = [d for d, _ in rows]

a, b = np.polyfit(x, y, 1)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, a * x + b, 'k-', label=f'y = {a:.4f}x + {b:.2f}')
ax.legend()
ax.set_title('Level log')
plt.tight_layout()
plt.show()
