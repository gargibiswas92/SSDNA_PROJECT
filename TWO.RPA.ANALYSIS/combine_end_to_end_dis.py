#!/bin/python

import numpy as np

all_val=[]

for i in range(1,11):
    name="end_dis_"+str(i)+".txt"
    print(name)
    try:
        data=np.loadtxt(name)
        val=data[:,1]
        valp = val[1000:]
        #val = val[val <= 95]
        all_val.append(valp)
    except:
        continue
    
all_val = np.concatenate(all_val)

np.savetxt('data.txt', all_val, fmt='%8.3f', delimiter='\t')

