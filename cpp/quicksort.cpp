#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;

class Solution {
public:
    void quicksort(vector<int> &nums, int start, int end) {
        if (start >= end) {
            return;
        }
        int mid = partition(nums, start, end);
        quicksort(nums, start, mid-1);
        quicksort(nums, mid+1, end);
    }

    int partition(vector<int> &nums, int start, int end) {
        int key = nums[start];
        int i = start;
        int j = end;
        while (i < j) {
            while ( i < j && nums[j] > key) {
                j--;
            }
            if (i < j) {
                swap(nums[i], nums[j]);
            }
            while (i < j && nums[i] < key) {
                i++;
            }
            if (i < j) {
                swap(nums[i], nums[j]);
            }
        }
        return i;
    }
};

int main() {
    vector<int> nums = {5, 17, 12, 6, 7, 2, 10};
    Solution s = Solution();
    s.quicksort(nums, 0, nums.size()-1);
    for (auto item : nums) {
        cout << item << endl;
    }
    sleep(5);
}
