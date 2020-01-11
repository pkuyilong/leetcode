class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr)
            return true;
        return helper(root->left, root->right);
    }

    bool helper(TreeNode* p, TreeNode* q)
    {
        if (!p && !q)
            return true;
        if (!p || !q)
            return false;
        if (p->val != q->val)
            return false;
        int l = helper(p->left, q->right);
        int r = helper(p->right, q->left);
        return p->val == q->val && l and r;
    }
};
