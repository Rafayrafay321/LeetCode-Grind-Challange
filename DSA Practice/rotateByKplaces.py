class solution:
    def rotateByK(self, nums, k):
        # Rotating left

        """n = len(nums)
        k = k % n  # Ensure k is within bounds

        if k == 0:  # No rotation needed
            return nums  

        temp = nums[:k]  # Store first k elements  

        # Shift remaining elements to the left  
        for i in range(n - k):
            nums[i] = nums[i + k]

        # Put back the temp elements at the end  
        for i in range(n - k, n):
            nums[i] = temp[i - (n - k)]"""
        
        # Rotating Right 

        """n = len(nums)
        k = k % n

        if k == 0:
            return nums
        
        temp = nums[k + 1:n + 1] # storing the last k elements in the temp

        for i in range(n - 1, k - 1, - 1):
            nums[i] = nums[i - k]
            
        for i in range(0,k):
            nums[i] = temp[i]

        return nums"""

        # Optimal Approach
        def ReverseArr(self,nums,strr,end):
            while strr < end:
                temp = nums[strr]
                nums[strr] = nums[end]
                nums[end] = temp
                strr += 1
                end -= 1

        def rotateArr(self,nums,k):
            n = len(nums)
            self.ReverseArr(nums,0,n - 1)
            self.ReverseArr(nums,0,k - 1)
            self.ReverseArr(nums,k, n - 1)





            


        




ob = solution()

nums = [8,7,6,5,4]
k = 2

rotated = ob.rotateByK(nums,k)
for i in rotated:
    print(i , end = " ")