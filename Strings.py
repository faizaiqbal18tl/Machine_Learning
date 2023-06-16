#!/usr/bin/env python
# coding: utf-8

# In[1]:


#strings
statement = 'My name is "Faiza"'
print(statement) #if I use double quotes inside double quotes it will prompt an error so one way to avoid this is use escape "My name is \"Faiza"" or the one like above


# In[7]:


print ("My name is \" Faiza")


# In[11]:


#multi line comments
a = '''
My
name 
is 
Faiza
Iqbal'''
print(a)


# In[14]:


a = """A database is a collection of structured data that is organized and optimized for efficient retrieval, 
manipulation, and storage. It is typically used to support transactional processing, such as capturing and storing customer
orders or tracking inventory levels. Databases are designed to support online transaction processing (OLTP) and are
optimized for fast and efficient reads and writes.
"""
print(a)


# In[15]:


#Accessing character of a string (string is like an array of charcters, where array is collection of items)
name = "Faiza"
print(name[0])


# In[24]:


#For loop for strings
#if you want to see characters of  some large sentence it is difficult through indexing
name = "Faiza"

a = '''
Hi, my name is Faiza Iqbal
I am 22 years old, 
I am a Data Scientist'''
#print (a)


for character in a:
    print(character)


# In[22]:


name = "Faiza"
for character in name:
    print(character)


# In[ ]:




