#!/usr/bin/env python
# coding: utf-8

# # 📊 Dataset Description: Retail Sales Analysis
# 
# #### This dataset contains transactional retail sales data, capturing customer purchases across different product categories along with demographic and pricing details.
# ### Column Names:-
# #### transactions_id, sale_date, sale_time, customer_id, gender, age, category, quantity, price_per_unit, cogs, total_sale
# 
#     

# ## End-to-End Mini Project
# 
# ### 👉 Perform full EDA:

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("SQL_Sale.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.sample()


# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


df.describe


# In[9]:


df.columns


# In[10]:


df.nunique


# # Clean missing values or null

# In[11]:


df.isnull().sum()


# In[12]:


df2=df.copy()
df2


# In[13]:


# Correct way
df2['age'] = df2['age'].fillna(df2['age'].median())
df2
df2.isnull().sum()


# In[ ]:





# In[14]:


column=['age','quantiy','price_per_unit','cogs','total_sale']
for col in column:
    df2[col] =df2[col].fillna(df2[col].median())

df2.isnull().sum()


# # Handle duplicates

# In[15]:


df2.duplicated()


# # Fix data types

# In[16]:


df2['age']=df2['age'].astype(float)
df2.dtypes


# In[17]:


df2.dtypes


# # Create new features

# # Feature Engineering
# 
# ### 👉 Create:
# 
# ### total_amount = quantity * price_per_unit
# ### A new column: "High Value" if total > 1000 else "Low Value"

# In[18]:


df2.assign(total_amount = df2['quantiy'] * df2['price_per_unit'])


# In[19]:


df2['value_status'] = df2['total_sale'].apply(lambda x: 'High Value' if x > 1000 else 'Low Value')
df2


# #### 3. Customer Lifetime Value (CLV)
# 
# #### 👉 Create a feature:
# 
# #### Total money spent by each customer across all transactions

# In[26]:


df2.groupby('customer_id')['total_sale'].transform('sum')



# In[28]:


df2['CLV'] = df2.groupby('customer_id')['total_sale'].transform('sum')
df2.head()


# #### 2. Purchase Frequency
# 
# #### 👉 Create a column:
# 
# #### Number of purchases per customer
# 
# #### Then classify:
# 
# #### "Frequent Buyer" (>10 purchases)
# #### "Occasional Buyer"

# In[39]:


df2['purchase_freq'] = df2.groupby('customer_id')['transactions_id'].transform('count')


# In[37]:


df2.drop('CLV', axis=1, inplace=True)
df2


# In[42]:


df2['buyer_type'] = df2['purchase_freq'].apply(lambda x: "Frequent Buyer" if x > 10 else "Occasional Buyer")
df2


# #### Average Order Value (AOV)
# 
# #### 👉 For each customer:
# 
# #### Compute average spending per transaction

# In[45]:


df2['AOV'] = df2['customer_total'] / df2['purchase_freq']
df2


# In[46]:


df2['AOV'] = df2.groupby('customer_id')['total_sale'].transform('mean')
df2

