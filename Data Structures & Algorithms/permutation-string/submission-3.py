class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False 
        freq={}
        for c in range(len(s1)):
            freq[s1[c]]=freq.get(s1[c],0)+1

        for i in range(len(s1)):
            if s2[i] in freq:
                freq[s2[i]]-=1
            if all (values==0 for values in freq.values()):
                return True


        left=0
        for right in range(len(s1), len(s2)):
            if s2[right] in freq:
                freq[s2[right]]-=1 
            if s2[left] in freq:
                freq[s2[left]]+=1
            left += 1
            if all (values==0 for values in freq.values()):
                return True
        return False                
            
            
                
                
                

                
                
            

            



            
        

















