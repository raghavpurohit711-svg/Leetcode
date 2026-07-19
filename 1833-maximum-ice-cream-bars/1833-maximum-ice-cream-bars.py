class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=x=i=0
        while x<=coins and i<len(costs):
            if x+costs[i]<=coins:
                count+=1
                x+=costs[i]
            i+=1
        return count