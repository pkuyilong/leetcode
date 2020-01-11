#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> intermediate;
        vector<vector<int> > res;
        if (nums.size() == 0)
            return res;
        for (int i = 0; i < nums.size()+1; i++)
        {
            dfs(nums, i, 0, intermediate, res);
        }
        return res;

    }
    void dfs(vector<int> nums, int total_num, int num_idx,
            vector<int> intermediate,
            vector<vector<int>> &res)
    {
        if (intermediate.size() == total_num)
        {
            res.push_back(intermediate);
            return;
        }
        for (int i = num_idx; i < nums.size(); i++)
        {
            intermediate.push_back(nums[i]);
            dfs(nums, total_num, i+1, intermediate, res);
            intermediate.pop_back();
        }
    }
};
// class Solution {
//  public:
//      std::vector<std::vector<int> > subsets(std::vector<int>& nums)
//      {
//          std::vector<int> intermediate;
//          std::vector<std::vector<int>> res;
//          for (int i = 0; i < nums.size() + 1; i++)
//          {
//              dfs(nums, i, 0, intermediate, res);
//          }
//          return res;
//      }
//
//      void dfs(vector<int> nums, int total_num, int now_num, vector<int> intermediate, vector<vector<int>> &res)
//      {
//             if (intermediate.size() == total_num)
//             {
//                 res.push_back(intermediate);
//                 return;
//             }
//             for (int i = now_num; i < nums.size(); i++)
//             {
//                 intermediate.push_back(nums[i]);
//                 dfs(nums, total_num, i + 1, intermediate, res);
//                 intermediate.pop_back();
//             }
//      }
//      cout << "happy new year" << endl;
// };

//class Solution {
// public:
//     std::vector<std::vector<int> > subsets(std::vector<int>& nums) {
//         std::vector<std::vector<int>> res;
//         return res;
//     }
//
//     std::vector<std::vector<int>> dfs(std::vector<int> nums,
//         int total_num,
//         int n,
//         std::vector<int> intermediate,
//         std::vector<std::vector<int>> &res)
//     {
//         if (intermediate.size() == total_num) {
//             res.push_back(intermediate);
//             return res;
//         }
//         for (int i = n; i < nums.size(); i++)
//         {
//             intermediate.push_back(nums[i]);
//             dfs(nums, total_num, i+1, intermediate, res);
//             intermediate.pop_back();
//         }
//         return res;
//     }
// };


int main()
{
    Solution s;
    std::vector<int> nums = {1,2,3,4,5};
    std::vector<int> intermediate;
    std::vector<std::vector<int>> res;
    std::vector<std::vector<int>> out = s.subsets(nums);
    for (auto &i : out)
    {
        for (auto &j : i)
        {
            cout << j << endl;
        }
        cout << "...." << endl;
    }
    sleep(5);
}
