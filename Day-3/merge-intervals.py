class Solution:
    def merge(self, intervals):
        intervals.sort()
        start=intervals[0][0]
        end=intervals[0][1]
        #print(intervals,start,end)
        i=0
        n=len(intervals)
        ans=[]
        while(i<n):
            if end>=intervals[i][0]:
                end=max(end,intervals[i][1])
            else:
                ans.append([start,end])
                #print(ans)
                start=intervals[i][0]
                end=intervals[i][1]
            i+=1
        ans.append([start,end])   
        return ans

if __name__ == "__main__":
    i=[[1,4],[4,5]]
    print(Solution().merge(i))