#include <stdio.h>
#include <string.h>
#define min(x,y) ( (x>y)? (y):(x) );

int main(int argc, const char *argv[])
{
    int x=2,y=3,z;
    char *p1,p2[20];
    strcpy(p2,"helloworld");
    p1 = (char*) malloc(10);
    strcpy(p1,"abcefg");
    printf("%s \n",p1);
    printf("%s \n",p2);
    //
    free(p2);
    p2 = (char*) malloc (100);
    strcpy(p2,"hello world");
    printf("p2 = %s\n",p2);
    return 0;
}
