#include <iostream>
#include <vector>

using namespace std;

class Heap {
public:
    Heap() {
        store = vector<int>(capacity, 0);
        store[0] = -1;
    }
    void buildHeap(vector<int> nums) {
        for (auto item : nums) {
            insert(item);
        }
    }

    void insert(int num) {
        if (curSize + 1 < capacity) {
            curSize += 1;
            // cout << "curSize : " << curSize << endl;
            store[curSize] = num;
            heapUpAdjust();
        }
    }

    bool empty() {
        return curSize > 0 ? false : true;
    }

    int getMax() {
        if (!empty())
            return store[1];
        else
            return store[0];
    }

    void heapDownAdjust(int idx) {
        if (idx == 0) {
            return;
        }
        int leftIdx = idx*2;
        int rightIdx = idx*2 + 1;
        while (leftIdx <= curSize) {
            if (rightIdx <= curSize) {
                int pos = store[rightIdx] > store[leftIdx] ? rightIdx : leftIdx;
                if (store[pos] > store[idx]) {
                    swap(store[idx], store[pos]);
                    idx = pos;
                }
                else break;
            }
            //if (rightIdx <= curSize) {
            //    if (store[leftIdx] > store[rightIdx]) {
            //        if (store[leftIdx] > store[idx]) {
            //            swap(store[leftIdx], store[idx]);
            //            idx = leftIdx;
            //        }
            //        else break;
            //    }
            //    else {
            //        if (store[rightIdx] > store[idx]) {
            //            swap(store[rightIdx], store[idx]);
            //            idx = rightIdx;
            //        }
            //        else break;
            //    }
            //}
            else {
                if (store[leftIdx] > store[idx]) {
                    swap(store[leftIdx], store[idx]);
                    idx = leftIdx;
                }
                else break;
            }
            leftIdx = idx*2;
            rightIdx = idx*2 + 1;
        }
    }

    int extractMax() {
        int ans = getMax();
        swap(store[1], store[curSize]);
        curSize--;
        heapDownAdjust(1);
        return ans;
    }

    void heapUpAdjust() {
        int idx = getSize();
        // cout << "cur : " << idx << endl;
        int parIdx =  idx / 2;
        while (parIdx > 0) {
            if (store[parIdx] < store[idx]) {
                swap(store[parIdx], store[idx]);
            }
            idx = parIdx;
            parIdx /= 2;
        }
    }

    int getSize() {
        return curSize;
    }
    void print() {
        for (auto item : store) { cout << item << endl;}
    }

    void buildMaxHeap(vector<int> nums) {
        if (nums.size() <= 1) {return;}
        for (int i = 0; i < nums.size(); i++) {
            store[i+1] = nums[i];
            curSize += 1;
        }
        if (curSize / 2 > 0) {
            for (int i = curSize / 2; i > 0; i--) {
                heapDownAdjust(i);
            }
        }
    }

private:
    int curSize = 0;
    int capacity = 100;
    vector<int> store;
};

int main() {
    vector<int> nums = {33,99, -3, 17,42, 90,48,52, 67, 23,-6,5,2,18,1};
    //vector<int> nums = {1,2,3};
    Heap heap = Heap();
    // heap.buildHeap(nums);
    heap.buildMaxHeap(nums);
    heap.print();
    for (int i = 0; i < nums.size(); i++) {
        int res = heap.extractMax();
        cout << "max num : " << res << endl;
        //heap.print();
    }
    // heap.print();
    return 0;
}
