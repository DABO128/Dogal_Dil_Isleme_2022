#!/usr/bin/env python
# coding: utf-8

# In[11]:


import re
email = input('Lütfen Email adressinizi girin:')
eReg = "(\w+)@((\w+\.)+(edu.tr))"
r = re.match(eReg,email)
print("Kullancı Adı:" + r.group(1))
print("Domain Adı:" + r.group(2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




