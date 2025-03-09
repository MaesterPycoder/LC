class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zs = ""

        find_zl = (2*numRows) - 2
        
        for nr in range(numRows):
            i = nr
            while i < len(s):  
                zs += s[i]
                if nr>0 and nr<numRows-1:
                    k = i + 2 * (numRows - nr-1)
                    if k < len(s):
                        zs += s[k]
                    
                i = (i + find_zl)
        
        return zs


