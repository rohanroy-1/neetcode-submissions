class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit=0
        left=0
        right=left+1
        

        while right<len(prices):
            profit = prices[right]-prices[left]
            if max_profit < profit:
                max_profit = profit
                right+=1
            elif prices[right]<prices[left]:
                left+=1    
                
            else:
                
                right+=1
        return max_profit        

                



        
        


        
        