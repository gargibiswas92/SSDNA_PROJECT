#!/bin/python

import linecache
import sys

file = '/trajectories/gargi/RPA_Ed/CODE.REPOSITORY/RPA.SSDNA.MODIFICATIONS/repA_dna235.pdb'
outname = sys.argv[1]
init_num = int(sys.argv[2])
end_num = int(sys.argv[3])

outfile = open(outname, 'w')

for i in range(1, 5426):
    line = linecache.getline(file, i)
    outfile.writelines(line)
    
count = 5426   
for j in range(5426, 9933):
    line = linecache.getline(file, j)
    init = line[0:4]
    atnum = int(line[4:11])
    mid = line[11:22]
    resnum = int(line[22:26])
    end = line[26:-1]
    
    if resnum >= init_num and resnum <=end_num:
        new_res = resnum -init_num + 1
        ss = '{}{:>7d}{}{:>4d}{}{}'.format(init, count, mid, new_res,end, '\n')
        outfile.writelines(ss)
        count = count + 1
        
outfile.close()