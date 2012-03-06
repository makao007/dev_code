#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 10
#define MIN(X,Y) (X<Y? X:Y)

int edit_distance (const char * source, const char * target ) {
    unsigned int data[MAX_LENGTH][MAX_LENGTH] = {0};
    int i,j;
    int d1,d2,d3;
    int len1,len2;
    len1 = strlen(source);
    len2 = strlen(target);

    for (i=1;i<=len1;++i)
        data[i][0] = i;

    for (i=1;i<=len2;++i)
        data[0][i] = i;

    for(i=1;i<=len1;++i) {
        for(j=1;j<=len2;++j) {
            if (source[i] == target[j] )
                data[i][j] = data[i-1][j-1];
            else {
                d1 = data[i-1][j] ;
                d2 = data[i][j-1] ;
                d3 = data[i-1][j-1];
                data[i][j] = MIN(MIN(d1,d2),d3) + 1;
            } 
        }
    }

    for (i=0;i<=len1;i++) {
        for (j=0;j<=len2;j++)
            printf("%d ",data[i][j]);
        printf("\n");
    }
    return data[len1][len2];
}

int main(int argc, const char *argv[])
{
    char s1[10] = "google";
    char s2[10] = "oogle";
    printf("%s %s distance = %d\n", s1,s2,edit_distance(s1,s2)); 
    return 0;
}
