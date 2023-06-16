#!/usr/bin/env python
# coding: utf-8

# In[5]:


#built in functions
#min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc
def calculate_gmean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)
    
a = 2
b = 3

if (a>b):
    print("First number is greater")
else:
    print("Second number is greater")

calculate_gmean(a, b)

#calculate another gmean for c and d
c = 4
d = 5

if (a>b):
    print("First number is greater")
else:
    print("Second number is greater")
    
calculate_gmean(c, d)


# In[6]:


#instead of writing this long block of code you can write function within function
def calculate_gmean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)
def is_Greater(a, b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
    
a = 2
b = 3
is_Greater(a, b)
calculate_gmean(a, b) #function call

#calculate another gmean for c and d
c = 4
d = 5
is_Greater(c,d)
calculate_gmean(c, d)


# In[ ]:




