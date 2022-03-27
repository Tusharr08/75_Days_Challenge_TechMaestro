class Solution:
    def maxProfit(self, prices):
        profit=0
        
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+= prices[i]-prices[i-1]
                
        return profit

if __name__ == "__main__":
    print(Solution().maxProfit([int(x) for x in input().split()]))