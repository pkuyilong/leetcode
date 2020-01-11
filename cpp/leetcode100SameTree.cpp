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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!q && !p)
            return true;
        if (!q || !p)
            return false;
        bool l = isSameTree(p->left,  q->left);
        bool r = isSameTree(p->right,  q->right);
        return l && r && p.val == q.val;
    }
}
