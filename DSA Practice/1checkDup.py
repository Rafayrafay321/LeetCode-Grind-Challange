# Check for the duplicate in the list
from typing import List


class solution:       
    # Brute force approch
    # Time complexity: O(n^2)
    # Space Complexity: O(1)

    def checkfordup(self,nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                if nums[i] == nums[j]:
                    return True
        return False

    # (Little Optimal Approach) Sorting then Comparing
    # Time complexity: O(n log n)
    # space Complexity: O(n)
    
    def quickSort(self,arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return self.quickSort(lesser) + [pivot] + self.quickSort(greater)
    
    def checkDup(self,arr):
        sorted_arr = self.quickSort(arr)
        for i in range(1,len(sorted_arr)):
            if sorted_arr[i] == sorted_arr[i - 1]:
                return True
        return False

    # Optimal Approach to Solve this problem Using the set
    # Time Complexity O(n)
    # Space Complexity O(n)

    def CheckDup(self,nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

    # Most Optimal Solutin for this problem is by using the len() operator:
    # Time Complexity O(n)
    # Space Complexity O(n)

    def CheckDup(self,nums):
        return len(set(nums)) < len(nums)


    


lst1 = [1,2,3,4]
ob = solution();

print(ob.CheckDup(lst1))


