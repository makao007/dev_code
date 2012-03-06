#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char *argv[])
{
    FILE *pf ;
    pf = fopen("sample.dat","r");
    int i;
    if (pf == NULL) {
        fprintf(stderr,"open file error");
        return -1;
    }

    fscanf(pf,"%d",&i);
    fscanf(pf,"%d",&i);
    printf("sizeof(%d) = %d\n",i,sizeof(i));
    fseek(pf,0,2);
    printf("%d\n",ftell(pf));
    fclose(pf);
    return 0;
}
