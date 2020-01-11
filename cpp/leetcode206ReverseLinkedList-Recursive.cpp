class Solution {
public:
    /* Solution
    nullptr    <-1   2   3   4   5     nullptr
prev   cur

          next
                        prev    cur
nullptr    <-1   <- 2   <- 3   4   5     nullptr

    */
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        ListNode* ans = nullptr;
        ListNode* prev = nullptr;
        ListNode* cur = head;
        dfs(prev, cur, ans);
        return ans;
    }
    void dfs(ListNode* prev, ListNode* cur, ListNode* &ans) {
        if (cur == nullptr) {
            ans = prev
            return;
        }
        ListNode* next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
        // don't forget dfs
        dfs(prev, next, ans)
    }
};
