#include <iostream>
#include <vector>
#include <stack>
#include <utility>
#include <queue>
using namespace std;

int mat[5][6] = {
        {0,0,0,0,0,1},
        {0,1,1,1,0,1},
        {0,1,0,0,0,1},
        {0,0,0,1,1,0},
        {0,0,0,0,0,1},
        };

int visited[5][6] = {
        {-1,-1,-1,-1,-1,-1},
        {-1,-1,-1,-1,-1,-1},
        {-1,-1,-1,-1,-1,-1},
        {-1,-1,-1,-1,-1,-1},
        {-1,-1,-1,-1,-1,-1}
};
stack<pair<int, int> > stk;
queue<pair<int, int> > q;

void print_visited()
{
    cout << "------- start -------" << endl;
    for (int ii = 0; ii < 5; ii++) {
        for (int jj = 0; jj < 6; jj++) {
            cout << visited[ii][jj] << ", ";
        }
        cout << endl;
    }
    cout << "------- end -------" << endl;
}
int fun()
{
    int block = 0;
    for (int ii = 0; ii < 5; ii++)
    {
        for (int jj = 0; jj < 6; jj++)
        {
            // cout << mat[ii][jj] << endl;
            if (visited[ii][jj] == 2)
                continue;
            if (mat[ii][jj] == 0)
            {
                visited[ii][jj] = 2;
                continue;
            }

            else if (mat[ii][jj] == 1)
            {
                cout << ii << jj << endl;
                visited[ii][jj] = 2;
                q.push(make_pair(ii, jj));
                block += 1;
            }

            while (!q.empty()) {
                print_visited();
                int size = q.size();
                for (int m = 0; m < size; m++) {
                    pair<int, int> pos = q.front();
                    int i = pos.first;
                    int j = pos.second;
                    if (i > 0 and mat[i-1][j] == 1)
                        if (visited[i-1][j] == -1)
                            q.push(make_pair(i-1, j));
                            visited[i-1][j] = 2;

                    if (j < 5 and mat[i][j+1] == 1)
                        if (visited[i][j+1] == -1)
                            q.push(make_pair(i, j+1));
                            visited[i][j+1] = 2;

                    if (i < 5 and mat[i+1][j] == 1)
                        if (visited[i+1][j] == -1)
                            q.push(make_pair(i+1, j));
                            visited[i+1][j] = 2;

                    if (j > 0 and mat[i][j-1] == 1)
                        if (visited[i][j-1] == -1)
                            q.push(make_pair(i, j-1));
                            visited[i][j-1] = 2;
                    q.pop();
                }
            }
        }
    }
    cout << block << endl;
    return block;

}
int main() {
    fun();
    return 0;
}
