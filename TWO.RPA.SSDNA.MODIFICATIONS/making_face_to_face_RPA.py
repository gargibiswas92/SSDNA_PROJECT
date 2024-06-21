#!/bin/python

import linecache
import math
import numpy as np
def get_coord(file, num):
    line = linecache.getline(file, num)
    x = float(line[26:38])
    y = float(line[38:46])
    z = float(line[46:54])
    return x, y, z

def direction_cosines(x1, y1, z1, x2, y2, z2):
    d = np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    l = (x2 - x1) / d
    m = (y2 - y1) / d
    n = (z2 - z1) / d
    
    return l, m, n

def rotate_point_180(x, y, z, l, m, n):
    rotation_matrix = np.array([
        [2*l**2-1, 2*l*m, 2*l*n],
        [2*l*m, 2*m**2-1, 2*m*n],
        [2*l*n, 2*m*n, 2*n**2-1]
    ])
    point = np.array([[x], [y], [z]])
    rotated_point = np.dot(rotation_matrix, point)
    rotated_x, rotated_y, rotated_z = rotated_point.flatten()
    return rotated_x, rotated_y, rotated_z


def rotate_PDB(filename, l, m, n, outfile):
    inp = open(filename, 'r')
    out = open(outfile, 'w')
    for line in inp:
        if line.startswith('ATOM'):
            init = line[0:26]
            x = float(line[26:38])
            y = float(line[38:46])
            z = float(line[46:54])
            end = line[54:-1]
            (r_x, r_y, r_z) = rotate_point_180(x, y, z, l, m, n)
            ss = '{}{:>12.3f}{:>8.3f}{:>8.3f}{}{}'.format(init, r_x, r_y, r_z, end, "\n")
            out.writelines(ss)
        else:
            out.writelines(line)

def distance(x1, y1, z1, x2, y2, z2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    dz = (z2 - z1)
    return dx, dy, dz
    
def translate_PDB(filename, tr_x, tr_y, tr_z, outfile):
    inp = open(filename, 'r')
    out = open(outfile, 'w')
    for line in inp:
        if line.startswith('ATOM'):
            init = line[0:26]
            x = float(line[26:38])
            y = float(line[38:46])
            z = float(line[46:54])
            end = line[54:-1]
            n_x = x + tr_x
            n_y = y + tr_y
            n_z = z + tr_z
            ss = '{}{:>12.3f}{:>8.3f}{:>8.3f}{}{}'.format(init, n_x, n_y, n_z, end, "\n")
            out.writelines(ss)
        else:
            out.writelines(line)
            
def separate_DNA_Prot(filename, prot_file, DNA_file):
    prot = open(prot_file, 'w')
    dna = open(DNA_file, 'w')
    num_lines = sum(1 for _ in open(filename))
    print(num_lines)
    for i in range(1, 5426):
        line = linecache.getline(filename, i)
        prot.writelines(line)
    for j in range(5426, num_lines+1):
        line = linecache.getline(filename, j)
        dna.writelines(line) 
        
def renumber_DNA(file, outfl):
    num = sum(1 for _ in open(file))
    res_max = int(linecache.getline(file, num-1)[22:26])
    count = 1
    out = open(outfl, 'w')
    for i in range(num, 0, -1):
        line = linecache.getline(file, i)
        if line.startswith('ATOM'):
            start = line[0:4]
            at = int(line[4:11])
            mid = line[11:22]
            res = int(line[22:26])
            end = line[26:-1]
            new_res = res_max + 1 -res
            new_at = count
            ss = '{}{:>7d}{}{:>4d}{}{}'.format(start, new_at, mid, new_res, end, '\n')
            out.writelines(ss)
            count = count + 1
        else:
            print(line)
            
def combine_DNA(file1, file2, outfl):
    num1 = sum(1 for _ in open(file1))
    num2 = sum(1 for _ in open(file2))
    print(num1, num2)
    out = open(outfl, 'w')
    for i in range(1, num1+1):
        line = linecache.getline(file1, i)
        if line.startswith('ATOM'):
            out.writelines(line)
        else:
            print(line)
    atnum1 = int(linecache.getline(file1, num1-1)[4:11])
    resnum1 = int(linecache.getline(file1, num1-1)[22:26])
    for j in range(1, num2+1):
        line = linecache.getline(file2, j)
        if line.startswith('ATOM'):
            start = line[0:4]
            at = int(line[4:11])
            mid = line[11:22]
            res = int(line[22:26])
            end = line[26:-1]
            n_at = atnum1+j
            n_res = res + resnum1 - 1
            ss = '{}{:>7d}{}{:>4d}{}{}'.format(start, n_at, mid, n_res, end, '\n')
            out.writelines(ss)
        else:
            print(ss)
            
def combine_protein(file1, file2, outfl):
    num1 = sum(1 for _ in open(file1))
    num2 = sum(1 for _ in open(file2))
    out = open(outfl, 'w')
    for i in range(1, num1+1):
        line = linecache.getline(file1, i)
        out.writelines(line)
    atnum1 = int(linecache.getline(file1, num1)[4:11])
    for j in range(1, num2+1):
        line = linecache.getline(file2, j)
        if line.startswith(('ATOM')):
            start = line[0:4]
            at = int(line[4:11])
            mid = line[11:20]
            chain = line[20:22]
            end = line[22:-1]
            n_at = atnum1+j
            if chain==' A':
                n_ch = ' D'
            if chain==' B':
                n_ch = ' E'
            if chain==' C':
                n_ch = ' F'
            ss = '{}{:>7d}{}{:>2s}{}{}'.format(start, n_at, mid, n_ch, end, '\n')
            out.writelines(ss)
        if line.startswith(('TER')):
            start = line[0:4]
            at = int(line[4:11])
            mid = line[11:20]
            chain = line[20:22]
            end = line[22:-1]
            n_at = atnum1+j
            if chain==' A':
                n_ch = ' D'
            if chain==' B':
                n_ch = ' E'
            if chain==' C':
                n_ch = ' F'
            ss = '{}{:>7d}{}{:>2s}{}{}'.format(start, n_at, mid, n_ch, end, '\n')
            out.writelines(ss)
            
def combine_protein_DNA(file1, file2, outfl):
    num1 = sum(1 for _ in open(file1))
    num2 = sum(1 for _ in open(file2))
    out = open(outfl, 'w')
    for i in range(1, num1+1):
        line = linecache.getline(file1, i)
        out.writelines(line)
    atnum1 = int(linecache.getline(file1, num1)[4:11])

    for j in range(1, num2+1):
        line = linecache.getline(file2, j)
        if line.startswith(('ATOM')):
            start = line[0:4]
            at = int(line[4:11])
            mid = line[11:20]
            chain = line[20:22]
            end = line[22:-1]
            n_at = atnum1+j
            if chain==' D':
                n_ch = ' G'
            ss = '{}{:>7d}{}{:>2s}{}{}'.format(start, n_at, mid, n_ch, end, '\n')
            out.writelines(ss)
        else:
            out.writelines(line)
            
folder='/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/PDB.FILES/'
#filename1=folder+'RPA_dna_50_b.pdb'
#filename2=folder+'RPA_dna_50_a.pdb'
#rotate_filename=folder+'RPA_dna_50a_rotate.pdb'
#trans_rot_filename=folder+'RPA_dna_50a_rot_trans.pdb'

filename1=folder+'RPA_dna_50_a.pdb'
filename2=folder+'RPA_dna_50_b.pdb'
rotate_filename=folder+'RPA_dna_50a_rotate.pdb'
trans_rot_filename=folder+'RPA_dna_50a_rot_trans.pdb'

#filename1=folder+'RPA_dna_30.pdb'
#filename2=folder+'RPA_dna_30.pdb'
#rotate_filename=folder+'RPA_dna_30_rotate.pdb'
#trans_rot_filename=folder+'RPA_dna_30_rot_trans.pdb'

x1, y1, z1 = get_coord(filename2, 5444)
#x2, y2, z2 = get_coord(filename1, 6419)
#x2, y2, z2 = get_coord(filename1, 6020)
x2, y2, z2 = get_coord(filename1, 6229)

l, m, n = direction_cosines(x1, y1, z1, x2, y2, z2)
#rotate_PDB(filename2, l, m, n, rotate_filename)

x1, y1, z1 = get_coord(filename1, 5444)
x2, y2, z2 = get_coord(rotate_filename, 6229)

dx, dy, dz = distance(x2, y2, z2, x1, y1, z1)

#translate_PDB(rotate_filename, dx+0.1, dy+0.1, dz+0.1, trans_rot_filename)

rpa1=folder+'RPAf_1a.pdb'
dna1=folder+'DNAf_1a.pdb'
rpa2=folder+'RPAf_2a.pdb'
dna2=folder+'DNAf_2a.pdb'

separate_DNA_Prot(trans_rot_filename, rpa1, dna1)
separate_DNA_Prot(filename1, rpa2, dna2)

comb_dna=folder+'combinedfa_DNA.pdb'
comb_rpa=folder+'combinedfa_RPA.pdb'
combined=folder+'combinedfa_str_100_f.pdb'

combine_DNA(dna1, dna2, comb_dna) 
combine_protein(rpa1, rpa2, comb_rpa) 
combine_protein_DNA(comb_rpa, comb_dna, combined) 
 

