class solution:
    def moveZero(self,nums):
        # Brute Force Approach 
        # Time Complexity: O(2N)
        # Time Complexity: O(N)

        n = len(nums)
        temp = [0] * n
        j = 0
        k = 0
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])
                j += 1
        n1 = len(temp)
        for i in range(n1):
            nums[i] = temp[k]
            k += 1
        for i in range(n1,n):
            nums[i] = 0
        return nums

    def swap(self,nums,start,end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        

    def moveZero(self,nums):

    # Optimal Solution Using the Two-Pointer
    

        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                self.swap(nums,j,i)
                j += 1
        return nums

           

    


    
ob = solution()

nums = [3,0,0,8,1,2,3]
print(ob.moveZero(nums))
