#!/usr/bin/env python
# coding: utf-8

# 4.1

# In[1]:


secret = 8
guess = 4

if guess == secret:
    print("Just Right")
elif guess < secret:
    print("Too Low")
else:
    print("Too High")


# 4.2

# In[2]:


small = False
green = True

if green:
    if small:
        print("pea")
    else:
        print("watermelon")
else:
    if small:
        print("cherry")
    else:
        print("pumpkin")


# 6.1

# In[3]:


numbers = [3, 2, 1, 0]
for number in numbers:
    print(number)


# 6.2

# In[5]:


guess_me = 7
number = 1
while number <= guess_me:
    if number < guess_me:
        print("Too low")
        number += 1
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("oops!")


# 6.3

# In[7]:


guess_me = 5
for number in range(10):
    if number < guess_me:
        print("Too low")
        number += 1
    elif number == guess_me:
        print("Found it")
        break
    else:
        print("oops!")
        break


# In[ ]:




