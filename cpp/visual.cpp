#include <iostream>
#include <vector>

using namespace std;


int main() {
    int nodeNum = 1;
    for (int i = 0; i < 4; i++) {
        // cout << "node Number " << nodeNum << endl;
        for (int j = 0; j < nodeNum; j++) {
            cout << "0";
        }
        nodeNum = 2*nodeNum;
        cout << endl;
    }
    cout << endl;
}
