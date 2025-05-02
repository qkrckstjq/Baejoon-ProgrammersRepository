#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	vector<char> info(n + 1);
	map<int, map<int, int>> graph;
	vector<pair<int, int>> queue;
	make_heap(queue.begin(), queue.end());
	set<int> visit;

	char gender;
	for (int i = 1; i <= n; i++) {
		cin >> gender;
		info[i] = gender;
	}

	while (m--) {
		int src, dst, v;
		cin >> src >> dst >> v;
		if (graph[src].count(dst) && graph[src][dst] != 0) {
			int prev_v = graph[src][dst];
			graph[src][dst] = prev_v < v ? prev_v : v;
			graph[dst][src] = prev_v < v ? prev_v : v;
		}
		else {
			graph[src][dst] = v;
			graph[dst][src] = v;
		}
	}

	queue.push_back({ 0, 1 }); //first 거리, second 노드
	push_heap(queue.begin(), queue.end());

	int result = 0;
	int cnt = 0;
	while (!queue.empty()) {
		pop_heap(queue.begin(), queue.end());
		pair<int, int> cur_node = queue.back();
		queue.pop_back();
		int cur_dst = -cur_node.first;
		int cur_v = cur_node.second;

		if (visit.count(cur_v)) {
			continue;
		}
		visit.insert(cur_v);

		result += cur_dst;
		cnt += 1;
		char cur_gender = info[cur_v];
		for (auto &[next_v, next_dst] : graph[cur_v]) {
			char next_gender = info[next_v];
			if (!visit.count(next_v) && cur_gender != next_gender) {
				queue.push_back({ -next_dst, next_v });
				push_heap(queue.begin(), queue.end());
			}
		}
	}
	if (cnt == n) {
		cout << result;
	}
	else {
		cout << -1;
	}
	return 0;
}