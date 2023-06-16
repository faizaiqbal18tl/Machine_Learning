#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Conditional operators: >, <, >=, <=, !=, ==
age = int(input("Enter your age:"))
print("Your age is:", age)

print(age>18)
print(age<18)
print(age>=18)
print(age<=18)
print(age!=18)
print(age==18)


# In[4]:


#Conditional loops (if else)
age = int(input("Enter your age:"))
print("Your age is:", age)

if (age>18):
    print("You are an adult")  #This space is called indentation in python
else:
    print("You are a kid")


# In[12]:


# if elif else statements
num = int(input("Enter the value if num:"))
if (num<0):
    print("The num is negative")
elif (num==0):
    print("The num is zero")
else:
    print("The num is positive")
print("The value of num is:", num) #this statement is out of loop it will run in either case if the indent was given then it will only be true in case of else condition


# In[20]:


#Nested if statements
nos = int(input("Enter a number:"))
if (nos<0):
    print("The nos is negative")
elif (nos>0):
    if (nos<10):
        print("The nos is in between 0 - 10")
    elif (nos>10 and nos<=20):
        print("The nos is in between 10-20")
    else:
        print("The nos is greater than 20")
else:
    print("The nos is zero")


# In[1]:


time = int (input("Its o'clock"))
if (time>6):
    print("Good Morning")
elif (time>=12 and time<5):
    print("Good Afternoon")
elif (time>=5 and time<=8):
    print("Good Evening")
else:
    print("Good Night")


# In[ ]:




