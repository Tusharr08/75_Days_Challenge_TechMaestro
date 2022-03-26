class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=1
        i=0
        while(i<n and j<n):
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                i+=1
            elif nums[i]!=0 and nums[j]==0:
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                i+=1
                j+=1
            #print(nums, i , nums[i], j, nums[j])
        
if __name__ == "__main__":
    print(Solution().moveZeroes([int(x) for x in input().split()]))