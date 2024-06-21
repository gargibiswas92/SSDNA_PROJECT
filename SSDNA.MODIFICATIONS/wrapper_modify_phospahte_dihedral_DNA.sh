#!/bin/bash

#length=(15 25 30 40 45 60 80 100)
beads=(46 76 91 121 136 181 241 301)

length=(25 30 40 45 60)
#beads=(181 241)

for ((i=0; i<${#length[@]}; i++)); do
    infile="/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING/DAT.FILES/dna_${length[i]}_rep_1.6_bond.dat"
    python modify_phosphate_dihedral_DNA.py "${infile}"
    done