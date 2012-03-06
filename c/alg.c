#include <math.h>
#include <stdio.h>
#include <string.h>
#define MAX_MOUNT 100

/*
#define DEBUG
*/

int load_data (char filename[],int data[] ) {
    int length;
    int row,col;
    int i ;
    FILE * fp;
    fp = fopen(filename,"r");
    if (fp == NULL)
        return 0;
    fscanf(fp, "%d\n", &length);
    printf("%d\n",length);
    for (row=0,i=0 ;row<length;row++) {
        for (col=0; col<length; col++) {
            fscanf(fp,"%d",&data[i]);
            i++;
        }
    }
    return length*length;
}

void print_data (int data[], int length) {
    int i;
    for (i=0;i <length; i++) 
        printf("%d ",data[i]);
    printf("\n");
    return;
}

int is_exists (int data [],int length, int target) {
    int row,col,temp;
    temp = sqrt(length);
    row = 0;
    col = temp - 1;
    while (1) {
#ifdef DEBUG
        printf("row:%d  col:%d\n",row,col);
#endif

        if (row < 0 || col < 0 || row >= temp || col>= temp)
            break;
        if (data[row*temp+col] == target) 
            return 1;
        else if (data[row*temp+col] > target)
            col --;
        else
            row ++;
    }
    return 0;
}
    

int main(int argc, const char *argv[])
{
    char filename[100];
    int  num,data[MAX_MOUNT],target,length;
    strcpy(filename,"data.txt");
    length = load_data(filename, data);
    print_data(data,length);
    printf("input target >>> ");
    scanf("%d",&target);
    if (is_exists(data,length,target)) 
        printf("exists\n");
    else
        printf("no exists\n");
    return 0;
}
