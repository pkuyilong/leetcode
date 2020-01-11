#include <iostream>
#include <vector>
#include <unistd.h>
using namespace std;
vector<int> weight  = {1,1,2,2,};
vector<int> value = {1,2,4,5};

int main() {
    vector<vector<int>> ans(5, vector<int>(5, 0));
    for (int i = 1; i < 5; i++) {
        for (int j = 1; j < 5; j++) {
            if (j < weight[i-1]) ans[i][j] = ans[i-1][j];
            else
                ans[i][j] = max(ans[i-1][j], ans[i-1][j-weight[i-1]] + value[i-1]);
        }
    }
    for (auto &j : ans) {
        for (auto &i : j) {
            cout << i << '\t';
        }
        cout << endl;
    }
    sleep(50);
}
