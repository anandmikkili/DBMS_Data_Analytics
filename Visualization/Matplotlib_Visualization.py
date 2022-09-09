#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Line Plot: Between 2 numerical entities

# In[4]:


x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([70,60,80,40,90,20,70,45,67,82])


# In[5]:


plt.plot(x,y)
plt.show()


# In[8]:


#Better Visualization of Line Plot
plt.plot(x,y)
plt.title("Student vs Marks")
plt.xlabel("Student ID")
plt.ylabel("Marks Scored")
plt.grid(True)
plt.show()


# In[17]:


#Subplots in Line Plot
student_ids = np.array([101,102,103,104,105,106,107,108,109,110])
english = np.array([70,60,80,40,90,20,70,45,67,82])
hindi = np.array([45,60,68,80,39,56,70,45,67,82])
science = np.array([93,21,68,40,90,40,70,45,67,82])
social = np.array([24,84,30,40,80,45,58,45,67,82])

plt.subplot(2,2,1)
plt.plot(student_ids, english, color='r',linestyle=':', linewidth=2)
plt.title("Student ID vs English Marks")
plt.xlabel("Student ID")
plt.ylabel("English Marks")
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(student_ids, hindi, color='g',linestyle=':', linewidth=2)
plt.title("Student ID vs Hindi Marks")
plt.xlabel("Student ID")
plt.ylabel("Hindi Marks")
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(student_ids, science, color='b',linestyle=':', linewidth=2)
plt.title("Student ID vs Science Marks")
plt.xlabel("Student ID")
plt.ylabel("Science Marks")
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(student_ids, science, color='y',linestyle=':', linewidth=2)
plt.title("Student ID vs Social Marks")
plt.xlabel("Student ID")
plt.ylabel("Social Marks")
plt.grid(True)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

plt.show()


# Bar Plot: To present distribution of Categorical Segment

# In[20]:


students = {'Kanishka':7, 'Sahithi':8, 'Sibi':11, 'Athul':3, 'Raj':15}
names = list(students.keys())
ranks = list(students.values())

plt.bar(names, ranks)
plt.title("Student & Rank Distribution")
plt.xlabel("Name of Student")
plt.ylabel("Rank of Student")
plt.grid(True)
plt.show()


# In[22]:


student_ids = ["A","B","C","D","E","F","G","H","I","J"]
english = [70,60,80,40,90,20,70,45,67,82]
hindi = [45,60,68,80,39,56,70,45,67,82]
science = [93,21,68,40,90,40,70,45,67,82]
social = [24,84,30,40,80,45,58,45,67,82]

plt.subplot(2,2,1)
plt.bar(student_ids, english, color='r',linestyle=':', linewidth=2)
plt.title("Student ID vs English Marks")
plt.xlabel("Student ID")
plt.ylabel("English Marks")
plt.grid(True)

plt.subplot(2,2,2)
plt.bar(student_ids, hindi, color='g',linestyle=':', linewidth=2)
plt.title("Student ID vs Hindi Marks")
plt.xlabel("Student ID")
plt.ylabel("Hindi Marks")
plt.grid(True)

plt.subplot(2,2,3)
plt.bar(student_ids, science, color='b',linestyle=':', linewidth=2)
plt.title("Student ID vs Science Marks")
plt.xlabel("Student ID")
plt.ylabel("Science Marks")
plt.grid(True)

plt.subplot(2,2,4)
plt.bar(student_ids, social, color='y',linestyle=':', linewidth=2)
plt.title("Student ID vs Social Marks")
plt.xlabel("Student ID")
plt.ylabel("Social Marks")
plt.grid(True)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

plt.show()


# In[23]:


#Horizontal Bar Plot
students = {'Kanishka':7, 'Sahithi':8, 'Sibi':11, 'Athul':3, 'Raj':15}
names = list(students.keys())
ranks = list(students.values())

plt.barh(names, ranks)
plt.title("Student & Rank Distribution")
plt.xlabel("Name of Student")
plt.ylabel("Rank of Student")
plt.grid(True)
plt.show()


# Scatter Plot: Discrete Line Plot

# In[27]:


x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([70,60,80,40,90,20,70,45,67,82])

plt.scatter(x,y, marker='*',color='r',s=100)
plt.title("Student vs Marks")
plt.xlabel("Student ID")
plt.ylabel("Marks Scored")
plt.grid(True)
plt.show()


# In[28]:


student_ids = ["A","B","C","D","E","F","G","H","I","J"]
english = [70,60,80,40,90,20,70,45,67,82]
hindi = [45,60,68,80,39,56,70,45,67,82]
science = [93,21,68,40,90,40,70,45,67,82]
social = [24,84,30,40,80,45,58,45,67,82]

plt.subplot(2,2,1)
plt.scatter(student_ids, english, marker='*',color='r',s=100)
plt.title("Student ID vs English Marks")
plt.xlabel("Student ID")
plt.ylabel("English Marks")
plt.grid(True)

plt.subplot(2,2,2)
plt.scatter(student_ids, hindi, marker='*',color='g',s=100)
plt.title("Student ID vs Hindi Marks")
plt.xlabel("Student ID")
plt.ylabel("Hindi Marks")
plt.grid(True)

plt.subplot(2,2,3)
plt.scatter(student_ids, science, marker='*',color='b',s=100)
plt.title("Student ID vs Science Marks")
plt.xlabel("Student ID")
plt.ylabel("Science Marks")
plt.grid(True)

plt.subplot(2,2,4)
plt.scatter(student_ids, social, marker='*',color='y',s=100)
plt.title("Student ID vs Social Marks")
plt.xlabel("Student ID")
plt.ylabel("Social Marks")
plt.grid(True)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

plt.show()


# In[33]:


student_ids = ["A","B","C","D","E","F","G","H","I","J"]
english = [70,62,80,40,70,20,70,95,67,82]
hindi = [45,64,68,70,39,56,70,45,57,86]
science = [93,21,68,55,90,40,60,45,47,89]
social = [24,84,30,50,80,45,58,65,61,90]

plt.scatter(student_ids, english, marker='*',color='r',s=100)
plt.scatter(student_ids, hindi, marker='*',color='g',s=100)
plt.scatter(student_ids, science, marker='*',color='b',s=100)
plt.scatter(student_ids, social, marker='*',color='y',s=100)
plt.title("Student ID vs Subject Marks")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


# Histogram: For Continuous Numerical Segment

# In[35]:


marks = [90,56,87,65,28,92,39,52,10,68,32]
plt.hist(marks)
plt.show()


# In[38]:


data = pd.read_csv("data/iris.csv")


# In[39]:


data.columns


# In[45]:


plt.hist(data.sepal_length, color='r',bins=20)
plt.title("Distribution of Sepal Length for Iris Data")
plt.xlabel("Sepal Length")
plt.ylabel("Count")
plt.grid(True)
plt.show()


# In[46]:


data.describe()


# Box Plot: Used to analyse the outliers

# In[ ]:


#200 Rs ===> Max(Amabani 200 Cr Rs)  75%(RJ 100 Cr Rs)     Infosys(50%: 50K Rs)    (SE: 25%; 1000 Rs)      Min: Begger (2Rs)


# In[50]:


data = np.random.normal(100,20,300)
plt.boxplot(data)
plt.show()


# In[52]:


data


# In[57]:


english = [1,5,7,9,10,13,12,0,0,0,0,0,0,90,99]
hindi = [1,5,7,9,10,13,12,0,0,89,90,0,0,0,99]
science = [81,65,87,79,10,13,12,70,80,89,90,90,90,80,99]
data = [english, hindi, science]
labels = ['English','Hindi', 'Science']
plt.boxplot(data)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject Vs Marks")
plt.grid(True)
plt.show()


# In[58]:


english = [1,5,7,9,10,13,12,0,0,0,0,0,0,90,99]
hindi = [1,5,7,9,10,13,12,0,0,89,90,0,0,0,99]
science = [81,65,87,79,10,13,12,70,80,89,90,90,90,80,99]

plt.subplot(2,2,1)
plt.boxplot(english)
plt.title("English Marks")
plt.xlabel("English")
plt.ylabel("English Marks")
plt.grid(True)

plt.subplot(2,2,2)
plt.boxplot(hindi)
plt.title("Hindi Marks")
plt.xlabel("Hindi")
plt.ylabel("Hindi Marks")
plt.grid(True)

plt.subplot(2,2,3)
plt.boxplot(science)
plt.title("Science Marks")
plt.xlabel("Science")
plt.ylabel("Science Marks")
plt.grid(True)


plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

plt.show()


# Violin Plot: Same like Box Plot

# In[59]:


english = [1,5,7,9,10,13,12,0,0,0,0,0,0,90,99]
hindi = [1,5,7,9,10,13,12,0,0,89,90,0,0,0,99]
science = [81,65,87,79,10,13,12,70,80,89,90,90,90,80,99]
data = [english, hindi, science]
labels = ['English','Hindi', 'Science']
plt.violinplot(data,showmeans=True)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subject Vs Marks")
plt.grid(True)
plt.show()


# In[61]:


english = [1,5,7,9,10,13,12,0,0,0,0,0,0,90,99]
hindi = [1,5,7,9,10,13,12,0,0,89,90,0,0,0,99]
science = [81,65,87,79,10,13,12,70,80,89,90,90,90,80,99]

plt.subplot(2,2,1)
plt.violinplot(english, showmeans=True)
plt.title("English Marks")
plt.xlabel("English")
plt.ylabel("English Marks")
plt.grid(True)

plt.subplot(2,2,2)
plt.violinplot(hindi, showmeans=True)
plt.title("Hindi Marks")
plt.xlabel("Hindi")
plt.ylabel("Hindi Marks")
plt.grid(True)

plt.subplot(2,2,3)
plt.violinplot(science, showmeans=True)
plt.title("Science Marks")
plt.xlabel("Science")
plt.ylabel("Science Marks")
plt.grid(True)


plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

plt.show()


# Pie Chart: To understand the frequency or percentage of different categorical segments

# In[62]:


#Frequency
students = ['Kanishka', 'Sahithi','Sibi','Akriti','Amith', 'Rahul']
college_bunks_days = [76,87,65,56,85,35]
plt.pie(college_bunks_days, labels=students)
plt.show()


# In[63]:


#Percentage
students = ['Kanishka', 'Sahithi','Sibi','Akriti','Amith', 'Rahul']
college_bunks_days = [76,87,65,56,85,35]
plt.pie(college_bunks_days, labels=students, autopct='%0.2f%%')
plt.show()


# Donut Chart: Like of Pie Chart and is another form of Pie Chart

# In[68]:


#Frequency
students = ['Kanishka', 'Sahithi','Sibi','Akriti','Amith', 'Rahul']
college_bunks_days = [76,87,65,56,85,35]
plt.pie(college_bunks_days, labels=students,radius=2)
plt.pie([1],colors=['w'],radius=1)
plt.show()


# In[71]:


#Percentage
students = ['Kanishka', 'Sahithi','Sibi','Akriti','Amith', 'Rahul']
college_bunks_days = [76,87,65,56,85,35]
plt.pie(college_bunks_days, labels=students,autopct ='%0.2f%%',radius=2)
plt.pie([1],colors=['w'],radius=1)
plt.show()


# Pair Plots: For identifying correlation between any pair of segments

# In[72]:


data = pd.read_csv("data/iris.csv")


# In[73]:


data.columns


# In[74]:


import seaborn as sns


# In[ ]:




