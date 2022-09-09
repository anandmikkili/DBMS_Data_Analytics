#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Why we need Numpy?

# In[4]:


import pandas as pd
df = pd.DataFrame(columns=['Age','Score'])


# In[5]:


df.head()


# In[7]:


df['Age'] = np.random.randint(low=0,high=1000000,size=500000)
df['Score'] = np.random.randint(low=0,high=100,size=500000)


# In[8]:


df.shape


# In[10]:


df.head()


# In[9]:


def grade(score):
    if score>=70:
        return "A"
    elif((score>=50) and (score<70)):
        return 'B'
    elif((score>=35) and (score<50)):
        return 'C'
    else:
        return 'D'


# In[12]:


import time
start_for = time.time()
df['Grade']='F'
for i,r in df.iterrows():
    df.at[i,'Grade'] = grade(r.Score)
end_for = time.time()
print("Total Time Taken By ForLoop: ", (end_for - start_for), "Seconds")
df.head()


# In[13]:


df.drop(columns=['Grade'],inplace=True)
df.head()


# In[14]:


start_lambda = time.time()
df['Grade'] = df.apply(lambda r: grade(r.Score), axis=1)
end_lambda = time.time()
print("Total Time Taken By Lambda Function to Execute: ",(end_lambda - start_lambda), "Seconds")


# In[15]:


df.drop(columns=['Grade'],inplace=True)
df.head()


# In[16]:


start_npv = time.time()
df['Grade'] = np.vectorize(grade)(df.Score)
end_npv = time.time()
print("Total Time Taken By Lambda Function to Execute: ",(end_npv - start_npv), "Seconds")


# In[17]:


df.head()


# In[18]:


#1D
a = np.array([1,2,3,4,5,6,7,8,9,0,-1,-2,-3,-4,-5])


# In[19]:


type(a)


# In[20]:


#Retrieve elements from 1D
a[0]


# In[21]:


#Iteration over 1D
for i in a:
    print(i)


# In[22]:


#Slicing on 1D Array
a1 = a[2:7:1]
a1


# In[23]:


a1 = a[2:7:2]
a1


# In[24]:


a1 = a[2:7:3]
a1


# In[26]:


x=[0,5,9]
a2 = a[x]
a2


# In[27]:


#2D Arrays


# In[29]:


a = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
a


# In[31]:


#fetching elements
a[(1,2)]


# In[32]:


#iteration
for i in a:
    for j in i:
        print(j)


# In[33]:


#Slicing on 2D Array
a1 = a[1:3:1, 0:2:1]
a1


# Arithmetic Operations on Arrays

# In[34]:


a = np.array([1,2,3,4,5])
print(a+2)


# In[35]:


print(a-2)


# In[36]:


a = a+10
print(a//3)


# In[37]:


print(a**2)


# In[38]:


#Arrays to Arrays Operations
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = a*b
c


# Mathematical Operations

# In[39]:


c = np.dot(a,b)
c


# Data Type Conversions

# In[45]:


a = np.array([1,0,2,3,4])
a.dtype


# In[46]:


a = a.astype('int16')


# In[47]:


a.dtype


# In[48]:


a = a.astype('bool')


# In[49]:


a


# In[50]:


a.dtype


# In[ ]:




