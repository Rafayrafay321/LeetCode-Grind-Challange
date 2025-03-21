class solution:
    # Brute Force Approach 
    # Time Complexity O(n)
    # Space Complexity O(n)

    def rotateOnePlace(self,nums):
        n = len(nums)
        temp = [0] * n
        for i in range(1,n):
            temp[i - 1] = nums[i]
        temp[n - 1] = nums[0]
        return temp

    # Optimal Approach
     # Time Complexity O(n)
    # Space Complexity O(1)

    def rotateOnePlace(self,nums):
        n = len(nums)
        x = nums[0]
        for i in range(n - 1):
            nums[i] = nums[i + 1]
        nums[n - 1] = x
        return nums

ob = solution()

nums = [7,6,4,3,2,1]
print(ob.rotateOnePlace(nums))