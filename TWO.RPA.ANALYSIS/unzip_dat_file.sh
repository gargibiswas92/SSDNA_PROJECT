#!/bin/bash

indeces=(80 100)

for ((i=0; i<${#indeces[@]}; i++)); do
	for j in 0.0 0.4
	do
		for t in face
		do
			folder="/home_b/gargi/project_RPA_edwin/TWO.RPA.SIMULATIONS/TWO.RPA_${t}_${indeces[i]}_fl_RAD_1.6_DIH_${j}_STACKSA"
			cd "${folder}"/output/Traj/
			yourfile=`ls *.bz2`
			for file in ${yourfile}
			do
				echo ${file}
				bunzip2 "${file}"
			done
		done
	done
done
	
