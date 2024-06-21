#!/bin/bash


length=(80 100)

for ((i=0; i<${#length[@]}; i++)); do
    #infile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_two_rpa_side_${length[i]}_ch_rep_1.6.dat"
    infile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_side_${length[i]}_fl_ch_rep_1.6.dat"
    python modify_phosphate_dihedral_RPA_dna.py "${infile}"
    done