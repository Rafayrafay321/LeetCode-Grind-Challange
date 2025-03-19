from typing import *

#Given two strings s and t, return true if the two strings are anagrams 
# of each other, otherwise return false.

class solution:
    # Brute Force Approach
    # Time Complexity O(n log n + m log n)
    
    def quicSort(self,str):
        if len(str) <= 1:
            return str
        pivot = str[0]
        lesser = [x for x in str[1:] if x <= pivot]
        greater = [x for x in str[1:] if x > pivot]
        return self.quicSort(lesser) + [pivot] + self.quicSort(greater)
    
        

    def checkAngram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)
    
    
    # Optimal Approach Using HashTable (dict)
    # Time Complexity = O(n + m) 
    # Where n is the length of the string s and m is the length of string t

    def checkAnagram(self,str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        str1_dict = {}
        str2_dict = {}

        for i in range(len(str1)):
            str1_dict[str1[i]] = str1_dict.get(str1[i],0) + 1
            str2_dict[str2[i]] = str2_dict.get(str2[i],0) + 1
        return str1_dict == str2_dict

   




ob = solution()
        
str1 = "racecar"
str2 = "carrace"

print(ob.checkAnagram(str1,str2))
