class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)

        while low<high:
            mid=low+(high-low)//2

            hours=0

            for i in range(len(piles)):
                hours+=math.ceil(piles[i]/mid)
            # there is no other case to handle equal and we need to check lesser then mid eventhough mid is the answer cuz we need minimum speed(no of bananas)
            if hours<=h:
                high=mid
            else:
                low=mid+1
        return low                
        