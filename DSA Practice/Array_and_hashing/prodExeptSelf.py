from typing import *
class solution:
    def prodExcptSelf(self, nums: List[int]) -> List[int]:
        # Brute Forece Approach
        # Time Complexity: O(n^2)
        # Space Complexiy: O(n)
        ans = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            ans.append(prod)
        return ans

       
    def prodExcptSelf(self, nums: List[int]) -> List[int]:

        # Better Approach Approach 
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # suffix
        n = len(nums)
        suffix = [1] * n
        for i in range(1,n):
            suffix[i] = suffix[i - 1] * nums[i - 1]

        # Finding the prefix:
        prefix = [1] * n
        for i in range(n-2,-1,-1):
            prefix[i] = prefix[i + 1] * nums[i + 1]

        # Main loop for product
        ans = []
        for i in range(n):
            ans.append(suffix[i] * prefix[i])
        return ans

    def prodExcptSelf(self, nums: List[int]) -> List[int]:
        # Optimal Approach
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        ans = [1] * len(nums)

        # prefix => Ans

        for i in range(1,len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        # Suffix => Ans
        
        suffix = 1
        for i in range(len(nums) - 1, -1 , -1):
            ans[i] *= suffix
            suffix *= nums[i]
            

        return ans

        


            


ob = solution()

nums = [1,2,3,4]

print(ob.prodExcptSelf(nums))
            