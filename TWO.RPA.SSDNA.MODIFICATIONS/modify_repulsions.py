#!/bin/python

import linecache
import sys

filename = sys.argv[1]
string1='repulsive'
string2='electrostatic'

rep_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
ele_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))


new_file = filename.replace('.dat', '_ch_rep_1.6.dat')
out = open(new_file, 'w')

pp_rep = 10.24
pb_rep = 9.61
        
for k in range(1, rep_line+1):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
for j in range(rep_line+1, ele_line):
    line = linecache.getline(filename, j)
    arr1 = line.split()
    rep_rad = float(arr1[3])
    new_rep = rep_rad
    if rep_rad > 51.0 and rep_rad < 56.0:
        new_rep=pp_rep 
    if rep_rad > 25.0 and rep_rad < 29.0:
        new_rep=pb_rep
    ss = '{:>8d}{:>5d}{:>5d}{:>10.3f}{:>10.3f}{}'.format(int(arr1[0]), int(arr1[1]), int(arr1[2]), new_rep, float(arr1[4]), '\n')
    out.writelines(ss)

for l in range(ele_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)

