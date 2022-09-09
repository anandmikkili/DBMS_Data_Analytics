#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# Creating DataFrame

# In[2]:


names = ['Kanishka', 'Sahithi','Bansal', 'Sibi']
eng_marks = [100,56,33,78]
hindi_marks = [87,43,23,65]
science_marks = [93,71,56,32]
social_marks = [90,54,56,78]
d = {'Student_Name':names,'English':eng_marks, 'Hindi':hindi_marks,'Science':science_marks, 'Social':social_marks}
df = pd.DataFrame(data=d)


# In[3]:


df


# Reshaping DataFrame

# In[4]:


df.shape   #returns tuple (rows, columns)


# In[5]:


#Adding New Column
df['Environmental_Science'] = pd.Series([40,50,70,80])
df


# In[6]:


#Derving a New Column out of existing Columns
df['Avg_Marks'] = (df['English']+df['Hindi']+df['Science']+df['Social']+df['Environmental_Science'])/5
df


# In[7]:


def pass_fail_status(eng,hin,sci,soc,es):
    if((eng>=35) and (hin>=35) and (sci>=35) and (soc>=35) and (es>=35)):
        return 'P'
    else:
        return 'F'


# In[10]:


#Deriving a new column out of existing by applying a function
df['STATUS'] = df.apply(lambda r: pass_fail_status(r.English,r.Hindi,r.Science,r.Social,r.Environmental_Science), axis=1)
df


# In[11]:


df.shape


# In[12]:


df.drop(columns=['Avg_Marks'], inplace=True)
#df = df.drop(columns=['Avg_Marks'])


# In[13]:


df


# In[14]:


#Rename the Column Names
df.rename(columns={'Student_Name':'Name', 'Environmental_Science':'Environmental'}, inplace=True)


# In[15]:


df


# In[16]:


#Taking Subset of a DataFrame with range of indexes
df1 = df.iloc[1:3]
df1


# In[17]:


df2 = df[df['English']>60]
df2


# In[19]:


df3 = df[ (df['English']>60) & (df['Science']>60)]
df3


# Grouping of Rows from DataFrame

# In[20]:


df


# In[22]:


df_group = df.groupby(by='STATUS')
df_group.head()


# In[25]:


df['Gender'] = pd.Series(data=['F','F','M','M'])


# In[28]:


df_group = df.groupby(by=['STATUS','Gender'])
df_group.head()


# In[27]:


#Groupby with Aggregate Operations
df_group = df.groupby(by=['STATUS','Gender']).agg({'English':['mean','min','max']})
df_group.head(10)


# Merging Operations (SQL Like Merging)

# In[30]:


names = ['Kanishka', 'Sahithi','Bansal', 'Sibi']
eng_marks = [100,56,33,78]
hindi_marks = [87,43,23,65]
science_marks = [93,71,56,32]
social_marks = [90,54,56,78]
d = {'Student_Name':names,'English':eng_marks, 'Hindi':hindi_marks,'Science':science_marks, 'Social':social_marks}
df1 = pd.DataFrame(data=d)


# In[37]:


names = ['Kanishka', 'Sahithi','Bansal','Anand']
cul_act = [True,False,True,False]
pubser = [0,1,1,0]
d = {'Student_Name':names,'Cultural':cul_act, 'PublicService':pubser}
df2 = pd.DataFrame(data=d)


# In[38]:


df1


# In[39]:


df2


# In[40]:


# Inner Join (Intersection of df1 & df2)
df_intersection = df1.merge(df2, on="Student_Name", how="inner")
df_intersection


# In[41]:


# LeftOuter Join
df_leftouter = df1.merge(df2, on="Student_Name", how="left")
df_leftouter


# In[42]:


# RightOuter Join
df_rightouter = df1.merge(df2, on="Student_Name", how="right")
df_rightouter


# In[43]:


# FullOuter Join  [Union of df1 & df2]
df_fullouter = df1.merge(df2, on="Student_Name", how="outer")
df_fullouter


# In[45]:


# Cross Join
#df_cross = df1.merge(df2, on="Student_Name", how="cross")
#df_cross


# Combining DataFrames (Horizontally & Vertically

# In[46]:


names = pd.Series(['A','B','C','D'])
eng = pd.Series([60,70,80,90])
hin = pd.Series([70,30,20,10])
d = {'Name':names,'English':eng, 'Hindi':hin}
df1 = pd.DataFrame(data=d)
df1


# In[47]:


sci = pd.Series([650,40,60,70])
soc = pd.Series([40,70,40,50])
d1 = {'Science':sci,'Social':soc}
df2 = pd.DataFrame(data=d1)
df2


# In[ ]:




