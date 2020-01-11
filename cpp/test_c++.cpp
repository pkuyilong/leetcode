#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;


int main()
{
    vector<int> nums = { 1,2,3,4,5};
    //cout << *(find(nums.begin(), nums.end(), 6)) << endl;
    cout << (find(nums.begin(), nums.end(), 6))  != nums.end() << endl;
    sleep(4);


}
