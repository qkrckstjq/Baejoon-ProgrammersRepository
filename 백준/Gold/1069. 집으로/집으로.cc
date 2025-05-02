#include <stdio.h>
#include <cmath>
#define _CRT_SECURE_NO_WARNINGS

double distance(double y, double x) {
	return sqrt(pow(y, 2) + pow(x, 2));
}

int main() {
	double x, y, d, t;
	scanf("%lf %lf %lf %lf", &x, &y, &d, &t);

	double dis = distance(y, x);
	double case1, case2, case3;
	case1 = dis;
	case2 = dis >= d ? floor(dis / d) * t + fmod(dis, d) : t + d - dis;
	case3 = dis >= d ? (floor(dis / d) + 1) * t : t * 2;
	
	printf("%.9lf", fmin(case1, fmin(case2, case3)));
	return 0;
}