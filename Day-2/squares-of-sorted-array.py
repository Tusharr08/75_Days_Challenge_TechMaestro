import collections
class Solution:
    def sortedSquares(self, nums):
        ans=collections.deque()
        
        l,r = 0 , len(nums)-1
        
        while(l<=r):
            
            left, right= abs(nums[l]) , abs(nums[r])
            
            if left>right:
                ans.appendleft(left**2)
                l+=1
            else:
                ans.appendleft(right**2)
                r-=1
                
        return list(ans)

if __name__ == "__main__":
    print(Solution().sortedSquares([int(x) for x in input().split()]))