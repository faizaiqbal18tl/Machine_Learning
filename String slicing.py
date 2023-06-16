#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string slicing and operations on strings
name="Faiza,Iqbal"
print(name[0:5]) #to print no of letters in a string, including 0 but not 5 it will print [0: 5-1] = [0:4]


# In[2]:


#if you want to see the length of the string use len function; len()
print(len(name))


# In[3]:


sub = "Data"
length = len (sub)
print("Data is a", length, "letter word")


# In[4]:


print(name[:5]) #if you skip 0 it does not make any change python will consider starting from 0


# In[6]:


# print Iqbal
print(name[6:])


# In[7]:


print(name[0:-3]) # This means [0:len(name)-3] =[0:11-3] = [0:8] = Faiza,Iq


# In[8]:


print(name[-3:-1]) # [11-3:11-1] = [8:10]


# In[9]:


print(name[-1:-3]) #[11-1:11-3] = [10:8] This makes no sense


# In[11]:


name1="Harry"
print(name1[-4:-2])


# In[ ]:




