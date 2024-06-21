#!/bin/python

import linecache
import sys

filename = sys.argv[1]
#filename='dynamic_RPA_ssdna25.dat'
string1='dihedral'
string2='contacts'

dih_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
con_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))

val = (con_line-dih_line)

new_dih = 0.4
added_name = '_dih_'+str(0.4)+'.dat'
new_file = filename.replace('.dat', added_name)

out = open(new_file, 'w')

for i in range(dih_line+1, con_line):
    line = linecache.getline(filename, i)
    arr = line.split()
    if int(arr[1])==1340:
        dna_start_line=i
        
for k in range(1, dna_start_line):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
for j in range(dna_start_line, con_line):
    line = linecache.getline(filename, j)
    arr1 = line.split()
    ss = '{:>5d}{:>5d}{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{:>8.3f}{:>8.3f}{}'.format(int(arr1[0]), int(arr1[1]), int(arr1[2]), int(arr1[3]), int(arr1[4]), float(arr1[5]), new_dih, float(arr1[7]), float(arr1[8]), '\n')
    out.writelines(ss)
    
for l in range(con_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)
