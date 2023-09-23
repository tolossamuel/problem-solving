#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, query;
    cin >> n >> query;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    vector<int> q(query);
    for (int i = 0; i < query; ++i) {
        cin >> q[i];
    }
    vector<int> result;
    for (int item : q) {
        for (int i = 0; i < n; ++i) {
            if (nums[i] == item) {
                result.push_back(i + 1);
                nums.insert(nums.begin() + i, item);
                break;
            }
        }
    }
    
    for (int item : result) {
        cout << item << " ";
    }
    
    return 0;
}
