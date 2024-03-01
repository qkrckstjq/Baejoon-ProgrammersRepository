#include <stdio.h>


double route(double a) {



	for (double i = 0; i <= 100; i+=1.0) {
		if (i * i == a) {
			return i;
		}
		else if (a < (i + 1.0) * (i + 1.0)) {

			for (double j = 0.1; j < 1; j += 0.1) {
				if (a < (i + (j + 0.1)) * (i + (j + 0.1))) {

					for (double k = 0.01; k < 0.1; k+=0.01) { //0.01
						if (a < (i + j + (k + 0.01)) * (i + j + (k + 0.01))) {

							for (double L = 0.001; L < 0.01; L+=0.001) {  // 0.001
								if (a < (i+j+k+(L + 0.001)) * (i+j+k+(L + 0.001)) ) {

									for (double m = 0.0001; m < 0.001; m += 0.0001) {  // 0.0001
										if (a < (i + j + k + L + (m + 0.0001)) * (i + j + k + L + (m + 0.0001))) {

											for (double n = 0.00001; n < 0.0001; n += 0.00001) {  // 0.00001
												if (a < (i + j + k + L + m + (n+0.00001)) * (i + j + k + L + m + (n + 0.00001))) {

													for (double o = 0.000001; o < 0.0001; o += 0.000001) {  // 0.000001
														if (a < (i + j + k + L + m + n + (o+0.000001)) * (i + j + k + L + m + n + (o + 0.000001))) {
															return i + j + k + L + m + n + o+ 0.000001;
														}
													}
												}
											}
										}
									}

								}
							}

						}
					}
				}
			}
		}
	}
}


int main(void) {
	int T = 0; //테스트케이스

	double X1 = 0;
	double Y1 = 0;
	double R1 = 0;
	double X2 = 0;
	double Y2 = 0;
	double R2 = 0;
	double distance = 0;

	double bigcircle = 0;
	double smallcircle = 0;

	scanf("%d", &T);


	for (int i = 0; i < T; i++) {
		scanf("%lf %lf %lf %lf %lf %lf", &X1, &Y1, &R1, &X2, &Y2, &R2);
		distance = route(((X1-X2)*(X1-X2)) + ((Y1-Y2)*(Y1-Y2)));


		if (R1 >= R2) {
			bigcircle = R1;
			smallcircle = R2;
		}
		else {
			bigcircle = R2;
			smallcircle = R1;
		}

		if (distance == 0) { //두점사이의거리가0 즉 똑같은곳에있을때
			if (R1 == R2) {
				printf("%d\n", -1);
			}
			else {
				printf("%d\n", 0);
			}

		} else if (distance <= bigcircle) { //두점사이의거리보다 큰원이 더 크면 내접
			if (bigcircle - distance > smallcircle) {
				printf("%d\n", 0);
			}
			else if (bigcircle - distance < smallcircle) {
				printf("%d\n", 2);
			}
			else if (bigcircle - distance == smallcircle) {
				printf("%d\n", 1);
			}

		} else if(distance > bigcircle) {  // 두점사이의 거리보다 큰원반경이 작으면 내접하지 않음
			if (distance == R1 + R2) {
				printf("%d\n", 1);
			}
			else if (distance > R1 + R2) {
				printf("%d\n", 0);
			}
			else if (distance < R1 + R2) {
				printf("%d\n", 2);
			}
		}



	}



} 