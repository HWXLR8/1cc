#!/usr/bin/env python3
import csv, subprocess

vals = [int(v) for row in csv.reader(open('log.csv')) for v in row[1:] if v.strip()]
data = '\n'.join(f'{i} {v}' for i, v in enumerate(vals))

subprocess.run(['gnuplot', '--persist', '-'], text=True, input=f"""
$DATA << EOD
{data}
EOD
set fit nolog
a = 1; b = 1
f(x) = a*x + b
fit f(x) $DATA using 1:2 via a, b
set title sprintf("y = %.4f x + %.2f", a, b)
set grid
plot $DATA using 1:2 with lines title 'level', f(x) title 'fit'
""")
