#include <stdio.h>


int main() {
    // 흑돌이 1
    // 백돌이 2
    //무승부시 0 이긴 돌의 가로,세로좌표출력
    
    
    int arr[20][20];
    for(int i = 0; i < 19; i++){
        for(int j = 0; j<19; j++){
            scanf("%d",&arr[i][j]);
        }
    }
    int stand = 0;
    int count = 0;
    int boolean = 1; //1이면 오목성공 0이면 오목아님
    
    
    for(int i = 0; i < 19; i++){
        for(int j = 0; j<19; j++){
            if(arr[i][j] == 1 || arr[i][j] == 2){
                boolean = 1;
                stand = arr[i][j];
                
                for(int k = 1; k <= 5; k++){
                    if(arr[i][j+k] == stand  && k != 5){
                        boolean *= 1;
                    } else if (arr[i][j+k] != stand  && k != 5) {
                        boolean *= 0;
                    } else if ( k==5 && arr[i][j+k] == stand) {
                        //arr[0][-1]가 1임
                        boolean *= 0;
                    } else if(j != 0 && arr[i][j-1] == stand) {
                        boolean *= 0; 
                    } 
                    
                    if(boolean == 0) break;
                }
                
                if(boolean == 1){
                    printf("%d\n",stand);
                    printf("%d %d",i+1, j+1);
                    count++;
                    break;
                }
                
                boolean = 1;
                for(int k = 1; k <= 5; k++){
                    if(arr[i+k][j] == stand  && k != 5){
                        boolean *= 1;
                    } else if (arr[i+k][j] != stand  && k != 5) {
                        boolean *= 0;
                    } else if (k==5 && arr[i+k][j] == stand) {
                        boolean *= 0;
                    } else if (i != 0 && arr[i-1][j] == stand){
                        boolean *= 0;
                    }
                    if(boolean == 0) break;
                }
                
                if(boolean == 1){
                    printf("%d\n",stand);
                    printf("%d %d",i+1, j+1);
                    count++;
                    break;
                }
                
                boolean = 1;
                for(int k = 1; k <= 5; k++){
                    if(arr[i+k][j+k] == stand && k != 5){
                        boolean *= 1;
                    } else if (arr[i+k][j+k] != stand  && k != 5) {
                        boolean *= 0;
                    } else if (k==5 && arr[i+k][j+k] == stand) {
                        boolean *= 0;
                    } else if (i!=0 && j!=0 && arr[i-1][j-1] == stand) {
                        boolean *=0;
                    }
                    if(boolean == 0) break;
                }
                if(boolean == 1){
                    printf("%d\n",stand);
                    printf("%d %d",i+1, j+1);
                    count++;
                    break;
                }
                
                boolean = 1;
                for(int k = 1; k <= 5; k++){
                    if(arr[i-k][j+k] == stand && k != 5){
                        boolean *= 1;
                    } else if (arr[i-k][j+k] != stand  && k != 5) {
                        boolean *= 0;
                    } else if (k==5 && arr[i-k][j+k] == stand) {
                        boolean *= 0;
                    } else if (i!=0&&j!=0 && arr[i+1][j-1] ==stand){
                        boolean *=0;
                    }
                    if(boolean == 0) break;
                }
                
                if(boolean == 1){
                    printf("%d\n",stand);
                    printf("%d %d",i+1, j+1);
                    count++;
                    break;
                }
                
                
                
            }
            if(count != 0) {
                break;
            }
            
        }
        if(count != 0) {
                break;
            }
    }
    
    if(count == 0){
        printf("%d",0);
    }
    
    
}