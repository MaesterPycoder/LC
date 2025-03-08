# Using Binary search tactic

import math as m

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def calc_power(x, n):
            if n == 0:
                return 1

            if x == 0:
                return 0
            
            res = calc_power(x, n//2)
            res =  res * res
            if n%2 != 0:
                res = res * x
            return res
        
        if n < 0:
            x = 1/x
        
        return calc_power(x, abs(n))
        

