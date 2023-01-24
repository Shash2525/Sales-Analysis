#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[5]:


files=[file for file in os.listdir('C:\\Users\\91863\\OneDrive\\Desktop\\Sales_Data-20230117T090451Z-001\\Sales_Data')]
for file in files:
    print (file)


# In[11]:


path='C:\\Users\\91863\\OneDrive\\Desktop\\Sales_Data-20230117T090451Z-001\\Sales_Data'
all_data=pd.DataFrame()
for file in files:
    current_df=pd.read_csv(path+'/'+file)
    all_data=pd.concat([all_data,current_df])
all_data.shape    


# In[17]:


all_data.to_csv(r'C:\Users\91863\OneDrive\Desktop\Sales_Data-20230117T090451Z-001\Sales_Data\Combined_data.csv',index=False)


# In[19]:


#data cleaning and formatting
all_data.dtypes


# In[20]:


all_data.head(10)


# In[28]:


all_data.isnull().sum()


# In[29]:


all_data=all_data.dropna(how='all')
all_data.shape


# In[33]:


# Which month has highest number of sales.
'04/19/19 08:46'.split('/')[0]


# In[34]:


def month(x):
    return x.split('/')[0]


# In[39]:


all_data['Month']= all_data['Order Date'].apply(month)


# In[40]:


all_data.head(10)


# In[37]:


all_data.dtypes


# In[42]:


all_data['Month'].unique()


# In[43]:


filter=all_data['Month']=='Order Date'
len(all_data[~filter])


# In[44]:


all_data=all_data[~filter]


# In[45]:


all_data['Month']=all_data['Month'].astype(int)


# In[47]:


all_data.dtypes


# In[48]:


all_data['Price Each']=all_data['Price Each'].astype(float)
all_data['Quantity Ordered']=all_data['Quantity Ordered'].astype(int)


# In[49]:


all_data.dtypes


# In[50]:


all_data['Sales']=all_data['Quantity Ordered']*all_data['Price Each']


# In[51]:


all_data.head(10)


# In[52]:


all_data.groupby('Month')['Sales'].sum()


# In[55]:


Months=range(1,13)
plt.bar(Months,all_data.groupby('Month')['Sales'].sum())
plt.xticks(Months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()


# In[61]:


# Which city has highest number of sales?
'917 1st St, Dallas, TX 75001'.split(',')[1]


# In[63]:


def City(x):
    return x.split(',')[1]


# In[65]:


all_data['City']=all_data['Purchase Address'].apply(City)


# In[66]:


all_data.head()


# In[71]:


all_data.groupby('City')['City'].count().plot.bar()


# In[76]:


all_data['Order Date'].dtype


# In[78]:


all_data['Hour']=pd.to_datetime(all_data['Order Date']).dt.hour


# In[79]:


all_data.head()


# In[81]:


keys=[]
hour=[]
for key,hour_df in all_data.groupby('Hour'):
    keys.append(key)
    hour.append(len(hour_df))


# In[82]:


plt.grid()
plt.plot(keys,hour)


# In[ ]:


#Between 12 to 7 is the best time to advertise to maximise product purchase


# In[83]:


all_data.groupby('Product')['Quantity Ordered'].sum().plot(kind='bar')


# In[84]:


all_data.groupby('Product')['Price Each'].mean()


# In[85]:


products=all_data.groupby('Product')['Quantity Ordered'].sum().index
quantity=all_data.groupby('Product')['Quantity Ordered'].sum()
prices=all_data.groupby('Product')['Price Each'].mean()


# In[86]:


plt.figure(figsize=(40,24))
fig,ax1 = plt.subplots()
ax2=ax1.twinx()
ax1.bar(products, quantity, color='g')
ax2.plot(products, prices, 'b-')
ax1.set_xticklabels(products, rotation='vertical', size=8)


# In[87]:


df=all_data[all_data['Order ID'].duplicated(keep=False)]
df.head(20)


# In[88]:


#create grouped col 
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))


# In[89]:


df2 = df.drop_duplicates(subset=['Order ID'])


# In[90]:


df2['Grouped'].value_counts()[0:5].plot.pie()


# In[91]:


import plotly.graph_objs as go
from plotly.offline import iplot


# In[92]:


values=df2['Grouped'].value_counts()[0:5]
labels=df['Grouped'].value_counts()[0:5].index


# In[93]:


trace=go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=25),
              pull=[0, 0, 0,0.2, 0]
               )


# In[94]:


iplot([trace])


# In[ ]:




