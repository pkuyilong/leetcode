class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        helper(root, ans);
        return ans;
    }

    int helper(TreeNode *root, int &ans) {
        if (root == nullptr) {
            return -1;
        }
        int left = helper(root->left, ans);
        int right = helper(root->right, ans);
        ans = max(ans, left+right+2);
        return max(left, right) + 1;
    }
};
