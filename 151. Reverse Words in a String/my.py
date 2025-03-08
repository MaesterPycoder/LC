class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        lst = s.split(" ")
        lst = lst[::-1]
        nlst = []
        for ele in lst:
            if ele != "":
                nlst.append(ele)
        return " ".join(nlst)        
