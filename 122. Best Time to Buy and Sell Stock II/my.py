class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxp = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                lxp = prices[i] - buy
                if lxp > 0:
                    mxp += lxp
                    buy = prices[i]
        
        return mxp
