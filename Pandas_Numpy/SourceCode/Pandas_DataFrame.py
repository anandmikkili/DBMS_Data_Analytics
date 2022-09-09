#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


names = ['Kanishka', 'Sahithi','Bansal', 'Sibi']
eng_marks = [100,56,33,78]
hindi_marks = [87,43,23,65]
science_marks = [93,71,56,32]
social_marks = [90,54,56,78]
d = {'Student_Name':names,'English':eng_marks, 'Hindi':hindi_marks,'Science':science_marks, 'Social':social_marks}
df = pd.DataFrame(data=d)


# In[5]:


df


# In[6]:


type(df)


# In[7]:


df.shape


# In[10]:


df


# In[151]:


df = pd.read_csv("data/marks.csv")


# In[152]:


df


# In[153]:


#!pip install openpyxl


# In[154]:


#df = pd.read_excel("data/marks.xlsx")
#df


# In[155]:


df.values


# In[156]:


type(df.values)


# In[157]:


df.dtypes


# In[158]:


df.columns.tolist()


# In[159]:


df.size


# Retrieve Rows from Pandas DataFrame

# In[160]:


df


# In[161]:


df.at[2,'English']


# In[162]:


df.iat[1,3]


# In[163]:


df.loc[2]       # Row wise retrieval


# In[164]:


df.loc[1:3]      #Label Based


# In[165]:


df.iloc[2]


# In[166]:


df1 = df.iloc[1:3]          #Slicing the Dataframe (Index Based)


# In[167]:


df1


# Iterate over Pandas DataFrame

# In[168]:


for i,r in df.iterrows():
    print("Index is: ",i, " The Row is: ",r['Name'])


# In[169]:


def pass_fail_status(eng,hin,sci,soc):
    if((eng>=35) and (hin>=35) and (sci>=35) and (soc>=35)):
        return 'P'
    else:
        return 'F'


# In[170]:


import time


# In[171]:


start_for = time.time()
df['STATUS']='F'
for i,r in df.iterrows():
    df.at[i,'STATUS'] = pass_fail_status(r.English,r.Hindi,r.Science,r.Social)
end_for = time.time()
print("Total Time Taken By ForLoop: ", (end_for - start_for), "Seconds")
df


# In[172]:


df1 = pd.read_csv("data/marks.csv")


# In[173]:


df1


# In[174]:


start_lambda = time.time()
df1['STATUS'] = df1.apply(lambda r: pass_fail_status(r.English,r.Hindi,r.Science,r.Social), axis=1)
end_lambda = time.time()
print("Total Time Taken By Lambda Function to Execute: ",(end_lambda - start_lambda), "Seconds")


# In[175]:


df1


# Statistical Operations on Pandas DataFrame

# In[176]:


df.English.mean()


# In[177]:


df.English.mode()


# In[178]:


df.English.max()


# In[179]:


df.English.min()


# Scalar Operations on Pandas DataFrame

# In[180]:


df.Hindi = df.Hindi+5


# In[181]:


#df['Hindi'] = df['Hindi']+5


# In[182]:


#df.loc['Hindi'] = df['Hindi']+5


# In[183]:


df['Hindi'] = df.apply(lambda r: ((r.Hindi)+5),axis=1)


# In[184]:


df


# Object Operations on Pandas DataFrame

# In[185]:


names = pd.Series(['A','B','C','D'])
eng = pd.Series([60,70,80,90])
hin = pd.Series([70,30,20,10])
d = {'Name':names,'English':eng, 'Hindi':hin}
df1 = pd.DataFrame(data=d)
df1


# In[186]:


sci = pd.Series([650,40,60,70])
soc = pd.Series([40,70,40,50])
d1 = {'Science':sci,'Social':soc}
df2 = pd.DataFrame(data=d1)
df2


# In[187]:


#Horizontal Concatenation of DataFrames


# In[188]:


df = pd.concat([df1,df2],axis=1)
df.shape


# In[189]:


names = pd.Series(['A','B','C','D'])
eng = pd.Series([60,70,80,90])
hin = pd.Series([70,30,20,10])
sci = pd.Series([650,40,60,70])
soc = pd.Series([40,70,40,50])
d2 = {'Name':names,'English':eng, 'Hindi':hin,'Science':sci,'Social':soc}
df3 = pd.DataFrame(data=d2)
df3


# In[190]:


df3.shape


# In[191]:


#Vertical Concatenation of DataFrames
df = pd.concat([df,df3],axis=0, ignore_index=True)
df.shape


# In[192]:


df


# In[194]:


names = pd.Series(['A','B','C','D'])
eng = pd.Series([60,70,80,90])
hin = pd.Series([70,30,20,10])
sci = pd.Series([50,40,60,70])
soc = pd.Series([40,70,40,50])
d2 = {'Name':names,'English':eng, 'Hindi':hin,'Science':sci,'Social':soc}
df1 = pd.DataFrame(data=d2)
df1


# In[195]:


names = pd.Series(['A','B','C','D'])
eng = pd.Series([60,70,80,90])
hin = pd.Series([70,30,20,10])
sci = pd.Series([650,40,60,70])
soc = pd.Series([40,70,40,50])
d2 = {'Name':names,'English':eng, 'Hindi':hin,'Science':sci,'Social':soc}
df2 = pd.DataFrame(data=d2)
df2


# In[200]:


df3 = df1+df2


# In[201]:


df3


# In[ ]:




