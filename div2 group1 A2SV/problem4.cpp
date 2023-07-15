#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    string a;
    getline(cin, a);
    unordered_set<char> keys;
    int buy = 0;
    for (int i = 0; i < a.length(); i++) {
        if (islower(a[i])) {
            keys.insert(a[i]);
        } else {
            char key = tolower(a[i]);
            if (keys.count(key) > 0) {
                keys.erase(key);
            } else {
                buy++;
            }
        }
    }
    cout << buy << endl;
    return 0;
}
