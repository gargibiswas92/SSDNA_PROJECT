#!/bin/bash

indeces=(15 25 30 40 45 60 80 100)

for ((i=0; i<${#indeces[@]}; i++)); do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/RPA.DNA.SIMULATIONS/RPA.DNA_${indeces[i]}_RAD_1.6_DIH_${j}_STACKSA_05"
		cd "${folder}"/output/Traj/
		yourfile=`ls *.bz2`
		for file in ${yourfile}
		do
			echo ${file}
			bunzip2 "${file}"
		done
	done
done
	
