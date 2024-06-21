#!/bin/bash

indeces=(80 100)

for i in 0 1; do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/TWO.RPA.SIMULATIONS/TWO.RPA_face_${indeces[i]}_fl_RAD_1.6_DIH_${j}_STACKSA"
		#folder="/home_b/gargi/project_RPA_edwin/TWO.RPA.SIMULATIONS/TWO.RPA_side_RAD_1.6_DIH_${j}_STACKSA"
		cd "${folder}"/output/Traj/
		cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/TWO.RPA.ANALYSIS/combine_end_to_end_dis.py .
 	python combine_end_to_end_dis.py
		filename="end_to_end_TWO_RPA_stacks_face_fl_${indeces[i]}_dih_${j}.txt"
		mv data.txt /trajectories/gargi/RPA_Ed/RESULTS.ANALYSIS/"${filename}"
	done 
done
	
