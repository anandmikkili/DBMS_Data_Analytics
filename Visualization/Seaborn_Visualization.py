#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Line Plot: To draw line between 2 numerical entities

# In[2]:


iris = pd.read_csv("D:/Training/Unext/Source_Code/Python_Visualization/iris.csv")
iris.columns


# In[3]:


iris.head()


# In[4]:


iris.species.value_counts()


# - Normal Line Plot

# In[5]:


sns.lineplot(x="sepal_length", y = "petal_length", data=iris)
plt.show()


# In[6]:


sns.lineplot(x="sepal_length", y = "sepal_width", data=iris)
plt.show()


# - Line Plot with hue [Grouping]

# In[11]:


sns.lineplot(x="sepal_length", y = "petal_length",hue='species', data=iris)
plt.show()


# - Line plot with markers

# In[12]:


sns.lineplot(x="sepal_length", y = "petal_length",hue='species',style='species', markers=True, data=iris)
plt.show()


# # Bar Plot: For distribution of Categorical Segments

# In[13]:


titanic = pd.read_csv("D:/Training/Unext/Source_Code/Python_Visualization/titanic.csv")
titanic.columns


# In[14]:


titanic.Survived.value_counts()


# In[20]:


titanic.Pclass.value_counts()


# - Normal Bar Plot

# In[27]:


palette = sns.color_palette("bright")
sns.barplot(x='Sex',y='Survived', data=titanic,palette='bright')
plt.show()


# - Grouping on Bar Plots

# In[23]:


sns.barplot(x='Sex',y='Survived',hue='Pclass', data=titanic)
plt.show()


# # Scatter Plot: Visualization of interpolate the data

# -  Normal Scatter Plot

# In[29]:


iris.columns


# In[30]:


sns.scatterplot(x='sepal_length', y='petal_length', data=iris)
plt.show()


# - Grouping in Scatter Plot

# In[31]:


sns.scatterplot(x='sepal_length', y='petal_length',hue='species', data=iris)
plt.show()


# In[32]:


sns.scatterplot(x='sepal_length', y='petal_length',hue='sepal_width', data=iris)
plt.show()


# # Histogram: Continuous Numerical Segments

# - Normal Histogram

# In[34]:


sns.distplot(iris.sepal_length)
plt.show()


# In[35]:


sns.distplot(iris.sepal_length, hist=False)
plt.show()


# In[36]:


sns.distplot(iris.sepal_length, color='red')
plt.show()


# In[37]:


sns.distplot(iris.sepal_length, color='green',vertical=True)
plt.show()


# # Joint Plot (Scatter Plot + Histogram)

# In[42]:


sns.jointplot(x='sepal_length', y='petal_length', data=iris,palette='dark2')
plt.show()


# # Box Plot: To identify the outliers

# In[43]:


titanic.columns


# In[47]:


sns.boxplot(x='Survived',y='Age', data=titanic)
plt.show()


# In[49]:


sns.boxplot(x='Survived',y='Age',hue='Sex', data=titanic)
plt.show()


# # Pair Plot: To find correlation between any 2 segment

# In[51]:


sns.pairplot(data=iris,size=3)
plt.show()


# In[53]:


iris.columns


# In[54]:


sns.pairplot(data=iris,hue='species',size=3)
plt.show()


# In[55]:


sns.pairplot(data=iris,hue='species',diag_kind="hist",size=3)
plt.show()


# # Heatmap: To show the correlation between variables with intensity/number

# In[61]:


iris_num = iris.drop(columns=['species'])
sns.heatmap(iris_num.corr(), annot=True)
plt.show()


# In[ ]:


# 0.6 - 0.9

