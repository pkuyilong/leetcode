/*
 * levelOrder.cpp  2018 mayilong 
 */
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>

using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* createTree(vector<int> treeNodes)
{
        return NULL;
}

class Solution {
public:
    vector<vector<int> > levelOrder(TreeNode* root) {
        queue<pair<TreeNode*, int> > q;
        vector<vector<int> > res;
        if (root == NULL)
            return res;
        q.push(make_pair(root, 0));
        while (!q.empty())
        {
            TreeNode * tmp = q.front().first;
            int level = q.front().second;
            cout << level << endl;
            if(level == res.size())
               res.push_back(vector<int>());
            res[level].push_back(tmp->val);
            if (tmp->left){
                q.push(make_pair(tmp->left, level + 1));
            }
            if (tmp->right){
                q.push(make_pair(tmp->right, level + 1));
            }
            q.pop();
        }
        return res;
    }
};

int main()
{
        vector<int> treeNodes({3, 9, 20, 0, 0, 15, 17});
        for (vector<int>::iterator it = treeNodes.begin(); it != treeNodes.end(); it++)
        {
                cout << *it << endl;
        }
        Solution sol =  Solution();
        TreeNode *root = new TreeNode(0);
        sol.levelOrder(root);
        cout << "Hello world" << endl;
}

