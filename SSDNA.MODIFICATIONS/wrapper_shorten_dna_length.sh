#!/bin/bash

#length=(15 25 30 40 45)
#beads=(46 76 91 121 136)

length=(60 80 100)
beads=(181 241 301)

for ((i=0; i<${#length[@]}; i++)); do
    outfile="/home_b/gargi/project_RPA_edwin/ONLY.DNA.MAKING/DAT.FILES/dna_${length[i]}_7.dat"
    python shorten_dna_length.py "${beads[i]}" "${outfile}"
    done