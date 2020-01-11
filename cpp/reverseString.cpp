#include <iostream>
#include <string>


using namespace std;
class Solution {
public:
    string reverseString(string s) {
        if (s.length() == 1) {
            return s;
        }
        string res = reverseString(s.substr(1));
        return res+s[0];
    }

};

int main() {
    string s("hello world");
    Solution sol = Solution();
    string res = sol.reverseString(s);
    cout << res << endl;
}
