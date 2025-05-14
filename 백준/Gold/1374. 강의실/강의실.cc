//#include <iostream>
//#include <utility>
//#include <vector>
//#include <algorithm>
//using namespace std;
//
//int main() {
//	int n;
//	cin >> n;
//
//	vector<pair<int, int>> list;
//	vector<int> queue;
//
//	for (int i = 0; i < n; i++) {
//		int num, start, end;
//		cin >> num >> start >> end;
//		list.push_back({ start, end });
//	}
//
//	sort(list.begin(), list.end(), [](pair<int, int> a, pair<int, int> b) {
//		if ((a.first < b.first) || (a.first == b.first && a.second < b.second)) {
//			return true;
//		}
//		return false;
//	});
//
//	queue.push_back(-list.front().second);
//	push_heap(queue.begin(), queue.end());
//	
//	int answer = 1;
//
//	for (int i = 1; i < list.size(); i++) {
//		auto [start, end] = list[i];
//		int last_end = -queue.front();
//
//		if (last_end <= start) {
//			pop_heap(queue.begin(), queue.end());
//			queue.pop_back();
//		}
//		else {
//			answer += 1;
//		}
//
//		queue.push_back(-end);
//		push_heap(queue.begin(), queue.end());
//	}
//
//	cout << answer;
//}

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<pair<int, int>> list;
	for (int i = 0; i < n; i++) {
		int num, start, end;
		cin >> num >> start >> end;
		list.push_back({ start, end });
	}

	sort(list.begin(), list.end(), [](pair<int, int> a, pair<int, int> b) {
		return a.first < b.first || (a.first == b.first && a.second < b.second);
		});

	priority_queue<int, vector<int>, greater<int>> pq; // min-heap
	pq.push(list[0].second);
	int answer = 1;

	for (int i = 1; i < list.size(); i++) {
		auto [start, end] = list[i];
		if (pq.top() <= start) {
			pq.pop(); // 기존 회의실 재사용
		}
		else {
			answer += 1; // 새로운 회의실 필요
		}
		pq.push(end);
	}

	cout << answer;
}
