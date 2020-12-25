#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution:
    def twosum(self, nums:List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range (i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return([i,j])

            
        
        


# In[ ]:




