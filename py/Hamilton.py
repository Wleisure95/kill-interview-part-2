#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:12:41 2019

@author: leisure
"""

import numpy as np
f=np.full((1<<5,5),1000)
w=np.array([[0,2,4,5,1],[2,0,6,5,3],[4,6,0,8,3],[5,5,8,0,5],[1,3,3,5,0]])
f[1][0]=0
for i in range(1,1<<5):
    for j in range(0,5):
        if(i>>j&1):
            for k in range(5):
                if(i-(1<<j)>>k&1):
                    print(i,j)
                    f[i][j] = min(f[i][j],f[i-(1<<j)][k]+w[k][j])
                    print(f[i][j])