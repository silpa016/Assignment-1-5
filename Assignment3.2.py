
# coding: utf-8

# In[5]:


string_1 = "ACADGILD"
comp_list = [x for x in string_1]
print(comp_list)


# In[6]:


input_list = ['x','y','z']
result = [item*num for item in input_list for num in range(1,5)]
print(result)


# In[4]:


input_list = ['x','y','z']
result = [item*num for num in range(1,5) for item in input_list]
print(result)


# In[7]:


input_list = [2,3,4]
result = [[item+num] for item in input_list for num in range(0,3)]
print(result)


# In[8]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print(result)


# In[18]:


input_list=[1,2,3]
result = [(a,b) for b in input_list for a in input_list]
print(result)

