#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#!pip install pandas   #To install pandas on notebook


# Creating Series Object

# In[ ]:


# List, Dictionary, Tuple, Set


# In[7]:


d = [10,20,30,40]
s = pd.Series(data=d)
s


# In[6]:


type(s)


# In[8]:


d = [10,20,30,40]
s = pd.Series(data=d, index=['a','b','c','d'])
s


# In[12]:


s['a']   #To get a value at a perticular index from Series 


# In[14]:


d = {'Kanishaka':10,'Ruchika':20, 'Sahithi':30,'Amith':40}
s = pd.Series(data=d)
s


# In[16]:


s['Kanishaka']


# In[17]:


d = (10,20,30,40)
s = pd.Series(data=d)
s


# Slicing in Pandas Series

# In[18]:


s[0:2]


# In[19]:


s[1:3]


# In[21]:


s[-3:-1]


# Attributes of Pandas Series

# In[22]:


d = ['Kanishka', 10,20.5, 10+20j, True]
s = pd.Series(data=d)


# In[24]:


s.dtype


# In[25]:


d = [10.5,20.5,30.5,40.5]
s = pd.Series(data=d)
s.dtype


# In[26]:


d = [10,20,30,40]
s = pd.Series(data=d)
s.dtype


# In[27]:


d = ['a','b','c','d']
s = pd.Series(data=d)
s.dtype


# In[28]:


d = [True, False, True, False,True]
s = pd.Series(data=d)
s.dtype


# In[29]:


d = [10+20j,20+30j,30+40j,40+50j]
s = pd.Series(data=d)
s.dtype


# In[30]:


s.shape


# In[31]:


s.size


# In[32]:


s.values


# Functions of Pandas Series Object

# In[33]:


s.memory_usage()


# Scalar Operations on Pandas Series

# In[41]:


s = pd.Series([10,20,30,40])
s = s+5
s


# In[42]:


s = pd.Series([10,20,30,40])
s = s*5
s


# In[43]:


s = pd.Series([10,20,30,40])
s = s//3
s


# Object Operations in Pandas Series

# In[44]:


s1 = pd.Series([10,20,30,40])
s2 = pd.Series([40,30,20,10])
s3 = s1+s2
s3


# In[45]:


s3 = s1.add(s2)
s3


# In[46]:


s3.pop(0)
s3


# Statistical Operation on Pandas Series Object

# In[47]:


s = pd.Series([10,20,30,40])


# In[48]:


s.mean()


# In[49]:


s.mode()


# In[50]:


s.nlargest(2)


# In[51]:


s.nsmallest(2)


# In[52]:


s1 = pd.Series([10,20,30,40,10,20,40,40,30,30,30,20])


# In[53]:


s1.unique()


# In[54]:


s1.nunique()


# In[ ]:




