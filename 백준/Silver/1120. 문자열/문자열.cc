#include <iostream>
using namespace std;

int main() {
	string a, b;
	cin >> a >> b;

	int answer = 987654321;
	int temp;
	for (int i = 0; i < b.size() - a.size() + 1; i++) {
		temp = 0;
		for (int j = 0; j < a.size(); j++) {
			if (a[j] != b[j + i]) {
				temp += 1;
			}
		}
		answer = min(answer, temp);
	}
	cout << answer;
}