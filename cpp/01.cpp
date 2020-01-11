#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;
// 注意物品的位置是从0下标开始的
vector<int> weight  = {1,1,2,2,};
vector<int> value = {1,2,4,5};


vector<vector<int>> ans(5, vector<int>(5,0));
int main() {
    // 物品
    for (int i = 1; i < 5; i ++) {
        // 空间
        for (int j = 1; j < 5; j++) {
            if (j < weight[i-1]) {
                ans[i][j] = ans[i-1][j];
                cout << i << '\t' << j << '\t' << ans[i][j] << endl;
            }
            else {
		                                             // 注意第i个物品的下标是i-1
                ans[i][j] = max(ans[i-1][j], ans[i-1][j-weight[i-1]] + value[i-1]);
                cout << i << '\t' << j << '\t' <<  ans[i][j] << endl;
            }
        }
    }
    for (auto &i : ans) {
        for (auto &j : i) {
            cout << j << '\t';
        }
        cout << endl;
    }
    sleep(10);
}
