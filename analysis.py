# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 01:36:22 2020

@author: ishan
"""

import matplotlib.pyplot as plt
import json
import numpy as np
tasks=["RR_Tasks.txt","Random_Tasks.txt","LL_Tasks.txt"]
jobs=["RR_Jobs.txt","Random_Jobs.txt","LL_Jobs.txt"]
for temp in range(len(tasks)):
        print(tasks[temp][:tasks[temp].index("_")])    
        print("Task:")
        with open(tasks[temp],"r") as f:
            totaltask=json.loads(f.read())
            finaltasks=[totaltask[task] for task in totaltask]
            alltasks=sorted(finaltasks)
            if len(alltasks)%2 != 0:
                taskmedian=alltasks[int((len(alltasks)+1)/2)]
                taskmean=sum(alltasks)
                taskmean/=len(alltasks)
                
                print("mean :",round(taskmean,5))
                print("median :",round(taskmedian,5))
            else:
                taskmedian=alltasks[int(len(alltasks)/2)]
                taskmedian+=alltasks[int((len(alltasks)/2)+1)]
                taskmedian/=2
                taskmean=sum(alltasks)
                taskmean/=len(alltasks)
                #print(tasks[temp][:tasks[temp].index("_")])
                print("mean :",round(taskmean,5))
                print("median :",round(taskmedian,5))
    
        print("Job:")
        with open(jobs[temp],"r") as f:
            totaljob=json.loads(f.read())
            finaljobs=[totaljob[job] for job in totaljob]
            alljobs=sorted(finaljobs)
            if len(alljobs)%2 != 0:
                jobmedian=alljobs[int((len(alljobs)+1)/2)]
                jobmean=sum(alljobs)
                jobmean/=len(alljobs)
                print("mean :",round(jobmean,5))
                print("median :",round(jobmedian,5))
            else:
                jobmedian=alljobs[int(len(alljobs)/2)]
                jobmedian+=+alljobs[int((len(alljobs)/2)+1)]
                jobmedian/=2
                jobmean=sum(alljobs)
                jobmean/=len(alljobs)
                print("mean :",round(jobmean,5))
                print("median :",round(jobmedian,5))
                
                        
        
        print("\n")
        
        
files=['RR_Log.txt','Random_Log.txt','LL_Log.txt']
time=[]
for k in files:
    with open(k,"r") as f:
            time.append(json.load(f))
    x=[float(i) for i in time[0]]
    array=np.array(list(time[0].values()))
    plt.figure(figsize = (20,20))
    plt.plot(x,array.T[0])
    plt.plot(x,array.T[1])
    plt.plot(x,array.T[2])
    plt.xlabel('Time (in seconds)')
    plt.ylabel('No. of tasks')
    plt.legend(['Worker 1','Worker 2','Worker 3'])
    plt.grid()
    plt.show()
