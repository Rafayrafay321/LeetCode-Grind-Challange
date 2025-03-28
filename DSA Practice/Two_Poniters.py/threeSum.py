from typing import *
class solution:
    def threeSumII(self,nums: List[int]) -> List[List[int]]:
        # Brute Force Approach
        # Time Complexity: O(n^3)

        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i] ,nums[j] , nums[k]]
                        res.add(tuple(sorted(temp)))
        return [list(i) for i in res]
    

    def threeSumII(self, nums: List[int]) -> List[List[int]]:
        
        # Optimal Solution
        # Time Complexity: O(n ^ 2)
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number
            
            l, r = i + 1, len(nums) - 1  # initialization of pointers
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])  
                    l += 1

                    # Skip duplicates for the second number
                    while l < r and nums[l] == nums[l - 1]:  
                        l += 1
        return res



