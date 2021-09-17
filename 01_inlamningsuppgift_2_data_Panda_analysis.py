#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Data Collection
# Data Pre Processing
# EDA
# Conclusion


# In[3]:


# Import Libraries

import pandas as pd
import matplotlib
import seaborn as sns
from pathlib import Path
import numpy as np


# In[4]:



# Get the Data
url= "https://raw.githubusercontent.com/NordAxon/ec-python-course/master/assignments/01_inlamningsuppgift_2_data.csv"
df = pd.read_csv(url)
print(df.head(5))


# In[5]:


# Data Visualtion
df.hist(bins=50 , figsize=(20,15))


# In[105]:


df.plot(kind='hist' ,title= 'Covid19' )


# In[34]:


df.info()


# In[41]:


df[['country','people_vaccinated','total_vaccinations']].value_counts()


# In[42]:


df.describe()


# In[6]:


len(df)


# In[73]:


df.shape


# In[7]:


df.columns


# In[8]:


df.tail()


# In[107]:


from pandas.plotting import scatter_matrix

attributes = ["people_vaccinated" , 'total_vaccinations' , "country" ]
scatter_matrix(df[attributes], figsize=(12, 8))


# In[66]:


df.plot(kind='scatter' , x='people_vaccinated' , y='total_vaccinations'  ,label= 'people_vaccinated'
        ,figsize=(10,7) , cmap=plt.get_cmap("jet") , colorbar=True , sharex = False)
plt.legend()


# In[ ]:


# Data Cleaning


# In[67]:


df.isnull().sum()


# In[71]:


median1=df['people_vaccinated'].median()
median2=df['total_vaccinations'].median()
print(" Median people_vaccinated" , median)
print(" Median total_vaccinations" , median)


# In[10]:


df.isna()


# In[11]:


df_2 = df[['people_vaccinated' , 'total_vaccinations' , 'country' ]]
df_2.head()


# In[108]:


country_1 = df_2['country'] == 'Sweden'

sweden = df_2[country_1]

sweden.head()
sweden.dropna()


# In[109]:


country_2 = df_2['country'] == 'Italy'

Italy = df_2[country_2]

Italy.head()
Italy.dropna()


# In[93]:


df_2.hist(color='red')


# In[127]:


df = df.sort_values(by='country'  )
df.head()


# In[16]:


df.describe()


# In[17]:


df_2 = df[['people_vaccinated' , 'total_vaccinations' , 'country' ]]
df_2.head()


# In[18]:


mask = df_2['country'] == 'Sweden'

sweden = df_2[mask]

sweden.head()
sweden.dropna()


# In[19]:


df_2.hist(color='red' )


# In[22]:


df.dropna(inplace=True)


# In[106]:


df_3= df.groupby('country').sum()
df_3


# In[ ]:





# In[ ]:





# In[ ]:




