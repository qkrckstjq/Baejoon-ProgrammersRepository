#include <stdio.h>
#include <stack>
#include <vector>
#include <utility>
using namespace std;

int dy[] = { 1, -1, 0, 0 };
int dx[] = { 0, 0, 1, -1 };

void dfs(int y, int x, int m, int n, vector<vector<int>> &board) {
	stack<pair<int, int>> arr;
	arr.push({ y, x });

	while (!arr.empty()) {
		pair<int, int> coord = arr.top();
		arr.pop();
		int y = coord.first;
		int x = coord.second;

		for (int i = 0; i < 4; i++) {
			int next_y = y + dy[i];
			int next_x = x + dx[i];

			if (0 <= next_y && next_y < n && 0 <= next_x && next_x < m) {
				if (board[next_y][next_x] != 0) {
					arr.push({ next_y, next_x });
					board[next_y][next_x] = 0;
				}
			}
		}
		
	}
}

int main() {
	int t;
	scanf("%d", &t);

	while (t--) {
		int m, n, k;
		scanf("%d %d %d", &m, &n, &k);
		vector<vector<int>> board(n, vector<int>(m, 0));
		while (k--) {
			int x, y;
			scanf("%d %d", &x, &y);
			board[y][x] = 1;
		}
		int result = 0;
		for (int y = 0; y < n; y++) {
			for (int x = 0; x < m; x++) {
				if (board[y][x] == 1) {
					/*printf("y : %d, x : %d\n", y, x);*/
					dfs(y, x, m, n, board);
					result += 1;
				}
			}
		}
		printf("%d\n", result);
	}
	return 0;
}