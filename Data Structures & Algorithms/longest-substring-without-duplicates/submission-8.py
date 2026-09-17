class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        result=0
       

        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=i

            else:
                left=  max(left , seen[s[i]]+1)
                seen[s[i]]=i
            length=i-left+1
            if length>=result:
                result=length
        return result           
                
                

        
        
        
        