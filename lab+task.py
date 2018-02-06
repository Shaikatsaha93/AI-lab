
# coding: utf-8

# In[1]:


#task 1
import pandas as pd
df=pd.read_csv('iris.csv')
df.head()


# In[3]:


df.tail(3)


# In[9]:


#task 2
df.sort_values("petal_length")


# In[8]:


#task 3
df1=df.groupby(['species'][0:4])['sepal_length','sepal_width','petal_length','petal_width'].mean()
print(df1)


# In[17]:


#task 4
import matplotlib.patches as mp
sepal_length=df['sepal_length']
sepal_width=df['sepal_width']
species = df['species']
pairs={'setosa' :'red','versicolor' :'green','virginica' :'blue'} 
labels = [mp.Patch(color=cl, label=la) for la, cl in pairs.items()]

plt.scatter(sepal_length, sepal_width, c=[pairs[i] for i in species], label=[pairs[i] for i in pairs])
plt.ylabel('Sepal Widht')                       
plt.xlabel('Sepal Length')                       
plt.title('Sepal Width vs Sepal Length')  
plt.legend(handles = labels)
plt.show()


# In[32]:


import matplotlib.patches as mp
petal_length=df['petal_length']
petal_width=df['petal_width']
species = df['species']
pairs={'setosa' :'red','versicolor' :'green','virginica' :'blue'} 
labels = [mp.Patch(color=cl, label=la) for la, cl in pairs.items()]

plt.scatter(petal_length, petal_width, c=[pairs[i] for i in species], label=[pairs[i] for i in pairs])
plt.ylabel('Petal Widht')                        
plt.xlabel('Petal Length')                        
plt.title('Petal Width vs Petal Length')  
plt.legend(handles = labels)
plt.show()


# In[37]:


#task 5
import numpy as np
df['Calyx Width'] = np.where(df['sepal_length'] <5, 0, 1)
df.head()


# In[42]:


sepal_length = df['sepal_length']
plt.hist(sepal_length, bins = 30 ) 
plt.title("Sepal Length") 
plt.show()

