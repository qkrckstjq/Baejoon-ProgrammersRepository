//#include <iostream>
//#include <vector>
//#include <utility>
//#include <set>
//#include <array>
//using namespace std;
//
//int main() {
//	int n, m;
//	cin >> n >> m;
//
//	array<int, 4> dy = { 0, 0, 1, -1 };
//	array<int, 4> dx = { 1, -1, 0, 0 };
//
//	vector<vector<int>> board(n, vector<int>(m));
//
//	for (int i = 0; i < n; i++) {
//		string row;
//		cin >> row;
//		for (int j = 0; j < m; j++) {
//			board[i][j] = row[j];
//		}
//	}
//	vector<pair<pair<int, int>, int>> stack;
//	vector<vector<set<pair<int, int>>>> visit(n, vector<set<pair<int, int>>>(m));
//	int answer = 0;
//	bool find = false;
//
//	stack.push_back({ {0, 0}, 0 });
//
//	while (!stack.empty()) {
//		if (find) {
//			break;
//		}
//		auto [cur_node, cur_cnt] = stack.back();
//		stack.pop_back();
//		auto [cur_y, cur_x] = cur_node;
//
//		answer = max(answer, cur_cnt);
//		int move = board[cur_y][cur_x] - '0';
//		for (int i = 0; i < 4; i++) {
//			int next_y = (cur_y + dy[i] * move);
//			int next_x = (cur_x + dx[i] * move);
//			if (next_y < 0 || next_y >= n || next_x < 0 || next_x >= m || board[next_y][next_x] == 'H') continue;
//
//			if (!visit[next_y][next_x].count({ cur_y, cur_x })) {
//				visit[next_y][next_x].insert({cur_y, cur_x});
//				stack.push_back({{next_y, next_x}, cur_cnt + 1});
//			}
//			else {
//				find = true;
//				break;
//			}
//		}
//	}
//
//	if (find) {
//		cout << -1;
//	}
//	else {
//		cout << (answer + 1);
//	}
//}

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n, m;
vector<vector<char>> board;
vector<vector<int>> dp;
vector<vector<bool>> visited;
bool hasCycle = false;

int dy[4] = { 0, 0, 1, -1 };
int dx[4] = { 1, -1, 0, 0 };

int dfs(int y, int x) {
    if (hasCycle) return 0; // 이미 사이클 감지되었으면 중단
    if (y < 0 || y >= n || x < 0 || x >= m || board[y][x] == 'H') return 0;
    if (visited[y][x]) {
        hasCycle = true;
        return 0;
    }
    if (dp[y][x]) return dp[y][x];

    visited[y][x] = true;

    int move = board[y][x] - '0';
    int maxCount = 0;
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i] * move;
        int nx = x + dx[i] * move;
        maxCount = max(maxCount, dfs(ny, nx) + 1);
    }

    visited[y][x] = false;
    dp[y][x] = maxCount;
    return dp[y][x];
}

int main() {
    cin >> n >> m;
    board.resize(n, vector<char>(m));
    dp.assign(n, vector<int>(m, 0));
    visited.assign(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < m; j++) {
            board[i][j] = row[j];
        }
    }

    int result = dfs(0, 0);
    if (hasCycle) cout << -1;
    else cout << result;

    return 0;
}
