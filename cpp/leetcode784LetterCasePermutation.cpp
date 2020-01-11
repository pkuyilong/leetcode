
#include <iostream>
#include <unistd.h>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> ans;
        helper(S, 0, ans);
        return ans;
    }

    void helper(string S, int idx, vector<string> &ans) {
        if (idx == S.size()) {
            ans.push_back(S);
            cout << S << endl;
            return;
        }
        helper(S, idx+1, ans);
        if (isalpha(S[idx])) {
            S[idx] ^= 32;
            helper(S, idx+1, ans);
            S[idx] ^= 32;
        }
    }
};

int main() {
    Solution s = Solution();
    vector<string> ans = s.letterCasePermutation("a1b2");
    sleep(10);
}
