#!/bin/python

import linecache
import sys

max_val = int(sys.argv[1])
out = sys.argv[2]

def replace_string_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        file_content = file.read()
    modified_content = file_content.replace(old_string, new_string)
    with open(file_path, 'w') as file:
        file.write(modified_content) 

#max_val= 47
#out = 'testfile.dat'
out1 = open(out, 'w')
filename='dna.dat'
string1='stacks'
string2='bonded'
string3='angle'
string4='dihedral'
string5='contacts'
string6='repulsions'
string7='electrostatic'
string8='atom'
string9='second'

stack_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
bond_line = next((i+1 for i, line in enumerate(open(filename)) if string2 in line), None)
ang_line = next((i+1 for i, line in enumerate(open(filename)) if string3 in line), None)
dih_line = next((i+1 for i, line in enumerate(open(filename)) if string4 in line), None)
con_line = next((i+1 for i, line in enumerate(open(filename)) if string5 in line), None)
rep_line = next((i+1 for i, line in enumerate(open(filename)) if string6 in line), None)
ele_line = next((i+1 for i, line in enumerate(open(filename)) if string7 in line), None)
atm_line = next((i+1 for i, line in enumerate(open(filename)) if string8 in line), None)
end_line = sum(1 for _ in open(filename))


stack_count=1
stack_init='stacks'+'\n'
out1.writelines(stack_init)
for i in range(stack_line+1, bond_line-1):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val and int(arr[2]) <= max_val):
        ss='{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{}'.format(stack_count, int(arr[1]), int(arr[2]), float(arr[3]), float(arr[4]), '\n')
        out1.writelines(ss)
        stack_count = stack_count + 1
        
bond_count=1
bond_init='bonded'+'\n'
out1.writelines(bond_init)
for i in range(bond_line+1, ang_line-1):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val and int(arr[2]) <= max_val):
        ss='{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{}'.format(bond_count, int(arr[1]), int(arr[2]), float(arr[3]), float(arr[4]), '\n')
        out1.writelines(ss)
        bond_count = bond_count + 1
        
        
ang_count=1
ang_init='angle'+'\n'
out1.writelines(ang_init)
for i in range(ang_line+1, dih_line-1):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val and int(arr[2]) <= max_val and int(arr[3]) <= max_val):
        ss='{:>5d}{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{}'.format(ang_count, int(arr[1]), int(arr[2]), int(arr[3]), float(arr[4]), float(arr[5]), '\n')
        out1.writelines(ss)
        ang_count = ang_count + 1
        
dih_count=1
dih_init='dihedral'+'\n'
out1.writelines(dih_init)
for i in range(dih_line+1, con_line-1):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val and int(arr[2]) <= max_val and int(arr[3]) <= max_val and int(arr[4]) <= max_val):
        ss='{:>5d}{:>5d}{:>5d}{:>5d}{:>5d}{:>8.3f}{:>8.3f}{:>8.3f}{:>8.3f}{}'.format(dih_count, int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), float(arr[5]), float(arr[6]), float(arr[7]), float(arr[8]), '\n')
        out1.writelines(ss)
        dih_count = dih_count + 1
        
con_init='contacts'+'\n'
out1.writelines(con_init)
con_count = 1

rep_count=1
rep_init='repulsions'+'\n'
out1.writelines(rep_init)
for i in range(rep_line+1, ele_line-1):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val and int(arr[2]) <=  max_val):
        ss='{:>8d}{:>5d}{:>5d}{:>10.3f}{:>10.3f}{}'.format(rep_count, int(arr[1]), int(arr[2]), float(arr[3]), float(arr[4]), '\n')
        out1.writelines(ss)
        rep_count = rep_count + 1
        
ele_count=1
ele_init='electrostatic'+'\n'
out1.writelines(ele_init)
for i in range(ele_line+1, atm_line-1):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val):
        ss='{:>8d}{:>5d}{:>8.3f}{}'.format(ele_count, int(arr[1]), float(arr[2]), '\n')
        out1.writelines(ss)
        ele_count = ele_count + 1
        
atm_count=1
atm_init='atom'+'\n'+'          2 chains.'+'\n'+'          1 is the size of chain      1.'+'\n'
atm_init2='second'+'\n'
out1.writelines(atm_init)
out1.writelines(atm_init2)
for i in range(atm_line+4, end_line):
    line = linecache.getline(filename, i)
    arr = line.split()
    if (int(arr[1]) <= max_val):
        ss='{:>5d}{:>4d}{:>3s}{:>4s}{:>8.3f}{:>8.3f}{:>8.3f}{:>8.3f}{}'.format(atm_count, atm_count, (arr[2].strip()), (arr[3].strip()), float(arr[4]), float(arr[5]), float(arr[6]), float(arr[7]), '\n')
        out1.writelines(ss)
        atm_count = atm_count + 1
out1.close() 

string1a='      '+str(stack_count-1)+' stacks'
replace_string_in_file(out, string1, string1a)
string2a='      '+str(bond_count-1)+' Hookean bonded pairs'
replace_string_in_file(out, string2, string2a)
string3a='      '+str(ang_count-1)+' bond angle trios'
replace_string_in_file(out, string3, string3a)
string4a='      '+str(dih_count-1)+' dihedral quartet'
replace_string_in_file(out, string4, string4a)
string5a='      '+str(con_count-1)+' contacts'
replace_string_in_file(out, string5, string5a)
string6a='      '+str(rep_count-1)+' repulsions'
replace_string_in_file(out, string6, string6a)
string7a='      '+str(ele_count-1)+' electrostatic residues.'
replace_string_in_file(out, string7, string7a)
string8a='         '+str(atm_count-1)+' atom positions.'
replace_string_in_file(out, string8, string8a)
string9a='         '+str(atm_count-2)+' is the size of chain      2.'
replace_string_in_file(out, string9, string9a)