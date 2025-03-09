from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        print(words)
        
        # Caluculate word lengths
        word_lens = [len(word) for word in words]
        print(word_lens)

        # Prepare lines
        lst = []
        prf = -1
        nlst = []
        
        i = 0
        while i < len(word_lens):
            cl = prf + word_lens[i] + 1
            print(f"for index {i} : value {word_lens[i]} => {cl}")
            
            if (cl < maxWidth):
                if ((i+1)<len(word_lens) and (cl+1+word_lens[i+1])>maxWidth and len(nlst)==1):
                    nlst.append(i)
                    print(f"==============case 2 :=> {nlst}\n\n")
                    lst.append(nlst)
                    prf = -1
                    nlst = []
                else:
                    print("case 1")
                    prf = cl
                    nlst.append(i)
                i+=1
            
            elif cl == maxWidth:
                nlst.append(i)
                print(f"==============case 3 :=> {nlst}\n\n")
                lst.append(nlst)
                prf = -1
                nlst = []
                i+=1
                
            else:
                print(f"==============case 4 :=> {nlst}\n\n")
                lst.append(nlst)
                prf = -1
                nlst = []
            
            if i+1>len(word_lens) and len(nlst)>0:
                print("Final case")
                lst.append(nlst)
        
        print(lst)
        
        
        # Find Spaces
        dc = []
        for line in lst:
            char_count = 0
            for wid in line:
                char_count += word_lens[wid]
            space_count = maxWidth - char_count
            extra_spaces = space_count - len(line) + 1
            dc.append(extra_spaces)
        
        print(f"spaces => {dc}")
        
        # Final Strings
        fs = []
        for i in range(len(lst)):
            es = dc[i]
            st = ""
            print(f"\n\nprocessing words: {lst[i]}\n\n")
            if (i == len(lst)-1) or (len(lst[i])==1):
                for j in range(len(lst[i])):
                    if j == 0:
                        st = st + words[lst[i][j]]
                    else: 
                        st += " " +words[lst[i][j]]
                rs = maxWidth - len(st)
                st += " "*rs
            else:
                k = (es // (len(lst[i]) - 1)) if (len(lst[i]) - 1) > 0 else 0
                remaining = (es % (len(lst[i]) - 1)) if (len(lst[i]) - 1) > 0 else 0
                for j in range(len(lst[i])):
                    if j == 0:
                        st = st + words[lst[i][j]]
                    else: 
                        st = st + " " + " " * k + " "*(1 if remaining > 0 else 0) + words[lst[i][j]]
                        remaining -= 1
            
            fs.append(st)
        
        print("\n\n\n\n")
        for ele in fs:
            if(len(ele)==maxWidth):
                print(f"\"{ele}\" => true {len(ele)}")
            else:
                print(f"\"{ele}\" => false {len(ele)}")
        


if __name__ == "__main__":
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # maxWidth = 16
    
    # words = ["What","must","be","acknowledgment","shall","be"]
    # maxWidth = 16
    
    words = ["The","important","thing","is","not","to","stop","questioning.","Curiosity","has","its","own","reason","for","existing."]
    maxWidth = 17
    
    # words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    # maxWidth = 20
    
    s = Solution()
    s.fullJustify(words, maxWidth)

        
