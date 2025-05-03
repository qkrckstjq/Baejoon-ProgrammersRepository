#include <iostream>
#include <vector>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;


int find_index(const vector<int>& list, int value) {
    int left = 0;
    int right = list.size();

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (list[mid] < value)      left = mid + 1;
        else right = mid;
    }
    return left;
}

int main() {
    int n, x;
    cin >> n;

    vector<int> list;
    for (int i = 0; i < n; i++) {
        cin >> x;

        int index = find_index(list, x);
        if (index == list.size()) {
            list.push_back(x);
        }
        else {
            list[index] = x;
        }
    }

    cout << (n - list.size());
}