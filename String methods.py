#!/usr/bin/env python
# coding: utf-8

# In[3]:


#string methods
name = "Faiza!"
print((name))

#strings are immutable canot be changed we can create a new string using string methods
print(name.upper()) #it will create a new string but do not change the existing string


# In[4]:


print(name.lower())


# In[7]:


#you can remove trailing char from strings like !, ? using rstrip
print(name.rstrip("!"))

#it will not strip leading !
name1="!Faiza"
print(name1.rstrip("!"))


# In[13]:


#replace characters in string
name2="Faiza Iqbal is a good girl. The word Faiza Iqbal means Victorious."
print(name2.replace("Faiza Iqbal","Faiza"))


# In[15]:


#split( ) in python returns the separated strings as list items
print(name2.split(" "))


# In[18]:


#if you want first letter to be capital use capitalize()
a="welcome to 100 days of programming"
print(a.capitalize())

#if you make any mistake it will correct it and make frst letter capital and rest to be uniform
b="welcoMe to 100 days of prOgramming"
print(b.capitalize())


# In[24]:


#to move string towards center
c="Hey matos!"
print(c)
print(len(c))
print(c.center(50))
print(len(c.center(50)))


# In[26]:


print(name2.count("Faiza"))


# In[28]:


print(name1.endswith("!")) #it returns boolean datatype
print(c.endswith("!"))


# In[30]:


print(a.endswith("to",0 , 10)) #"welcome to 100 days of programming" [0:10] = welcome to "Yes it ends with to"


# In[33]:


#find() will detect first occurance of that word you want to detect in string
print(a.find("is")) #-1 means no occurance of is in a
print(a.find("to")) #to is strating at index 8 in a


# In[35]:


#index() method is used whe you raise an exception you want python to find" is" in string and if is not present do not return -1 instead prompt and error
print(a.index("to"))
print(a.index("is")) #error: substring not found


# In[39]:


# isalnum() , look for char like A-Z, a-z, 0-9
str="MyNameisFaiza1"
print(str.isalnum()) #if there is space it will return false
print(c.isalnum())


# In[40]:


#isalpha() return only alphabet A-Z, a-z
str="MyNameisFaiza1"
print(str.isalpha()) #if there is numeric value it will return false


# In[42]:


#islower() to see if all char are in lower case
print(str.islower()) 

#you can make it lower
print(str.lower()) 


# In[44]:


#isprintable() return only printable char
print(str.isprintable())

str1="MyNameisFaiza1\n" 
print(str1.isprintable()) #now it will return false \n is not a printable char


# In[49]:


print(str.isspace())

x="   "
print(x.isspace()) # check white space


# In[50]:


print(str.startswith("My"))


# In[51]:


#swapcase() upper case to lower and vice versa
print(str.swapcase())


# In[52]:


#title() change string into title case
print(a.title())


# In[ ]:




