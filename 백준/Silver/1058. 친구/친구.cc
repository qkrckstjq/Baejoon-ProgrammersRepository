#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <utility>
//#include <cmath>
using namespace std;

int find_friends(int n, map<int, vector<int>>& graph) {
    set<int> visit;
    vector<pair<int, int>> stack;

    // 1) 자기 자신은 미리 방문 처리 (count할 때 제외하기 위해)
    visit.insert(n);
    stack.push_back({ n, 0 });

    // 2) DFS 스택 순회하되, depth가 2 이상이면 더 뻗지 않음
    while (!stack.empty()) {
        auto [curNode, depth] = stack.back();
        stack.pop_back();

        // depth == 2이면 친구(1)과 친구의 친구(2)까지만 허용하고 그 이후는 탐색 안 함
        if (depth == 2)
            continue;

        for (int nextNode : graph[curNode]) {
            if (!visit.count(nextNode)) {
                // 새로 만난 친구이니 방문 처리하고 스택에 넣어준다
                visit.insert(nextNode);
                stack.push_back({ nextNode, depth + 1 });
            }
        }
    }

    // 전체 방문한 사람 수에서 자기 자신 한 명을 빼면 친구·친구의 친구 수
    return static_cast<int>(visit.size()) - 1;
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