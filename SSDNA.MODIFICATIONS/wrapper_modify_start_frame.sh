#!/bin/bash

#length=(15 25 30 40 45)
#beads=(46 76 91 121 136)

length=(25 30 40 45 60 80 100)
#beads=(181 241 301)

for ((i=0; i<${#length[@]}; i++)); do
    for j in 0.0 0.4
    do
        datfile="/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING/DAT.FILES/dna_${length[i]}_7_ch_rep_1.6_dih_${j}_bond_st.dat"
        pdbfile="/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING/PDB.FILES/dna_${length[i]}_frame_0.pdb"
        python modify_starting_frame.py "${datfile}" "${pdbfile}"
    done
done