#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("data/titanic.csv")


# In[3]:


df.head()


# In[4]:


#Step 1: Data Description
         # a) Data Types
         # b) How much percentage of missing values are present
         # c) what are the statistics of the data


# In[5]:


#Data Types
df.info()


# In[8]:


#How much percentage of missing values are present
df.isna().sum()/len(df)*100


# In[9]:


#What are the statistics of the data
df.describe()


# In[10]:


# 0-25%, 25%-50%, 50%-75%, >75%


# In[11]:


# Step 2: Univariate Analysis


# In[12]:


price = df.Fare


# In[13]:


price


# In[22]:


#!pip install seaborn


# In[23]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize =(5, 3))
ax.hist(df.Fare, bins = [0, 25, 50, 75, 100])
plt.show()


# In[24]:


#Step 3: Bi-Variate Analysis


# In[28]:


fig = plt.figure(figsize = (5, 2))
 
# creating the bar plot
plt.bar(df.Survived, df.Fare,  color ='maroon',
        width = 0.4)
 
plt.xlabel("No. of Survivors")
plt.ylabel("Fare")
plt.title("Titanic Surivors with Fare")
plt.show()


# In[29]:


# Step 4: Finding Correlation between pairs of segments


# In[30]:


df.corr()     #0.6-0.9 is good


# In[31]:


plt.matshow(df.corr())
plt.show()


# In[ ]:




