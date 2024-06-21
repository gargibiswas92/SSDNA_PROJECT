#!/bin/bash

#length=(15 25 30 40 45)
#beads=(46 76 91 121 136)

length=(60 80)
beads=(181 241)

for ((i=0; i<${#length[@]}; i++)); do
    infile="/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING/DAT.FILES/dna_${length[i]}_3.dat"
    python modify_stacking_interactions.py "${infile}"
    done