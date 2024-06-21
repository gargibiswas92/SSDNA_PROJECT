#!/bin/python

import linecache
import sys

filename = sys.argv[1]
start_num = int(sys.argv[2])

string1='bonded'
string2='angle'

end_num = start_num + 3*22
mid_num = start_num + 3*11

forward_list = []
for i in range(start_num, mid_num, 3):
    forward_list.append(i)
    
back_list = []
for j in range(end_num, mid_num, -3):
    back_list.append(j)
    
#for item, item1 in zip(forward_list, back_list):
#    print(item, item1)
    

bond_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
ang_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
end_line = sum(1 for _ in open(filename))

bond_line_cont = linecache.getline(filename, bond_line)
arr = bond_line_cont.split()
bo_num = int(arr[0])
new_bo_num = bo_num + len(back_list)

ssp = '{:>10d} Hookean bonded pair{}'.format(new_bo_num, '\n')


added_name = '_bond.dat'
new_file = filename.replace('.dat', added_name)

out = open(new_file, 'w')
        
for k in range(1, bond_line):
    line = linecache.getline(filename, k)
    out.writelines(line)
    
out.writelines(ssp)
    
for j in range(bond_line+1, ang_line):
    line = linecache.getline(filename, j)
    out.writelines(line)
 
count = 1       
for i in range(len(forward_list)):
    ss='{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{}'.format(bo_num+count, forward_list[i], back_list[i], 55.0, 5.0, '\n')
    out.writelines(ss)
    count = count + 1
    
for l in range(ang_line, end_line+1):
    line = linecache.getline(filename, l)
    out.writelines(line)
    
out.close()
    
