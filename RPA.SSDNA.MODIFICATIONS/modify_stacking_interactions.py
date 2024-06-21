#!/bin/python

import linecache
import sys

filename = sys.argv[1]
string1='stacks'
string2='bonded'

sta_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
bon_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))


new_file = filename.replace('.dat', '_stacks_A.dat')
out = open(new_file, 'w')

stack_4 = 4.00
stack_3 = 3.00
        
for k in range(1, sta_line+1):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
for j in range(sta_line+1, bon_line):
    line = linecache.getline(filename, j)
    arr1 = line.split()
    stack_str = float(arr1[4])
    new_stack = stack_str
    if stack_str == 3.00:
        new_stack=stack_4
    if stack_str == 2.00:
        new_stack=stack_3
    ss = '{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{}'.format(int(arr1[0]), int(arr1[1]), int(arr1[2]), float(arr1[3]), new_stack, '\n')
    out.writelines(ss)

for l in range(bon_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)

