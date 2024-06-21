#!/bin/bash



length=(15 25 30 40 45 60 80 100)
init=(1340 1340 1340 1358 1367 1388 1418 1448)
end=(1384 1414 1429 1441 1447 1471 1501 1531)

#length=(40)
#init=(1358)
#end=(1441)


for ((i=0; i<${#length[@]}; i++)); do
    for j in 0.4 0.0
    do
        infile="/home_b/gargi/project_RPA_edwin/RPA.DNA.MAKING/DAT.FILES/RPA.DNA${length[i]}_7_ch_rep_1.6_dih_${j}.dat"
        python modify_stacking_interactions_selected.py "${infile}" "${init[i]}" "${end[i]}"
        done
    done



