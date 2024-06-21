#!/bin/bash

#length=(15 25 30 40 45 60 80 100)
#beads=(46 76 91 121 136 181 241 301)

length=(40 60 80 100)
#beads=(181 241)

for ((i=0; i<${#length[@]}; i++)); do
    infile="/home_b/gargi/project_RPA_edwin/RPA.DNA.MAKING/DAT.FILES/RPA.DNA${length[i]}_7_ch_rep_1.6.dat"
    python modify_phosphate_dihedral_RPA_dna.py "${infile}"
    done