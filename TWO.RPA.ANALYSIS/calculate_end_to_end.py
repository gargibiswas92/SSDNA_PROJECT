import os
import numpy as np
from itertools import islice

def custom_converter(line):
    x = float(line[0:8])
    y = float(line[8:16])
    z = float(line[16:24])
    return x, y, z

idna_start = 2679
idna_end = 2000 #last bead of DNA
end_phos = 500  #last phosphate bead
chain_no = 7
skip_line = 2+chain_no+idna_end
os.system("ls Traj_*.dat > input.txt")
with open("input.txt", "r") as f:
    filenames = f.readlines()

for ifile in range(1, 11):
    filename = filenames[ifile - 1].strip()
    print(filename)
    outname='end_dis_'+str(ifile)+'.txt'
    with open(filename, "r") as f, open(outname, 'w') as out:
        for _ in range(skip_line):
            next(f)
        for step in range(10000):
            next(f)
            x_arr = np.array([])
            y_arr = np.array([])
            z_arr = np.array([])
            for _ in range(idna_end):
                line = next(f) 
                try:   
                    x, y, z = custom_converter(line)
                    x_arr = np.append(x_arr, x)
                    y_arr = np.append(y_arr, y)
                    z_arr = np.append(z_arr, z)
                except:
                    continue
            next(f)
            try:    
                dx = x_arr[idna_start] - x_arr[end_phos]
                dy = y_arr[idna_start] - y_arr[end_phos]
                dz = z_arr[idna_start] - z_arr[end_phos]
            
                dist = np.sqrt(dx**2+dy**2+dz**2)
            except:
                dist = 0.0
                
            ss = '{:>12d}{:>10.3f}{}'.format(step, dist, '\n')
            out.writelines(ss)
        out.close()
                

os.remove("input.txt")