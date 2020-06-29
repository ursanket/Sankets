#!/usr/bin/env python
# coding: utf-8

# In[38]:


import csv
def st(name, roll_no):
    std = [name, roll_no]
    with open("std.csv","a+", newline="") as file:
     writer = csv.writer(file)
     writer.writerow(std)


# In[41]:


st("Sanket", 70)


# In[ ]:




