from typing import *
class solution(object):

    # Brute Force Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

    def twoSumII(self,nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums[i] + 1,nums[j] + 1]
        return []
    
                
    # Using Binary Search
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)

    def twoSumII(self,nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            low , up = i + 1 , len(nums) - 1
            temp = target - nums[i]
        while low < up:
            mid = (low + up) // 2
            if nums[mid] == temp:
                return[i + 1,mid + 1]
            elif  nums[mid] > temp:
                up = mid - 1
            else:
                low = mid + 1
        return []
    
    # Using the Two Pointer 
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def twoSumII(self,nums: List[int], target: int) -> List[int]:
        low , up = 0 , len(nums) - 1
        while low < up:
            total = nums[low] + nums[up]
            if total > target:
                up -= 1
            elif total < target:
                low += 1
            else:
                return [low , up]
        return []

                    