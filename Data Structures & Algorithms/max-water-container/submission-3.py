class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        area = 0 
        while l < r:
            area = max(area,(min(heights[l],heights[r]))*(r-l))
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return area