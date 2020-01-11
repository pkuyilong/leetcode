#include <iostream>
#include <vector>

#include <algorithm>
#include <unistd.h>

using namespace std;

bool search(vector<int> nums, int key) {
    int i = 0;
    int j = nums.size() - 1;
    while (i <= j) {
        int mid = i + (j-i)/2;
        if (nums[mid] == key) {
            return true;
        }
        else if (nums[mid] > key) {
            j = mid - 1;
        }
        else {
            i = mid + 1;
        }
    }
    return false;
}
int main() {
    vector<int> nums = { 17, 5, 10, 2, 6, 7, 12};
    sort(nums.begin(), nums.end());
    bool res = search(nums, 16);
    cout << res << endl;

    sleep(5);
}
