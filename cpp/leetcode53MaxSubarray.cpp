class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0) {
            return INT_MIN;
        }
	// 注意初始化, 不要一想起来初始化就是0
        int rval = INT_MIN;
        vector<int> res(nums.size(), 0);
        res[0] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (res[i-1] < 0) {
                res[i] = nums[i];
            }
            else {
                res[i] = res[i-1]  + nums[i];
            }
        }
        for (auto &item : res) {
            rval = max(rval, item);
        }
        return rval;
    }
};
