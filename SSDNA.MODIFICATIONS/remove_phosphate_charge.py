#!/bin/python

import linecache
import sys

filename = sys.argv[1]
string1='electrostatic'
string2='atom'

ele_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
atm_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))


new_file = filename.replace('.dat', '_rem_phos_ch.dat')

out = open(new_file, 'w')
        
for k in range(1, ele_line):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
ss = '      0 electrostatic residues\n'
out.writelines(ss)
    
for l in range(atm_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)
