#!/bin/python

import linecache
import sys

filename = sys.argv[1]
string1='angle'
string2='dihedral'

ang_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
dih_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))


new_file = filename.replace('.dat', '_ch_rep.dat')
out = open(new_file, 'w')

pb_ang = 1.1
pp_ang = 1.2
        
for k in range(1, ang_line+1):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
for j in range(ang_line+1, dih_line):
    line = linecache.getline(filename, j)
    arr1 = line.split()
    ang_val = float(arr1[4])
    new_ang = ang_val
    if ang_val > 2.1 and ang_val < 2.3:
        new_ang=pb_ang 
    if ang_val > 2.1 and ang_val < 2.3:
        new_ang=pb_ang
    ss = '{:>5d}{:>5d}{:>5d}{:>5d}{:>10.3f}{:>10.3f}{}'.format(int(arr1[0]), int(arr1[1]), int(arr1[2]), float(arr1[3]),new_ang, float(arr1[5]), '\n')
    out.writelines(ss)

for l in range(dih_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)
