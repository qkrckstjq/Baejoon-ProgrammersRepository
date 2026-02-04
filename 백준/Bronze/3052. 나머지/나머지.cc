#include <stdio.h>

int main() {
	int a[10] = { 0 };
	int num[10];
	for (int i = 0; i < 10; i++) {
		scanf("%d", &a[i]);
	}
	for (int i = 0; i < 10; i++) {
		a[i] = a[i] % 42;
		num[i] = 42;
	}

	for (int i = 0; i < 10; i++) {
		for (int j = i+1; j < 10; j++) {
			if (a[i] == a[j]) {
				num[i] = a[i];
			}
		}
	}

	int ten = 10;

	/*for (int i = 0; i < 10; i++) {
		printf("%d ", num[i]);
	}*/

	for (int i = 0; i < 10; i++) {
		if (num[i] != 42) {
			ten -= 1;
		}
	}

	printf("%d", ten);

}