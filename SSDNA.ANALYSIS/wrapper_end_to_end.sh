#!/bin/bash


length=(25 30 40 45 60 80 100)
beads=(76 91 121 136 181 241 301)

#length=(80 100)
#beads=(241 301)

for ((i=0; i<${#length[@]}; i++)); do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/DNA.SIMULATIONS/DNA_${length[i]}_RAD_1.6_DIH_${j}_BOND_ST"
		cd "${folder}"/output/Traj/
		rm -rf end_dis*
		cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/SSDNA.ANALYSIS/calculate_end_to_end.py .
		end_bead="${beads[i]}"
		end_phosphate="$((beads[i] - 2))"
		sed -i "s/1000/"${end_phosphate}"/g" calculate_end_to_end.py
		sed -i "s/2000/"${end_bead}"/g" calculate_end_to_end.py
		python calculate_end_to_end.py
	done
done
	
