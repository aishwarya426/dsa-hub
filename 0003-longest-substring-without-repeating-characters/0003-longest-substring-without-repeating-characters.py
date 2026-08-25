class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        done=set()
        count =0
        maxcount=0
        i=0
        j=0
        while j<len(s) and i<len(s):
            if s[j] not in done :
                done.add(s[j])
                count+=1
                if count>maxcount:
                    maxcount=count

            else:
                while s[j] in done:     
                    done.remove(s[i])
                    i+=1
                    count-=1
                done.add(s[j])
                count+=1
                

            j+=1
            
        return maxcount



        
        