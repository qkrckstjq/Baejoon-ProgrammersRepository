#include <stdio.h>
#include <vector>
#include <stack>
#include <deque>
#include <set>
#include <string>
#include <algorithm>
#define _CRT_SECURE_NO_WARNINGS 
using namespace std;

void dfs(int start, vector<vector<int>> graph) {
	stack<int> arr;
	set<int> visit;

	arr.push(start);
	string result = "";
	while (!arr.empty()) {
		int cur_v = arr.top();
		arr.pop();

		if (visit.count(cur_v)) {
			continue;
		}

		result += to_string(cur_v) + " ";
		visit.insert(cur_v);


		for (int i = graph[cur_v].size() - 1; i >= 0; i--) {
			int next_v = graph[cur_v][i];
			if (!visit.count(next_v)) {
				arr.push(next_v);
			}
		}
	}
	printf("%s\n", result.c_str());
}

void bfs(int start, vector<vector<int>> graph) {
	deque<int> arr;
	set<int> visit;

	arr.push_back(start);
	string result = "";
	while (!arr.empty()) {
		int cur_v = arr[0];
		arr.pop_front();

		if (visit.count(cur_v)) {
			continue;
		}

		result += to_string(cur_v) + " ";
		visit.insert(cur_v);

		for (int next_v : graph[cur_v]) {
			if (!visit.count(next_v)) {
				arr.push_back(next_v);
			}
		}
	}
	printf("%s\n", result.c_str());
}


int main() {
	int N, M, V;
	scanf("%d %d %d", &N, &M, &V);
	vector<vector<int>> graph(N + 1);
	
	for (int i = 0; i < M; i++) {
		int src, dst;
		scanf("%d %d", &src, &dst);
		graph[src].push_back(dst);
		graph[dst].push_back(src);
	}

	for (vector<int>& node : graph) {
		sort(node.begin(), node.end());
	}

	dfs(V, graph);
	bfs(V, graph);
}