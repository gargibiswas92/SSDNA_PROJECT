#!/bin/python

import linecache
import sys
import numpy as np

filename = sys.argv[1]
pdb_file = sys.argv[2]

def read_PDB(pdb_file):
    end_pdb = sum(1 for _ in open(pdb_file))
    x_arr, y_arr, z_arr = [], [], []
    for i in range(2, end_pdb):
        line = linecache.getline(pdb_file, i)
        x, y, z = float(line[26:38]), float(line[38:46]), float(line[46:54])
        x_arr.append(x)
        y_arr.append(y)
        z_arr.append(z)
    x_npr, y_npr, z_npr = np.array(x_arr), np.array(y_arr), np.array(z_arr)
    return x_npr, y_npr, z_npr

string1='atom'

atm_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
end_line = sum(1 for _ in open(filename))

x_npr, y_npr, z_npr = read_PDB(pdb_file)

added_name = '_frame.dat'
new_file = filename.replace('.dat', added_name)

out = open(new_file, 'w')
     
for k in range(1, atm_line+5):
    line = linecache.getline(filename, k)
    out.writelines(line)
 
count = 1   
for j in range(atm_line+5, end_line+1):
    line = linecache.getline(filename, j)
    arr1 = line.split()
    ss = '{:>5d}{:>4d}{:>3s}{:>4s}{:>8.3f}{:>8.3f}{:>8.3f}{:>8.3f}{:>3d}{}'.format(int(arr1[0]), int(arr1[1]), arr1[2].strip(), arr1[3].strip(), x_npr[count], y_npr[count], z_npr[count], 1.0, 0, '\n')
    out.writelines(ss)
    count = count + 1
    

out.close()