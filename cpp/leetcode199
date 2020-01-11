/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//class Solution {
//public:
//    vector<int> rightSideView(TreeNode* root) {
//        vector<int> ans;
//        if (root == nullptr) {
//            return ans;
//        }
//        unordered_map<int, int> mp;
//        preOrder(root, 0, mp);
//        for(auto item : mp) {
//            cout << item.first << " " << item.second << endl;
//        }
//        return ans;
//    }
//
//    void preOrder(TreeNode* root, int idx, unordered_map<int,int> &mp) {
//        if (root == nullptr) {
//            return;
//        }
//        mp[idx] = root->val;
//        preOrder(root->left, idx+1, mp);
//        preOrder(root->right, idx+1, mp);
//    }
//};

// version 2
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if (root == nullptr) {
            return ans;
        }
        preOrder(root, 0, ans);
        return ans;

    }
    void preOrder(TreeNode* root, int idx, vector<int> &ans) {
        if (root == nullptr) {
            return;
        }
        if (ans.size() <= idx)
            ans.push_back(root->val);
        else
            ans[idx] = root->val;
        preOrder(root->left, idx+1, ans);
        preOrder(root->right, idx+1, ans);
    }
};
