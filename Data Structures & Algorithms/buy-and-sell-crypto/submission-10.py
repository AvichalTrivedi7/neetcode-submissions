class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==1:
            return 0
    
        minx = 101
        hold = 0
        for i in range(len(prices)):
            minx = min(minx, prices[i])
            hold = max((prices[i]-minx), hold)
        return hold

        