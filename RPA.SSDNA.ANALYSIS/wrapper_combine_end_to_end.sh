#!/bin/bash

indeces=(100)

for i in 0; do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/RPA.DNA.SIMULATIONS/RPA.DNA_${indeces[i]}_RAD_1.6_DIH_${j}_STACKSA_05"
		cd "${folder}"/output/Traj/
		cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/RPA.SSDNA.ANALYSIS/combine_end_to_end_dis.py .
 	python combine_end_to_end_dis.py
		filename="end_to_end_RPA_stacks_N_${indeces[i]}_dih_${j}.txt"
		mv data.txt /trajectories/gargi/RPA_Ed/RESULTS.ANALYSIS/"${filename}"
	done 
done
	
