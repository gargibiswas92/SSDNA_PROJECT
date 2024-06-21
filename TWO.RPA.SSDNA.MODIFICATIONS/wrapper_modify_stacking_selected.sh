#!/bin/bash

#      **********60 nucleotide DNA***********
#length=(side face)
#init1=(2679 2685)
#end1=(2745 2757)
#init2=(2775 2775)
#end2=(2844 2838)
#length=(60)
#init1=(2679)
#end1=(2745)
#init2=(2775)
#end2=(2844)
#       ******face-to-face RPA*******
#length=(80 100)
#init1=(2697 2697)
#end1=(2763 2763)
#init2=(2841 2901)
#end2=(2913 2973)
#       **********side-by-side RPA *******
length=(80 100)
init1=(2691 2691)
end1=(2763 2763)
init2=(2841 2901)
end2=(2913 2973)

for ((i=0; i<${#length[@]}; i++)); do
    for j in 0.4 0.0
    do
        #infile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_two_rpa_${length[i]}_ch_rep_1.6_dih_${j}.dat"
        infile="/home_b/gargi/project_RPA_edwin/TWO.RPA.MAKING/DAT.FILES/add_side_${length[i]}_fl_ch_rep_1.6_dih_${j}.dat"
        python modify_stacking_interactions_selected.py "${infile}" "${init1[i]}" "${end1[i]}" "${init2[i]}" "${end2[i]}"
        done
    done



