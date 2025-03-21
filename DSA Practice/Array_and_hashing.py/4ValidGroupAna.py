from collections import defaultdict
class solution:
    
    # Solving by SOrting
    # Time Complexity O(m * n log n)
    # Space Complexity O(m * n)
    def validAnaGram(self,strs):
    
        dict = defaultdict(list)
        for i in strs:
            dict["".join(sorted(i))].append(i)
        return dict.values()
    
    # Solving Using HashTable
    # Time Complexity = O(m * n)
    # Space Complexity = O(m.)
    
    def validAnaGram(self,strs):
        dict = defaultdict(list)
        for word in strs:
            lst = [0] * 26
            for char in word:
                lst[ord(char) - ord("a")] += 1
            lst = tuple(lst)
            dict[lst].append(word)
        return dict.values()



ob = solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(ob.validAnaGram(strs))