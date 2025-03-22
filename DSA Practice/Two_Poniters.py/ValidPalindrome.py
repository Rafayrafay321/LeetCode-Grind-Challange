from typing import *
class Solution:
    
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def reverse(self,string):
        return string[::-1]  
    
    def validPalindorme(self,stringg: str) -> bool:
        stringg = "".join(c.lower() for c in stringg if c.isalnum())
        revString = self.reverse(stringg)
        return stringg == revString
    
    # Optimal Approach
    # Time Complexity: O(N)
    # Space Complexity: O(1)

    def isAlphaNum(self,c: str) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or
        ord("0") <= ord(c) <= ord("9"))
    
    def validPalindorme(self,s: str) -> bool:
        start , end = 0 , len(s) - 1
        while start < end:
                while start < end and not self.isAlphaNum(s[start]):
                    start += 1
                while end > start and not self.isAlphaNum(s[end]):
                     end -= 1
                if s[start].lower() != s[end].lower():
                     return False
                start , end = start + 1, end - 1
        return True
                

            
        

ob = Solution()

sstring = "was it a car or a cat I saw"
print(ob.validPalindorme(sstring))