#!/usr/bin/env python
# coding: utf-8

# 7.4

# In[1]:


things = ["mozzarella", "cinderella", "salmonella"]


# 7.5

# In[4]:


things[1] = things[1].capitalize()
print(things)


# Yes, the element was changed to so 'Cinderella' is capitalized

# 7.6

# In[5]:


things[0] = things[0].upper()
print(things)


# 7.7

# In[6]:


del things[-1]
print(things)


# 9.1

# In[10]:


def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())


# 9.2

# In[12]:


def get_odds():
    for number in range(10):
        if number % 2 ==1:
            yield number
counter = 0
for odd_number in get_odds():
    counter += 1
    if counter == 3:
        print("The third odd number is " + str(odd_number))
        break


# In[ ]:




