#!/bin/bash

indeces=(15 25 30 40 45 60 80)
#indeces=(80 100)
#indeces=("40_7_CH_REP_

for i in 0 1 2 3 4 5 6; do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/DNA.SIMULATIONS/DNA_${indeces[i]}_RAD_1.6_DIH_${j}_BOND_ST"
		cd "${folder}"/output/Traj/
		cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/SSDNA.ANALYSIS/combine_end_to_end_dis.py .
 	python combine_end_to_end_dis.py
		filename="end_to_end_${indeces[i]}_dih_${j}_bond_st.txt"
		mv data.txt /trajectories/gargi/RPA_Ed/RESULTS.ANALYSIS/"${filename}"
	done
done
	
