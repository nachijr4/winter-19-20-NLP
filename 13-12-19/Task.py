#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[3]:


from nltk.corpus import brown
brown.categories()


# In[9]:


len(brown.words(categories = 'adventure'))


# In[10]:


brown.words(categories = 'adventure')[:100]


# <h1>inaugural is the corupus of all the inaugural speechs given by the american presidents</h1>

# In[11]:


from nltk.corpus import inaugural


# In[13]:


len(inaugural.fileids())


# In[14]:


inaugural.fileids()


# In[18]:


inaugural.words(fileids = '2009-Obama.txt')


# In[21]:


words = inaugural.words(fileids = '2009-Obama.txt')[:20]


# In[22]:


for word in words:
    print(word)


# In[37]:


from nltk.book import *


# In[39]:


from nltk.probability import FreqDist

frequency = FreqDist(text1)
frequency.most_common(10)


# <h1>Frequency distribution function present in nltk</h1>

# In[33]:



frequency = FreqDist(inaugural.words(fileids = '2009-Obama.txt'))


# In[36]:


frequency.most_common(10)


# In[ ]:




