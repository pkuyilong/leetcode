#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;










class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }
        if (strs.size() == 1)
            return strs[0];

        int len = INT_MAX;
        for (int i = 0; i < strs.size(); i++) {
            int sz = strs[i].length();
            len = min(sz, len);
        }
        // 比较的位置
        int i = 0;
        for (; i < len; i++) {
            // 字符串
            for (int j = 0; j < strs.size() - 1; j++) {
                if (strs[j][i] != strs[j+1][i]) {
                    return strs[0].substr(0, i);
                    break;
                }
            }
        }
        return strs[0].substr(0, i);
    }
};


int main() {
    vector<string> strs = {"fly", "flower", "flight"};

    // Solution s = Solution();
    // string res = s.longestCommonPrefix(strs);
    // cout << res << endl;
    // cout << "res is " <<  res << endl;
    string s  = "hello";
    cout << s.substr(0,1) << endl;
    sleep(5);
}
