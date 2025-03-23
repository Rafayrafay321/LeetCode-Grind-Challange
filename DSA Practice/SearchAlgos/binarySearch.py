class Solution:
    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1  # Correct variable names

        while low <= high:
            mid = (low + high) // 2  # Calculate mid correctly

            if nums[mid] == target:
                return mid  # Target found, return index
            elif nums[mid] > target:
                high = mid - 1  # Move the upper bound down
            else:
                low = mid + 1  # Move the lower bound up

        return -1  # Target not found


        
         
ob = Solution()
nums = [1,2,3,4,5,6]
target = 6
print(ob.binary_search(nums,target))
