#include <iostream>
#include <queue>
#include <vector>
#include <unistd.h>


using namespace std;

vector<vector<int>> mat = { {0, 0, 0, 0, 0},
                            {0, 1, 1, 0, 0},
                            {0, 0, 1, 0, 0},
                            {0, 1, 0, 1, 0},
                            {1, 1, 0, 0, 0}
                        };

vector<vector<int>> visited(5, vector<int>(5,0));
queue<pair<int, int>> q;

int main() {
    vector<int> x = {0, 1, -1, 0};
    vector<int> y = {1, 0, 0, -1};
    int count = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (mat[i][j] == 0) continue;
            // 是1但是还没又被访问过
            if (mat[i][j] == 1 && visited[i][j] == 0) {
                visited[i][j] = 1;
                q.push(make_pair(i,j));
                count += 1;
                while (!q.empty()) {
                    pair<int, int> tmp = q.front();
                    q.pop();
                    for (int k = 0; k < 4; k++) {
                        int next_x = tmp.first + x[k];
                        int next_y = tmp.second + y[k];
                        if (next_x >= 0 && next_x < 5 && next_y >= 0 && next_y < 5) {
                            if (mat[next_x][next_y] == 1 && visited[next_x][next_y] == 0) {
                                visited[next_x][next_y] = 1;
                                cout << next_x << " " << next_y << endl;
                                q.push(make_pair(next_x,next_y));
                            }
                        }
                    }
                }
            }
        }
    }
    cout << count << endl;
    sleep(10);
}
