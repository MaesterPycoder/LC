class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mx=0

        for i in range(0, len(prices)-1):
            lx = max(prices[i+1::])
            if(lx > prices[i]):
                lmx = lx - prices[i]
                if lmx > mx:
                    mx = lmx

        return mx
        
