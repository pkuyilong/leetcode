/*
 * levelOrder2.cpp  2018 mayilong 
 */
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>

using namespace std;

struct TreeNode
{
        int val;
        TreeNode * left;
        TreeNode * right;
        TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

void printVector(vector<int> nums)
{
        for (auto item : nums)
        {
                cout << item << endl;
        }
}

TreeNode * createTree(vector<int> nums)
{
        vector<TreeNode*> nodes(1 + nums.size(), new TreeNode(-1));
        // push useless node

        if (nums.size() == 0)
                return NULL;
        int idx = 1;
        for (unsigned long  i = 0; i < nodes.size(); i++)
        {
                if (nums[i] != -1)
                {
                        nodes[idx] = new TreeNode(nums[i]);
                }
                else
                {
                        nodes[idx] = NULL;
                }
                idx++;

                if (i / 2 > 0 && i % 2 == 0 ) 
                {
                        nodes[i/2]->left = nodes[i];
                }
                else
                        nodes[i/2]->right = nodes[i];
        }
        return nodes[1];
}

void preOrder(TreeNode * root)
{
        if (root == NULL)
                return;

        cout << root->val << endl;
        preOrder(root->left);
        preOrder(root->right);
}
int main()
{

        vector<int> nums = {1, 2, 3, 4, -1, -1, 4, 5};
        TreeNode *root = createTree(nums);
        // preOrder(root);

        cout << "Hello world" << endl;
}

