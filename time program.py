#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
timestamps = time.strftime('%H:%M:%S')
print(timestamps)
timestamps1 = int(time.strftime('%H'))
print(timestamps1)
timestamps = int(time.strftime('%M'))
print(timestamps)
timestamps = int(time.strftime('%S'))
print(timestamps)
if (timestamps1>5 and timestamps1<12):
    print("Good Morning!")
elif (timestamps1>=12 and timestamps1<17):
    print("Good Afternoon!")
elif (timestamps1>=17 and timestamps1<20):
    print("Good Evening!")
else:
    print("Good Night!")


# In[ ]:





# In[ ]:





# In[ ]:




