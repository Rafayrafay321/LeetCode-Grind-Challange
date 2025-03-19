class solution:
    def largElement(self,nums):
        n = len(nums)
        smallest = float('-inf')  # Represents negative infinity
        for i in range(n):
            if nums[i] > smallest:
                smallest = nums[i]
        return smallest

ob = solution()
nums = [5,3,2,1,9]
print(ob.largElement(nums))

