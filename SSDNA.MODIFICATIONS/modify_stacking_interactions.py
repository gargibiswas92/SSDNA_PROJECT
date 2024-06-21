#!/bin/python

import linecache
import sys

filename = sys.argv[1]
string1='stacks'
string2='bonded'
new_dih=0.0

stack_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
bond_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))

val = (stack_line-bond_line)
#fl1, fl2 = filename.split('.')
new_file = filename.replace('.dat', '_stacks_1.dat')
#new_file = fl1+'_stacks_1.dat'

out = open(new_file, 'w')

        
for k in range(1, stack_line+1):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
for j in range(stack_line+1,bond_line):
    line = linecache.getline(filename, j)
    arr1 = line.split()
    ss='{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{}'.format(int(arr1[0]), int(arr1[1]), int(arr1[2]), float(arr1[3]), 1.0, '\n')
    out.writelines(ss)
    
for l in range(bond_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)
