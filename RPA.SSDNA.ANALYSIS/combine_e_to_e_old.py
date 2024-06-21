#!/bin/python

import numpy as np

all_val=[]

for i in range(1,10):
    try:
        name="end_dis_00"+str(i)+".txt"
        print(name)
        data=np.loadtxt(name)
        val=data[:,1]
        valp = val[1000:]
        all_val.append(valp)
    except:
        continue

for j in range(10,20):
    try:
        name="end_dis_0"+str(j)+".txt"
        print(name)
        data=np.loadtxt(name)
        val=data[:,1]
        valp = val[1000:]
        all_val.append(valp)
    except:
        continue
    
all_val = np.concatenate(all_val)

np.savetxt('data.txt', all_val, fmt='%8.3f', delimiter='\t')

