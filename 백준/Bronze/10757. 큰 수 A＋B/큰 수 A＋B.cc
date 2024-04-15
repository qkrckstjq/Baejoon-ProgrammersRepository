#include <stdio.h>


int main() {
	char a[10002],b[10002];
	scanf("%s %s",a,b);
	int alen = 0, blen = 0, bigger = 0;
	while(a[alen]) alen++;
	while(b[blen]) blen++;
	if(alen >= blen) {
		bigger = alen+1;
	} else {
		bigger = blen+1;
	}
	int arr[bigger];
	for(int i = 0; i < bigger; i++) {
		arr[i]=-1;
	}
	int extra=0;
	for(int i = (bigger-1); i>=0; i--) {
		arr[i] = ((a[alen-1] - 48) + (b[blen-1] - 48) + extra) % 10;
		
		
		extra = ((a[alen-1] - 48) + (b[blen-1] - 48)+ extra) / 10;
		if((alen-1) == 0) {
			a[alen-1] = 48;
		} else {
			alen--;
		}
		if((blen-1) == 0) {
			b[blen-1] = 48;
		} else {
			blen--;
		}		
	}
	int c = 0;
	int d = 0;
	for(int i = 0; i<bigger; i++) {
		if(arr[i] != 0) {
			d = i;
			break;
		}
	}	
	

	for(int i = d; i<bigger; i++) {
		printf("%d",arr[i]);
	}
	

}