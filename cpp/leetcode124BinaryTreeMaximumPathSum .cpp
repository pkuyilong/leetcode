/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN;
        helper(root, ans);
        return ans;
    }
    int helper(TreeNode* root, int &ans) {
        if (!root)
            return 0;
        int left = max(0,helper(root->left, ans));
        int right = max(0, helper(root->right, ans));
        int tmp = left + right + root->val;
        ans = max(tmp, ans);
        return max(left, right) + root->val;
    }
};
