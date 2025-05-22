#include <iostream>
#include <deque>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	deque<int> list;
	deque<int> answer;
	for (int i = 1; i <= n; i++) {
		list.push_back(i);
	}

	while (!list.empty()) {
		for (int i = 0; i < k - 1; i++) {
			list.push_back(list.front());
			list.pop_front();
		}
		answer.push_back(list.front());
		list.pop_front();
	}

	cout << '<';
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i];
		if (i < answer.size() - 1) {
			cout << ", ";
		}
	}
	cout << '>';
}