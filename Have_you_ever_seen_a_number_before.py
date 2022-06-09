#!/usr/bin/env python
# coding: utf-8

# In[34]:


x = input().split(' ')
unique_number = set()
for i in x:
    if i in unique_number:
        print('YES')
        unique_number.add(i)
    else:
        print('NO')
        unique_number.add(i)


# In[ ]:




