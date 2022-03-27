class Solution:
    def pivotIndex(self, nums):
        n=len(nums)
        s=sum(nums)
        s2=0
        print(s,s2)
        for i in range(n):
            s-=nums[i]
            if s==s2:
                return i
            s2+=nums[i]
            print(s,s2)
            
        return -1
if __name__ == "__main__":
    print(Solution().pivotIndex([int(x) for x in input().split()]))