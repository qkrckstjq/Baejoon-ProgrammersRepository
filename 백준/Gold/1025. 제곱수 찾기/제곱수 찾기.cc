#include <iostream>
#include <vector>
#include <cmath>

bool isMultiple(int num) {
    int sqrt = round(std::sqrt(num));
    if ((sqrt * sqrt) == num) {
        return true;
    }
    return false;
}

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::string> board(n);
    for (int i = 0; i < n; i++) {
        std::string row;
        std::cin >> row;
        board[i] = row;
    }

    if (n == 1 && m == 1) {
        if (isMultiple(board[0][0] - '0')) {
            std::cout << board[0][0];
        }
        else {
            std::cout << -1;
        }
        return 0;
    }

    int ans = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int dr = -(n - 1); dr <= n - 1; dr++) {
                for (int dc = -(m - 1); dc <= m - 1; dc++) {
                    if (dr == 0 && dc == 0) continue;
                    int num = 0;
                    int x = i, y = j;
                    while (x >= 0 && x < n && y >= 0 && y < m) {
                        num = num * 10 + (board[x][y] - '0');
                        if (isMultiple(num) && num > ans) {
                            ans = num;
                        }
                        x += dr;
                        y += dc;
                    }

                }
            }
        }
    }
    std::cout << ans;
    return 0;
}