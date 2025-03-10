class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mxp=0
        buy = prices[0]

        for i in range(1, len(prices)):
            if buy < prices[i]:
                mxp = max(mxp, prices[i]-buy)
            else:
                buy = prices[i]


        return mxp
