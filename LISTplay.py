
# coding: utf-8

# In[41]:


dummy_list=[99, 1, 45, 1, 10, 15, 4]


# Number 2

# In[42]:


print(dummy_list)


# In[43]:


dummy_list.reverse()


# In[44]:


print(dummy_list)


# In[45]:


dummy_list_2 = [2, 200, 16, 4, 1, 0, 9.45, 45.67, 90, 12.01, 12.02]


# In[46]:



i = 0
while i < len(dummy_list_2):
    dummy_list.append(dummy_list_2[i])
    i += 1

    


# In[47]:


print(dummy_list)


# In[48]:


dummy_list.count(dummy_list[1])


# In[49]:


#creating dictionary
dummy_dict={}
i=0
while i<len(dummy_list):
  dummy_dict[dummy_list[i]]=dummy_list.count(dummy_list[i])
  i += 1


# In[50]:


print(dummy_dict)


# In[52]:


dummy_list.sort()

print(dummy_list)


# In[54]:


dummy_list.sort(reverse= True)
print(dummy_list)


# In[60]:


x=200
dummy_list.remove(x)
print(dummy_list)



# In[61]:


x=20
dummy_list.remove(x)
print(dummy_list)


# In[62]:


x=5
del dummy_list[x]
print(dummy_list)


# In[63]:


x=50
del dummy_list[x]
print(dummy_list)


# In[65]:


del dummy_list[:]
print (dummy_list)

