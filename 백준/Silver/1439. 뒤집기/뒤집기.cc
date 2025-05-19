#include <iostream>
using namespace std;

int main() {
	string num;
	cin >> num;
	int one = 0;
	int zero = 0;
	char prev = num[0];

	if (prev == '0') {
		zero += 1;
	}
	else {
		one += 1;
	}

	for (int i = 1; i < num.size(); i++) {
		if (prev == num[i]) {
			continue;
		}
		else {
			if (num[i] == '0') {
				zero += 1;
			}
			else if (num[i] == '1') {
				one += 1;
			}
			prev = num[i];
		}
	}
	cout << min(one, zero);
}