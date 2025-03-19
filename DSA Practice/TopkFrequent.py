class solutions:
    def topKfrequent(self,nums,k):
        # Using the Sorting
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)

        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num,0)
        lst = []
        for num , cnt in dic.items():
            lst.append([cnt,num])
        lst.sort()
        
        res = []
        while len(res) < k:
            res.append(lst.pop()[1])
        return res
    
    def topKfrequent(self,nums,k):
        # Using the Modified Bucket Sort
        # Time Complexity O(n)
        # Space Complexity O(n)

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num,0)

        for val , cnt in count.items():
            freq[cnt].append(val)
        
        n = len(freq)
        res = []
        for i in range(n - 1,0,-1):
            for j in freq[i]:
                res.append(i)
                if len(res) == k:
                    return res




        
        

       

ob = solutions()
nums = [1,2,2,3,3,3]
k = 2
print(ob.topKfrequent(nums,k))
