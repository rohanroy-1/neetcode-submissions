class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        seen={}
        i=0
        j=i+1
        long_count=1

        seen[s[i]]=i

        while j<len(s):
            if s[j] in seen :
                i=max(i,seen[s[j]]+1)

            seen[s[j]]=j 

            count=j-i+1

            if count>long_count:
                long_count=count 
                
            j+=1
        return long_count    
               
                  
            
        
        

        