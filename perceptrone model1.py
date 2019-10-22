
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
dataset =pd.read_excel('Real estate valuation data set.xlsx')


# In[54]:


dataset.head(10)


# In[55]:


dataset.describe()


# In[56]:


dataset.columns


# In[57]:


dataset.drop(['No','X1 transaction date'],axis = 1,inplace =True)


# In[58]:


dataset.head()


# In[59]:


dataset['X1'] = dataset['X2 house age']


# In[60]:


dataset['X2'] = dataset['X3 distance to the nearest MRT station']


# In[61]:


dataset['X3'] = dataset['X4 number of convenience stores']
dataset['X4'] = dataset['X5 latitude']
dataset['X5'] = dataset['X6 longitude']
dataset['Y'] = dataset['Y house price of unit area']


# In[62]:


dataset.drop(['X2 house age','X3 distance to the nearest MRT station','X4 number of convenience stores', 'X5 latitude', 'X6 longitude','Y house price of unit area'],axis =1,inplace = True)


# In[63]:


dataset.head()


# In[64]:


weights = np.random.uniform(size=(5,1))


# In[65]:


weights


# In[66]:


bais = np.random.uniform(size = (1,1))
bais


# In[81]:


weights.shape


# In[67]:


x = dataset.iloc[:,:-1].values


# In[68]:


y = dataset.iloc[:,-1:].values


# In[69]:


y.shape


# In[70]:


x.shape


# In[71]:


bais[0,0]


# In[87]:


weights[0,0]
print(x[0,0],x[0,1],x[0,2],x[0,3],x[0,4])
print(weights[0,0],weights[1,0],weights[2,0],weights[3,0],weights[4,0])
print(y[1])


# In[84]:


for k in range(len(x)):
    sum=0
    for j in range(5):
        sum = sum+x[k,j]*weights[j,0]
    sum = sum+bais[0,0]
    
    y_answer = activation_function()    
    
    
    if(sum == y[k]):
        
    
    
    
    print(sum)


# In[92]:


get_ipython().run_line_magic('matplotlib', 'inline')
dataset['Y'].plot.box()


# In[95]:


dataset['Y'].plot.hist()


# In[ ]:


## theres a problem..cant solve anymore need to ask sir

