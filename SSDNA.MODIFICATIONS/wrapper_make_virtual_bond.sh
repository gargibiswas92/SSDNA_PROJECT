#!/bin/bash

length=(25 30 40 45 60 80 100)
beads=(2 11 26 32 56 86 116)

#length=(80 100)
#beads=(86 116)

for ((i=0; i<${#length[@]}; i++)); do
    for j in 0.0 0.4
    do
        infile="/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING/DAT.FILES/dna_${length[i]}_7_ch_rep_1.6_dih_${j}.dat"
        python make_one_virtual_bond.py "${infile}" "${beads[i]}"
        echo "${infile}" "${beads[i]}"
    done
done