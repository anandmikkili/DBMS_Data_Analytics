#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px


# In[2]:


data = px.data.tips()


# In[3]:


data.head()


# # Treemap Chart

# In[4]:


fig = px.treemap(data, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()


# In[7]:


import plotly
plotly.offline.plot(fig, filename='D:/Training/Unext/Source_Code/Python_Visualization/treemap_chart.html')


# # Sunburst Chart

# In[8]:


fig = px.sunburst(data, path=[ 'day', 'time', 'sex'], values='total_bill', color='day')
fig.show()


# In[9]:


import plotly
plotly.offline.plot(fig, filename='D:/Training/Unext/Source_Code/Python_Visualization/sunburst_chart.html')


# In[ ]:




