#include <stdio.h>
#define N 10

void print_array (int data[],int n) {
    int i;
    for (i=0;i<n;i++) 
        printf("%d ",data[i]);
    printf("\n");
    return ;
}

int main(int argc, const char *argv[])
{
    int i,p,q,t,id[N];
    for (i=0;i<N;++i) id[i] = i;
    printf(">>> ");
    while (scanf ("%d %d",&p,&q) == 2) {
        if (id[p] == id[q] ) 
            continue;
        for (t=id[p], i=0; i<N; ++i)
            if (id[i] == t)
                id[i] = id[q];
        printf("%d %d\n",p,q);
    }
    print_array (id,N);
    return 0;
}
