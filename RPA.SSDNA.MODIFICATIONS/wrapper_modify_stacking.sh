#!/bin/bash

#length=(15 25 30 40 45 60 80 100)
#beads=(46 76 91 121 136)

length=(15 25 30 40 45 60 80 100)
#length=(60 80)
#beads=(181 241)

for ((i=0; i<${#length[@]}; i++)); do
    for j in 0.4 0.0
    do
        infile="/home_b/gargi/project_RPA_edwin/RPA.DNA.MAKING/DAT.FILES/RPA.DNA${length[i]}_7_ch_rep_1.6_dih_${j}.dat"
        python modify_stacking_interactions.py "${infile}"
        done
    done



