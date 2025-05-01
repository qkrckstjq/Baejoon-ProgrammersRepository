#include <stdio.h>
#include <algorithm>
#define _CRT_SECURE_NO_WARNINGS
using namespace std;

long long int combination(int n, int r) {
	long long int result = 1;
	for (int i = 1; i <= r; i++) {
		result *= (n - r + i);
		result /= i;
	}
	return result;
}

int main() {
	int t;
	scanf("%d", &t);
	while (t--) {
		int n, r;
		scanf("%d %d", &n, &r);
		int max_n = max(n, r);
		int min_r = min(n, r);
		printf("%d\n", combination(max_n, min_r));
	}
	return 0;
}