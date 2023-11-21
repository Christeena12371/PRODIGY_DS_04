#!/usr/bin/env python
# coding: utf-8

# # PRODIGY INFOTECH -  DATASCIENCE INTERNSHIP
# 
# ## TASK - 4
# 
# ### Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes towards specific topics or brands.
# 

# In[31]:


#Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[32]:


#Load the data
Data=pd.read_csv("C:/Users/steph/OneDrive/Documents/twitter.csv")
print(Data)


# In[33]:


#Create a dataframe
df=pd.DataFrame(Data)
df


# In[34]:


#First 5 rows of the dataset
df.head()


# In[35]:


#Last 5 rows of the dataset
df.tail


# In[36]:


#Check for the information ,i.e, dtype and null value for each column
df.info


# In[37]:


#Check for Statistical analysis
df.describe()


# In[38]:


#Check for unique values
df.nunique()


# In[39]:


#Check for the no.of rows and columns
df.shape


# In[40]:


#Check for the data type
df.dtypes


# In[41]:


#Checking for null values
df.isnull().sum()


# In[42]:


#dropping irrelevant columns
df.dropna(subset=['Content'], inplace=True)


# In[43]:


#Check for null values
df.isnull().sum()


# In[44]:


#Check for the unique values in the column 'Sentiment'
df.Sentiment.unique()


# In[45]:


#Replacing 'Irrelevant' by 'Neutral' in the 'Sentiment' column
df.Sentiment=df.Sentiment.replace('Irrelevant','Neutral')
df.Sentiment


# In[46]:


#Check for the unique values of the column 'Sentiment'
df.Sentiment.unique()


# In[47]:


#Counting the occurences of each value in the 'Sentiment' column
Sentiment_count=df.Sentiment.value_counts()
Sentiment_count


# In[82]:


plt.pie(Sentiment_count, labels= ['Neutral','Negative','Positive'],colors=['green','orange','yellow'], 
        wedgeprops={'edgecolor':'black'}, autopct='%0.1f%%')
plt.title('Pie chart of Sentiments')
plt.tight_layout
plt.show


# In[49]:


#Unique values of the column 'Entity'
df.Entity.unique()


# In[50]:


#Counting the occurences of each value in the 'Entity' column
Entity_count=df.Entity.value_counts()
Entity_count


# In[51]:


#1st 10 value of the column 'Entity'
First_10_Entity=Entity_count.head(10)
First_10_Entity


# In[83]:


#PLotting the bar graph of 'Entity'
Entity=['MaddenNFL','LeagueOfLegends','CallOfDuty','Verizon','TomClancysRainbowSix',
        'Facebook','Microsoft','Dota2','WorldOfCraft','ApexLegends']
Id=[2377,2377,2376,2365,2364,2362,2361,2359,2357,2353]

plt.barh(Entity,Id,color='red')
plt.xticks(rotation=45)
plt.ylabel('Entity')
plt.xlabel('Number of Posts in Twitter')
plt.title('Bar graph of Entity')
plt.show()


# In[53]:


#1st three values of 'Entity'
First_5_Entity=Entity_count.head(3)
First_5_Entity


# In[54]:


#Extracting the index values and converting them into list
First_5_Entity_list=First_5_Entity.index.tolist()
First_5_Entity_list


# In[59]:


# Grouping by 'Enity' and 'Sentiments' and coutning the occurences of each unique sentiment value
Sentiment_and_Entity=df.loc[df['Entity'].isin(First_5_Entity_list)].groupby('Entity')['Sentiment'].value_counts().sort_index()
Sentiment_and_Entity


# In[73]:


# Plotting the pie chart of the grouped columns
plt.figure(figsize=(10,5))

Sentiments=['Neutral' , 'Negative' , 'Positive']
color=['red' , 'brown','orange']

plt.subplot(2,3,1)
plt.pie(Sentiment_and_Entity[:3] , labels=Sentiments , autopct='%0.1f%%' , colors=color)

plt.subplot(2,3,2)
plt.pie(Sentiment_and_Entity[3:6] , labels=Sentiments , autopct='%0.1f%%', colors=color)

plt.subplot(2,3,3)
plt.pie(Sentiment_and_Entity[6:] , labels=Sentiments , autopct='%0.1f%%', colors=color)


