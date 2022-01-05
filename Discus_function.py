#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def discus_func(x_local):
    D=x_local.size     # size of Numpy vector x_local
    discus = pow(x_local[0],2)*pow(10,6)
    for i in range(1,D):
        x_i=x_local[i]
        discus += pow(x_local[i],2)
    return discus


x_local=np.array([2,3,4,5])
b=discus_func(x_local)
print (b)


# In[ ]:




