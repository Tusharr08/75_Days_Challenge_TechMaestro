#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minsofar=INT_MAX, maxprofit=INT_MIN;
        
        for(int i=0;i<prices.size();i++)
        {
            minsofar= min(minsofar,prices[i]);
            maxprofit= max(maxprofit, prices[i]-minsofar);
            //cout<<minsofar<<" "<<maxprofit<<endl;
        }
        
        return maxprofit;
    }
};

int main()
{
    vector<int> arr;
    for(auto x:arr)
    cin>>x;
    Solution x;
    cout<<x.maxProfit(arr);       
}