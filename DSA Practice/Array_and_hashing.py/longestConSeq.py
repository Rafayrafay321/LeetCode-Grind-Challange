import sys
from typing import *
class solution:
    def quicSort(self,nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        lesser = [x for x in nums[1:] if x <= pivot]
        greater = [x for x in nums[1:] if x > pivot]

        return self.quicSort(lesser) + [pivot] + self.quicSort(greater)
           
    def longestConSeq(self,nums: List[int]) -> int:
        # Brute Force Sorting Approach
        # Time Complexity: O(N log N)

        if not nums:
            return 0
        
        nums = self.quicSort(nums)
        longConSec = 1
        currentstreak = 1
        for num in range(1,len(nums)):
            if nums[num] == nums[num - 1] + 1:
                currentstreak += 1
            elif nums[num] != nums[num - 1]:
                longConSec = max(currentstreak,longConSec)
                currentstreak = 1
        return max(longConSec,currentstreak)
            
            
    def longestConeq(self,nums):
        # Better Approach 
        my_set = set(nums)
        max_len = 0
        for num in my_set:
            if num - 1 not in my_set:
                current_num = num
                current_len = 1
                while current_num + 1 in my_set:
                    current_len += 1
                    current_num += 1
                
                max_len = max(max_len,current_len)
        return max_len




        
      
        

ob = solution()

nums = [100,4,200,1,3,2]
print(ob.longestConeq(nums))
            