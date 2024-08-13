#!/usr/bin/env python
# coding: utf-8

# In[180]:


print("Hello World")


# In[181]:


import numpy as np


# In[182]:


arr = np.array([[1,2,3],[4,5,6]])


# In[183]:


print(arr)


# In[184]:


type(arr)


# In[185]:


print(arr.ndim)


# In[186]:


print(arr.shape)


# In[187]:


print(arr.size)


# In[188]:


print(arr.dtype)


# In[189]:


arr.dtype


# In[190]:


arr.size


# In[191]:


a = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[192]:


a


# In[193]:


a.size


# In[194]:


a.shape


# In[195]:


c = np.zeros((3,4))


# In[196]:


c


# In[197]:


c.dtype


# In[198]:


np.ones((4,4))


# # np.eye(4)

# In[200]:


np.arange(0, 30, 4)


# In[201]:


np.linspace(0, 30, 4)


# In[202]:


np.linspace(0,5,10)


# In[203]:


a = np.array([[1,2,3,4],[4,5,6,5],[7,8,9,5]])
new_arr = a.reshape((4,3))


# In[204]:


new_arr


# In[205]:


new_arr.flatten()


# In[206]:


new_arr[1:,:3]


# In[207]:


new_arr


# In[208]:


new_arr[2:,:3]


# In[209]:


new_arr[:,:-1]


# In[210]:


cond = new_arr>5


# In[211]:


cond


# In[212]:


new_arr


# In[213]:


new_arr+1


# In[214]:


new_arr-1


# In[215]:


new_arr


# In[216]:


new_arr*3


# In[217]:


new_arr/2


# In[218]:


new_arr.T


# In[219]:


new_arr.max()


# In[220]:


new_arr.max(axis = 1)


# In[221]:


new_arr.max(axis = 0)


# In[222]:


new_arr.min(axis = 1)


# In[223]:


np.sort(new_arr, axis = None)


# In[224]:


np.sort(new_arr, axis = 0)


# In[225]:


np.sort(new_arr, axis = 1)


# In[226]:


np.sort(new_arr, axis = 0,kind = "mergesort")


# In[227]:


new_arr


# In[228]:


np.sort(new_arr, axis = 1,kind = "mergesort")


# In[229]:


ar1 = np.array([[1,2],[2,3]])
ar2 = np.array([[4,5],[6,7]])


# In[230]:


np.vstack((ar1,ar2))


# In[231]:


np.hstack((ar1,ar2))


# In[232]:


np.row_stack((ar1,ar2))


# In[233]:


arr1 = np.column_stack((ar1,ar2))


# In[234]:


arr1


# In[235]:


arr1[0]


# In[236]:


np.concatenate((ar1,ar2),1)


# In[237]:


np.hsplit(arr1,2)


# In[238]:


np.min(arr1)


# In[239]:


np.max(arr1)


# In[240]:


np.mean(arr1)


# In[241]:


np.median(arr1)


# In[242]:


np.average(arr1)


# In[ ]:




