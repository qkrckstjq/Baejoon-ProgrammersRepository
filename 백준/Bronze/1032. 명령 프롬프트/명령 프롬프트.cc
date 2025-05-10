#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<string> strings(n);
	for (int i = 0; i < n; i++) {
		string str;
		cin >> str;
		strings[i] = str;
	}

	string result = strings[0];

	for (int i = 0; i < result.size(); i++) {
		for (int j = 1; j < n; j++) {
			if (result[i] != strings[j][i]) {
				result[i] = '?';
				break;
			}
		}
	}

	cout << result;
}