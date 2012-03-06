#include <stdio.h>
int main(int argc, const char *argv[])
{
    int *p1,*p2,*p3,data[10]={0},i;
    int arr[2][3];

    p1 = (int*)arr;
    p2 = p1+1;
    printf("%d %d\n",p1,p2);
    //printf("%d %d\n",sizeof(data),sizeof(p1));

    return 0;
}
