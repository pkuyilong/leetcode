
#include <iostream>
#include <queue>


struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        std::vector<std::vector<int> > res;
        std::vector<int> intermediate;
      if (root == nullptr)
        return res;
      queue<TreeNode*> cur;
      queue<TreeNode*> next;
      cur.push(root);
      while (!cur.empty())
      {
        int size = cur.size();
        intermediate.clear();
        for (auto i = 0; i < size; i++)
        {
          TreeNode* tmp = cur.front();
          cout << tmp->val << endl;
          intermediate.push_back(tmp->val)
          cur.pop();
          if (tmp->left)
          {
            next.push(tmp->left);
          }
          if (tmp->right)
          {
            next.push(tmp->right);
          }
        }
        swap(next, cur);
        res.insert(res.begin(), intermediate);
      }
    }
    return res;
};

if __name__ == "__main__":
  Solution s();
