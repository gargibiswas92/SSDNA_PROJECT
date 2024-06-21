#!/bin/bash


length=(80 100)

for ((i=0; i<${#length[@]}; i++)); do
    #infile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_two_rpa_side_${length[i]}.dat"
    infile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_side_${length[i]}_fl.dat"
    python modify_repulsions.py "${infile}"
    done
