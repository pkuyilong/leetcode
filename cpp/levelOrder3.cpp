#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <unordered_map>
#include <map>
#include <unistd.h>
#include <vector>
using namespace std;
int main()
{
  unordered_map<string, unordered_set<char>> m;
  // string s("hello");
  vector<string> string_vector;
  string_vector.push_back("hello");
  string_vector.push_back("world");

  for (auto &s : string_vector)
  {
    cout << s << endl;
    for (int i = 0; i < s.size(); i++)
    {
      char c = s[i];
      s[i] = '*';
      m[s].insert(c);
      s[i] = c;
    }
  }

  for (auto &item : m)
  {
    cout << item.first << endl;
    for (auto &ch : item.second)
    {
      cout << ch << endl;
    }
    // cout << item.size() << endl;
  }
  cout << m.size() << endl;
  sleep(60);

}
