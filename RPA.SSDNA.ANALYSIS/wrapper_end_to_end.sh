#!/bin/bash


length=(15 25 30 40 45 60 80 100)
beads=(1384 1414 1429 1459 1474 1519 1579 1639)


for ((i=0; i<${#length[@]}; i++)); do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/RPA.DNA.SIMULATIONS/RPA.DNA_${length[i]}_RAD_1.6_DIH_${j}_STACKSA_05"
		cd "${folder}"/output/Traj/
		rm -rf end_dis*
		cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/RPA.SSDNA.ANALYSIS/calculate_end_to_end.py .
		#cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/RPA.SSDNA.ANALYSIS/e_to_e.f .
		end_bead="${beads[i]}"
		end_phosphate="$((beads[i] - 2))"
		sed -i "s/500/"${end_phosphate}"/g" calculate_end_to_end.py
		sed -i "s/2000/"${end_bead}"/g" calculate_end_to_end.py
		python calculate_end_to_end.py
	done
done
	
