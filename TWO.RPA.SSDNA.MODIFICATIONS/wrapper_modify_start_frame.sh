#!/bin/bash

#length=(15 25 30 40 45)
#beads=(46 76 91 121 136)

length=(80)
#beads=(181 241 301)

for ((i=0; i<${#length[@]}; i++)); do
    for j in 0.4
    do
        datfile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_two_rpa_side_${length[i]}_ch_rep_1.6_dih_${j}_stacks_A.dat"
        pdbfile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/MAKING.CG/two_rpa_face_${length[i]}.dat.pdb"
        python modify_starting_frame.py "${datfile}" "${pdbfile}"
    done
done