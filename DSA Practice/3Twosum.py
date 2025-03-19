from typing import *

class solution:
    # Brute force Approach
    # Time Complexity O(n^2)
    # Space complexity O(1)

    def twoSum(self,nums: List[int] , target: int ) -> List[int]:
        for i in range(len(nums)):
            for j in range( i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    # Optimal Approach
    # Time Complexity O(n)
    # Space Complexity O(n)

    def twoSum(self, nums: List[int], target: int ) -> List[int]:

        hashT = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashT:
                return [hashT[diff],i]
            hashT[n] = i
            



ob = solution()
nums = [2,7,11,5]
target = 9
print(ob.twoSum(nums,target))

