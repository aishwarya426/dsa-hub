class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxcount=0
        count =0
        for i in range(0,k):
            if s[i] =='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                count+=1
        maxcount=count
        i=0
        j=i+k-1
        while j+1<len(s):
            if s[i] in 'aeiou' and s[j+1] not in 'aeiou':
                count-=1
            elif s[i] not in 'aeiou' and s[j+1] in 'aeiou':
                count+=1
            if count> maxcount:
                maxcount=count
            i+=1
            j+=1
        return maxcount
        