#include <stdio.h>


int selfmult(int a) {
	if (a == 0) {
		return 1;
	}
	else {
		return 2 * selfmult(a - 1);
	}

}

int strg = 0;
int endrg = 0;
int start = 0;
int end = 0;

int firstend(int a) {
	return selfmult(a) * selfmult(a);
}



int findlocation(int N, int r, int c) {
	

	if ((r >= 0 && r < selfmult(N) / 2) && (c >= 0 && c < selfmult(N) / 2)) {

		//0<= 범위 <selfnum(N)*selfnum(N)/4
		strg = start;
		end -= selfmult(N) * selfmult(N) / 4 * 3;
		endrg = end;
		if (strg == endrg) {
			return strg;
		}
		else {
			return findlocation(N - 1, r, c);
		}
		
	}
	else if ((r >= selfmult(N) / 2 && r < selfmult(N)) && (c >= selfmult(N) / 2 && c < selfmult(N))) {

		//selfnum(N)*selfnum(N)/4*3 <= 범위 < selfnum(N)*selfnum(N)
		start += selfmult(N) * selfmult(N) / 4 * 3;
		strg = start;
		endrg = end;
		if (strg == endrg) {
			return strg;
		}
		else {
			return findlocation(N - 1, r - selfmult(N - 1), c - selfmult(N - 1));
		}
	}
	else if ((r >= 0 && r < selfmult(N) / 2) && (c >= selfmult(N) / 2 && c < selfmult(N))) {

		//selfnum(N)*selfnum(N)/4 <= 범위 < selfnum(N)*selfnum(N)/2
		start += selfmult(N) * selfmult(N) / 4;
		end -= selfmult(N) * selfmult(N) / 2;
		strg = start;
		endrg = end;
		if (strg == endrg) {
			return strg;
		}
		else {
			return findlocation(N - 1, r, c - selfmult(N - 1));
		}
	}
	else {

		//selfnum(N)*selfnum(N)/2 <= 범위 < selfnum(N)*selfnum(N)/4*3
		start += selfmult(N) * selfmult(N) / 2;
		end -= selfmult(N) * selfmult(N) / 4;
		strg = start;
		endrg = end;
		if (strg == endrg) {
			return strg;
		}
		else {
			return findlocation(N - 1, r - selfmult(N - 1), c);
		}
	}

}


int main() {
	int N = 0;
	int r = 0, c = 0; //row 가로행, colum 세로열
	scanf("%d %d %d", &N, &r, &c);
	

	end = firstend(N)-1;

	printf("%d", findlocation(N, r, c));

	

}