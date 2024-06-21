#!/bin/bash


#length=(60 80 100)
#beads=(2855 2921 2981)

length=(80 100)
beads=(2918 2978)

for ((i=0; i<${#length[@]}; i++)); do
	for j in 0.0 0.4
	do
		folder="/home_b/gargi/project_RPA_edwin/TWO.RPA.SIMULATIONS/TWO.RPA_face_${length[i]}_fl_RAD_1.6_DIH_${j}_STACKSA"
		cd "${folder}"/output/Traj/
		rm -rf end_dis*
		cp /trajectories/gargi/RPA_Ed/CODE.REPOSITORY/TWO.RPA.ANALYSIS/calculate_end_to_end.py .
		end_bead="${beads[i]}"
		end_phosphate="$((beads[i] - 2))"
		sed -i "s/500/"${end_phosphate}"/g" calculate_end_to_end.py
		sed -i "s/2000/"${end_bead}"/g" calculate_end_to_end.py
		python calculate_end_to_end.py
	done
done
	
