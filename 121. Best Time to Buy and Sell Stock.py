class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L,R = 0, 1
        diff = 0
        while R < len(prices):
            if prices[L]<prices[R]:
                diff = max(diff,prices[R]-prices[L])
            else:
                L=R
            R+=1
        return diff
            
