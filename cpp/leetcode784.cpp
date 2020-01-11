#include <iostream>
#include <vector>
#include <string>
#include <unistd.h>

using namespace std;
/*
   思路是 :
   从头开始遍历,
   a - > b  - > c - > d   -> 达到最低端之后返回上一层     这里的输出结果是 abcd
                    将这个位置翻转成大写    < -
                         - > 达到最低端之后返回上一层     这里的输出结果是 abcD
                < - < -    < - < -   <- < -  返回到c的位置
                -------------------------------->     abCd
                <----------------------------------
                -------------------------------->     abCD
                then  ************
*/
class Solution {
public:
    vector<string> permutation(string s) {
        vector<string> ans;
        helper(s, 0, ans);
        return ans;
    }
private:
    void helper(string s, const int idx, vector<string> &ans) {
        if (idx == s.size()) {
            ans.push_back(s);
            return;
        }
        helper(s, idx+1, ans);
        s[idx] ^= 32;
        helper(s, idx+1, ans);
        s[idx] ^= 32;
    }

};
int main() {
    string s = "abcd";
    Solution sol = Solution();
    vector<string> ans = sol.permutation(s);
    for (auto &item : ans) {
        cout << item << endl;
    }
    sleep(10);
}
