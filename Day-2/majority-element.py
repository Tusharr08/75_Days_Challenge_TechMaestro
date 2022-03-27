class Solution:
    def majorityElement(self, nums):
        n=len(nums)
        freq={}
        for i in nums:
            freq[i]=1+ freq.get(i,0)
        
        for k,v in sorted(freq.items(), key=lambda x:x[1], reverse=True):
            if v>(n//2):
                return k
        
        return 0

if __name__ == "__main__":
    print(Solution().majorityElement([int(x) for x in input().split()]))