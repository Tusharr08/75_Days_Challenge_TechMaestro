class Solution:
    def twoSum(self, nums, target):
        f=[]
        x,y=0,0
        for i in range(len(nums)):
            if target-nums[i] in f:
                x=f.index(target-nums[i])
                y=i
            else:
                f.append(nums[i])
            #print(i,f,abs(target-nums[i]))
                
        return [x,y]
                
if __name__ == "__main__":
    print(Solution().twoSum([int(x) for x in input().split()], int(input())))