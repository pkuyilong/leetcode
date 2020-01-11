#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> intermediate;
        for (int i = 0; i <= nums.size(); i++)
        {
            dfs(nums, i, 0, intermediate, res);
        }
        return res;
    }
    void dfs(vector<int> nums, int total_num, int idx,
    vector<int> intermediate,
    vector<vector<int>> &res)
    {
        if (intermediate.size() == total_num)
        {
            res.push_back(intermediate);
            return;
        }

        for (int i = idx; i < nums.size(); i++)
        {
            intermediate.push_back(nums[i]);
            dfs(nums, total_num, i+1, intermediate, res);
            // dont forget this
            intermediate.pop_back();
        }
    }
};

int main()
{
    vector<int> nums = {1,2,3};
    Solution s;
    vector<vector<int>> res;
    res = s.subsets(nums);
    for (auto &i : res)
    {
        for (auto &j : i)
        {
            cout << j << endl;
        }
        cout << "*****" << endl;
    }
    sleep(500);

}



// version 2.0
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> intermediate;
        if (nums.size() == 0)
            return ans;
        for (int i = 0; i <= nums.size(); i++) {
            helper(nums, 0, i, intermediate, ans);
        }
        return ans;
    }
    void helper(const vector<int> &nums, const int idx, const int total_num, vector<int> intermediate, vector<vector<int>> &ans) {
        if (intermediate.size() == total_num) {
            ans.push_back(intermediate);
            return;
        }
        for (int i = idx; i < nums.size(); i++) {
            intermediate.push_back(nums[i]);
            helper(nums, i+1, total_num, intermediate, ans);
            intermediate.pop_back();
        }
    }
};
