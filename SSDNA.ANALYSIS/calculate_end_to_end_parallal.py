import os
import numpy as np
from itertools import islice
from multiprocessing import Pool


def process_chunk(chunk, idna_start, end_phos):
    results = []
    x_arr = np.array([])
    y_arr = np.array([])
    z_arr = np.array([])
    for line in chunk:
        try:
            x = float(line[0:8])
            y = float(line[8:16])
            z = float(line[16:24])
        except:
            continue
        x_arr = np.append(x_arr, x)
        y_arr = np.append(y_arr, y)
        z_arr = np.append(z_arr, z)
    dx = x_arr[idna_start] - x_arr[end_phos]
    dy = y_arr[idna_start] - y_arr[end_phos]
    dz = z_arr[idna_start] - z_arr[end_phos]      
    dist = np.sqrt(dx**2+dy**2+dz**2)
    results.append(dist)
    return results

def main():
    idna_start = 1340
    idna_end = 2000 #last bead of DNA
    end_phos = 1000  #last phosphate bead
    chain_no = 4
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
                chunk_size=end_phos
            for step in range(10000):
                next(f)
                chunks = []
                chunk = f.read(chunk_size)
                chunks.append(chunk)
                next(f)
                with Pool() as pool:
                    results = pool.starmap(process_chunk, [(chunk, idna_start, end_phos) for chunk in chunks])
            final_result = []
            for chunk_results in results:
                final_result.extend(chunk_results)
            
            for j in range(len(final_result)):
                ss = '{:>12d}{:>10.3f}{}'.format(j*1000, final_result[j], '\n')
                out.writelines(ss)
            out.close()
                

os.remove("input.txt")