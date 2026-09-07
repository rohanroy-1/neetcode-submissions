class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
       
        i=0
        j=len(heights)-1
        
        
        while j>i:
            width = j-i
            Area = min(heights[i],heights[j]) * width
            if maxArea<Area:
                maxArea=Area
            
            elif heights[i]>heights[j]:
                j-=1

            else:
                i+=1 
            



        return maxArea        

              
                 



                
        return maxArea    




        
