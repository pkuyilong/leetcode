class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!q && !p)
            return true;
        if (!q || !p)
            return false;
        int l = isSameTree(p->left,  q->left);
        int r = isSameTree(p->right,  q->right);
        return l && r && p->val == q->val;
    }
};
