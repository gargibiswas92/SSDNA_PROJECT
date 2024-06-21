#!/bin/bash

#length=(15 25 30 35 45)
#init_num=(103 96 93 87 81)
#end_num=(118 120 122 121 125)
length=(40 50)
init_num=(82 72)
end_num=(122 122)

#length=(40 60 80 100)
#init_num=(87 77 67 57)
#end_num=(126 136 146 156)

for ((i=0; i<${#length[@]}; i++)); do
    outfile="/home_b/gargi/project_RPA_edwin/RPA.DNA.MAKING/PDB.FILES/RPA_dna_${length[i]}_b1.pdb"
    python modify_RPA_DNA_pdb.py "${outfile}" "${init_num[i]}" "${end_num[i]}"
    done