#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
      int count=0;
    for(int i=1;i<nums.size();i++)
    {
        if(nums[i]==nums[i-1])
            count++;
        else
            nums[i-count]=nums[i];
    }
    for(int i=0;i<nums.size();i++)
        cout<<nums[i]<<" ";
    
    return nums.size()-count;
    }
};

int main()
{
    vector<int> arr={1,1,2};
    Solution s1;
    cout<<s1.removeDuplicates(arr);
}