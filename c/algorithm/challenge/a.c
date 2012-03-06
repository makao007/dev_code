#include <stdio.h>
int main(int argc, const char *argv[])
{
    int *paths;
    int num = 10,i;

    paths = (int *) malloc(10 * size(int));
    
    for (i=0;i<num;i++)
        paths[i] = i;

    for (i=0;i<num;i++)
        printf("%d ",paths[i]);

    printf("\n");
    return 0;
}
