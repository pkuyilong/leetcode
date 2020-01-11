#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <unistd.h>


using namespace std;
class Solution()
{
public:
    bool wordBreak(string &s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
    }
    wordBreak(string &s, unordered_set<string> &dict){
        if (dict.count(s)) return mem_[s] = true;
        if (mem_.count(s)) return mem_[s];
        for (int i = 0; i < s.size(); i++)
        {
            string left = s.substr(0, i);
            string right = s.substr(i);
            if (dict.count(left) && wordBreak(right, dict))
                return true;
        }
        return false;


    }
private:
    unordered_map<string, bool> mem_;
};
int main()
{

    unordered_map<int, string> m;
    sleep(5);
}
