#!/usr/bin/env python
# coding: utf-8

# In[113]:


#importing pandas and other tools
import pandas as pd
import matplotlib.pyplot as plt
import plotnine as gg


# In[97]:


tv_df = pd.read_csv("namu_shows.csv")
tv_df = tv_df.rename(columns={'rating ': 'rating'})


# In[98]:


#first five shows in order of when i watched them 
tv_df.head()


# In[99]:


# getting genre of the series
tv_df.columns


# In[100]:


tv_df[['show_title','genre']]


# In[101]:


#How many seasons of shows have I seen in a three year span? 
tv_df['num_of_seasons'].sum()


# In[102]:


#How many shows have I rated under 5? 
tv_df[tv_df['rating'] <= 5].value_counts()


# In[103]:


tv_df[tv_df['rating']>= 5].count()


# In[104]:


#count how many shows per streaming platform overall 
tv_df['streaming_platform'].value_counts()


# In[118]:


#how many shows do i watch per year?
tv_df['year_watched'].value_counts()


# In[106]:


#what genre do i watch the most? (this was shocking)
tv_df['genre'].value_counts()


# In[110]:


#what are my top 5 most watched genres? 
tv_df['genre'].value_counts().head()


# In[119]:


#top 10? 
tv_df['genre'].value_counts().head(10)


# In[109]:


#no repeats
tv_df['show_title'].nunique()


# In[ ]:


(gg.ggplot(tv_df, gg.aes(x='', y='wt'))
    + gg.geom_bar(stat='identity'))

