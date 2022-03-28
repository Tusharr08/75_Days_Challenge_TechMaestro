class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                sum=a+nums[l]+nums[r]
                
                if sum==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
                    
                elif sum>0:
                    r-=1
                else:
                    l+=1
        return res

if __name__ == "__main__":
    print(Solution().threeSum([int(x) for x in input().split()]))