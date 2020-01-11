#include <iostream>
#include <unistd.h>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
using namespace std;
class Solution {
public:
    void deleteNode(ListNode* &node) {
        while (node->next != nullptr) {
            node->val = node->next->val;
            node = node->next;
            if (node->next == nullptr) {
                node = nullptr;
                return;
            }
        }
    }
};

// accepted solution is as follows.
// class Solution {
// public:
//     void deleteNode(ListNode* node) {
//         if (node == nullptr) {
//             return;
//         }
//         node->val = node->next->val;
//         node->next = node->next->next;
//     }
// };

int main(){
    ListNode* head = new ListNode(4);
    head->next = new ListNode(5);
    ListNode *one = new ListNode(1);
    head->next->next = one;
    head->next->next->next = new ListNode(3);
    head->next->next->next->next = nullptr;

    Solution s = Solution();
    s.deleteNode(one);
    while (head) {
        cout << head->val << endl;
        head = head->next;
    }
    sleep(5);

}
