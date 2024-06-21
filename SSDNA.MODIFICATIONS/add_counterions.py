#!/bin/python
import numpy as np
import linecache
import os

def calc_read_sections(filename):
    string1='stacks'
    string2='bonded'
    string3='angle'
    string4='dihedral'
    string5='contacts'
    string6='repulsions'
    string7='electrostatic'
    string8='atom'
    string9='chains.'
    sections = [string1, string2, string3, string4, string5, string6, string7, string8, string9]
    sec_line_num = []
    end_line = sum(1 for _ in open(filename))
    for item in sections:
        item_line = next((i+1 for i, line in enumerate(open(filename)) if item in line), None)
        sec_line_num.append(item_line)

    num_item_each_sect = []
    for item1 in sec_line_num:
        sect_line = linecache.getline(filename, item1)
        sect_line_arr = sect_line.split()
        num_sect = int(sect_line_arr[0])
        num_item_each_sect.append(num_sect)
    return num_item_each_sect, sec_line_num, end_line

def write_new_dat_file(old_filename, new_file, num_it_each_sect, sec_line_num, end_line, rep_file, elec_file, coord_file):
    unaltered = sec_line_num[4]
    for i in range(1, unaltered+1):
        line = linecache.getline(old_filename, i)
        new_file.writelines(line)
        
    rep_num = sum(1 for _ in open(rep_file))
    new_rep_num = num_it_each_sect[5]+rep_num
    rep_line='{:7d} repulsions{}'.format(new_rep_num, '\n')
    new_file.writelines(rep_line) 
    for i in range(sec_line_num[5]+1, sec_line_num[6]):
        line = linecache.getline(old_filename, i)
        new_file.writelines(line)
    for i in range(1, rep_num+1):
        line = linecache.getline(rep_file, i)
        new_file.writelines(line)
        
    elec_num = sum(1 for _ in open(elec_file))
    new_elec_num = num_it_each_sect[6]+elec_num
    elec_line='{:7d} electrostatic residues.{}'.format(new_elec_num, '\n')
    new_file.writelines(elec_line) 
    for i in range(sec_line_num[6]+1, sec_line_num[7]):
        line = linecache.getline(old_filename, i)
        new_file.writelines(line)
    for i in range(1, elec_num+1):
        line = linecache.getline(elec_file, i)
        new_file.writelines(line)
        
    atom_num = sum(1 for _ in open(coord_file))
    new_atom_num = num_it_each_sect[7]+atom_num
    atom_line='{:10d} atom positions.{}'.format(new_atom_num, '\n')
    new_file.writelines(atom_line)
     
    new_chain_num = num_it_each_sect[8]+1
    chain_line='{:10d} chains.{}'.format(new_chain_num, '\n')
    new_file.writelines(chain_line)
    for i in range(sec_line_num[8]+1, sec_line_num[8]+num_it_each_sect[8]+1):
        line = linecache.getline(old_filename, i)
        new_file.writelines(line)
    count_chain_line='{:10d} is the size of chain{:>8d}.{}'.format(atom_num, new_chain_num, '\n')
    new_file.writelines(count_chain_line)
    
    for i in range(sec_line_num[8]+num_it_each_sect[8]+1, end_line+1):
        line = linecache.getline(old_filename, i)
        new_file.writelines(line)
    for i in range(1,atom_num+1):
        line = linecache.getline(coord_file, i)
        new_file.writelines(line)
    new_file.close()

def calc_counterions(end_bead):
    init = 2
    count = 0
    for i in range(init, end_bead+1,3):
#        print(i)
        count = count + 1
    return count

def read_dat_file(filename):
    string1 = 'CA'
    ca_line = next((i+1 for i, line in enumerate(open(filename)) if string1 in line), None)
    end_line = sum(1 for _ in open(filename))
    end_L = linecache.getline(filename, end_line)
    end_res = int(end_L[0:5])
    
    coords = []
    for i in range(ca_line, end_line):
        line = linecache.getline(filename, i)
        x, y, z = float(line[16:24]), float(line[24:32]), float(line[32:40])
        coords.append((x, y, z))
        coords1 = np.array(coords)
    return coords1, end_res
        

def generate_unoccupied_points(coordinates, box_size, n_points, max_attempts=100):
   min_distance = 5.0
   unoccupied_points = []
   for p in range(n_points):
       for _ in range(max_attempts):
           point = list(np.random.rand(3) * box_size)
           too_close = False
           
           for atom_coord in coordinates:
               distance = np.linalg.norm(point - atom_coord)
               if distance < min_distance:
                   too_close = True
                   break
           
           if not too_close:
               unoccupied_points.append(point)
               break 
       
       if len(unoccupied_points) < p + 1:
           print(f"Max attempt to find a suitable point extended. Increase max attempt (current: {max_attempts}) or reduce min distance (current: {min_distance})")
           break
   return np.array(unoccupied_points)

def write_coordinates(ion_array, end_res, out):
    val = 1.000
    count = 1
    restype = 'C'
    res = 'CA'
    for i in range(len(ion_array)):
        resnum = end_res + count
        ss= '{:>5d}{:>4d}{:>3s}{:>4s}{:>8.3f}{:>8.3f}{:>8.3f}{:>8.3f}{}'.format(resnum, resnum, res, restype, ion_array[i][0], ion_array[i][1], ion_array[i][2],val, '\n')
        out.writelines(ss)
        count = count + 1


def write_electrostatics(init_num, end_res, num, out):
    val = 2.000
    for i in range(num):
        resnum = end_res + i + 1
        num = init_num + i + 1
        ss = '{:>8d}{:>5d}{:>8.3f}{}'.format(num, resnum, val, '\n')
        out.writelines(ss)

    
def write_repulsions(init_num, end_res, num, out):
    count = 1
    val = 1.0
    sigma = 16.0
    for j in range(end_res+1, end_res+num+1):
        for i in range(1, end_res+num+1):
            if i !=j:
                rep_num = init_num + count
                ss = '{:>8d}{:>5d}{:>5d}{:>10.3f}{:>10.3f}{}'.format(rep_num, j, i, sigma, val, '\n')
                out.writelines(ss)
                count = count + 1

    
    
#list_dat = ['dna_15_0.dat', 'dna_25_0.dat', 'dna_30_0.dat', 'dna_45_0.dat'] 
#list_dat_mod = ['dna_15_0_coun.dat', 'dna_25_0_coun.dat', 'dna_30_0_coun.dat', 'dna_45_0_coun.dat']

list_dat = ['dna_25_0.dat'] 
list_dat_mod = ['dna_25_0_coun.dat']  

folder='/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING'

for item, item1 in zip(list_dat, list_dat_mod):
    crd, num = read_dat_file(item)
    num_a, line_num, end_line = calc_read_sections(item)
    count_num = calc_counterions(num)
    ca_num = int(count_num/2)
    point_crd = generate_unoccupied_points(crd, 30, ca_num, max_attempts=100)
    
    out = open('testfile.txt', 'w')
    out1 = open('testfile_el.txt', 'w')
    out2 = open('testfile_rep.txt', 'w')
    out3 = open(item1, 'w')
    
    write_coordinates(point_crd, num, out)
    write_electrostatics(num_a[6], num,ca_num, out1)
    write_repulsions(num_a[5], num, ca_num, out2)
    
    print(num_a[7], num_a[5], num_a[6], ca_num)
    out.close()
    out1.close()
    out2.close()
    write_new_dat_file(item, out3, num_a, line_num, end_line, 'testfile_rep.txt', 'testfile_el.txt', 'testfile.txt')
    
    file_path3 = "/home_b/gargi/project_RPA_edwin/MDRUN/ONLY.DNA.MODIFICATIONS/ADD.COUNTERIONS/testfile_rep.txt" 
    file_path1 = "/home_b/gargi/project_RPA_edwin/MDRUN/ONLY.DNA.MODIFICATIONS/ADD.COUNTERIONS/testfile.txt"
    file_path2 = "/home_b/gargi/project_RPA_edwin/MDRUN/ONLY.DNA.MODIFICATIONS/ADD.COUNTERIONS/testfile_el.txt"

    for item2 in [file_path1, file_path2, file_path3]:
        if os.path.exists(item2):
            os.remove(item2)
        else:
            print("The file does not exist")
    
    out3.close()