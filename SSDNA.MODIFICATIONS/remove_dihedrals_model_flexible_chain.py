#!/bin/python

import linecache
import sys

filename = sys.argv[1]
string1='dihedral'
string2='contact'
new_dih_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

dih_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
con_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))

for item in new_dih_list:
    added_name = '_dih_'+str(item)
    new_file = filename.replace('.dat', added_name)

    out = open(new_file, 'w')
        
    for k in range(1, dih_line):
        line = linecache.getline(filename, k)
        out.writelines(line)
    
        ss = '      0 dihedral quartet\n'
        out.writelines(ss)
    
        for l in range(con_line, end_line+1):
            line = linecache.getline(filename, l)
            out.writelines(line)
