#include <stdio.h>
#include <string.h>

int is_same (char * p, int length) {
    int i;
    if (length==1 )
        return 1;

    for (i=0; i<length-1; i++)
        if ( p[i]!=p[i+1])
            break;

    if (i==length)
        return 1;
    else
        return 0;
}

int find_small_string (char *p, int length) {


    if (is_same(p,strlen(p)))
        return strlen(p);
}

int main(int argc, const char *argv[])
{
    char data[101];
    int  num,sum = 0,i;

    scanf("%d",&num);
    for (i=0; i<num; ++i) {
        memset(data,0,sizeof(data));
        scanf("%s",find_small_string(data,strlen(data)));
    }
    return 0;
}
