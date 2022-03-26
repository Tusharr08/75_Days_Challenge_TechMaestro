class Solution:
    def plusOne(self, digits):
        ans=[]
        for i in digits:
            ans.append(str(i))
        print(ans)
        s=''.join(ans)
        x=int(s)+1
        s=str(x)
        print(x,s)
        ans=[]
        for i in range(len(s)):
            ans.append(int(s[i]))
        print(ans)
        return ans

if __name__ == "__main__":
    print(Solution().plusOne([int(x) for x in input().split()]))