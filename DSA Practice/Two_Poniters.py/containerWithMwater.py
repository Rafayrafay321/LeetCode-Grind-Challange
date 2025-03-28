from typing import *
class solution:

    # Brute Force Approach
    # Time Complexity: O(n^2)

    def maxArea(self,height: list[int]) -> int:
        n = len(height)
        maxArea = 0
        for i in range(n):
            for j in range(i + 1 , n):
                width = j - i
                currHeight = min(height[i],height[j])
                currArea = width * currHeight
                maxArea = max(currArea , maxArea)
        return maxArea
