class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mxp=0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                mxp = max(mxp, prices[i] - buy)


        return mxp
        
