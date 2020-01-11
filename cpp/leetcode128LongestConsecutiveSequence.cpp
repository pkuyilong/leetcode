#include <iostream>
#include <vector>
#include <unordered_set>
#include <unistd.h>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        unordered_set<int> s(nums.begin(), nums.end());
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            int tmp = 1;
            if (s.count(nums[i] - 1)) continue;
            else {
                while (s.count(nums[i]+1)) {
                    tmp += 1;
                    nums[i] += 1;
                }
            }
            res = max(res, tmp);
        }
        return res;
    }
};

int main()
{
    vector<int> nums = { 1,2,6,4,3};
    Solution s;
    cout << s.longestConsecutive(nums) << endl;
    sleep(4);
    return 0;
}
