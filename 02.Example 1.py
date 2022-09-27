#!/usr/bin/env python
# coding: utf-8

# In[1]:


D_d = 68
o_d = 111
g_d = 103

D_b = bin(D_d)
o_b = bin(o_d)
g_b = bin(g_d)

print(D_b, o_b, g_b)


# In[2]:


D_b = D_b.replace('0b', '')
o_b = o_b.replace('0b', '')
g_b = g_b.replace('0b', '')

print(D_b, o_b, g_b)


# In[3]:


D_b = [b for b in D_b]
o_b = [b for b in o_b]
g_b = [b for b in g_b]

print(D_b)
print(o_b)
print(g_b)


# In[4]:


D_b.reverse()
o_b.reverse()
g_b.reverse()

print(D_b)
print(o_b)
print(g_b)


# In[5]:


D_P = len([b for b in D_b if b == '1']) % 2
o_P = len([b for b in o_b if b == '1']) % 2
g_P = len([b for b in g_b if b == '1']) % 2

print(D_P, o_P, g_P)


# In[6]:


D_ds = D_b.copy()
D_ds.append(str(D_P))
D_ds.append('1')
D_ds.append('1')

o_ds = o_b.copy()
o_ds.extend([str(o_P), '1', '1']) # note extend may be used to append multiple elements at once

g_ds = g_b.copy()
g_ds.extend([str(g_P), '1', '1'])

print(D_ds)
print(o_ds)
print(g_ds)


# In[7]:


D_ds.insert(0, '0')
o_ds.insert(0, '0')
g_ds.insert(0, '0')

print(D_ds)
print(o_ds)
print(g_ds)


# In[8]:


message = D_ds.copy()
message.extend(o_ds)
message.extend(g_ds)

print(message) # answer to first part


# In[9]:


baud_rate = 9600
time_per_bit = 1 / baud_rate

print(time_per_bit)


# In[10]:


total_time = len(message)*time_per_bit

print(total_time, 's') # answer to second part
print(total_time*1000, 'ms')

