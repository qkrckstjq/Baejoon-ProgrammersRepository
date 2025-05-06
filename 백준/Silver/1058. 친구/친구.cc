#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <utility>
//#include <cmath>
using namespace std;

int find_friends(int n, map<int, vector<int>>& graph) {
	int result = -1;
	set<int> visit;
	vector<pair<int, int>> stack;

	visit.insert(n);
	stack.push_back({ n, 0 });

	while (!stack.empty()) {
		auto [curNode, depth] = stack.back();
		stack.pop_back();
		
		result += 1;
		if (depth == 2) continue;

		for (int nextNode : graph[curNode]) {
			if (!visit.count(nextNode)) {
				visit.insert(nextNode);
				stack.push_back({ nextNode, depth + 1 });
			}
		}
	}

	return result;
}

int main() {
	int n;
	cin >> n;

	map<int, vector<int>> graph;

	for (int i = 0; i < n; i++) {
		string row;
		cin >> row;
		for (int j = 0; j < row.size(); j++) {
			if (row[j] == 'Y') {
				graph[i].push_back(j);
			}
		}
	}

	int result = 0;

	for (int i = 0; i < n; i++) {
		result = max(result, find_friends(i, graph));
	}

	cout << result;

	return 0;
}