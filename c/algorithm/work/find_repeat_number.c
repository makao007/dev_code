#include <math.h>
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

#define LIMIT_MEM  100
#define MAX_NUMBER 40000

typedef unsigned char uchar;
typedef unsigned int  uint;

int create_sample (int start, int end ) {
    int i;
    FILE * pf;
    char filename[50] = "sample.dat";
    pf = fopen(filename,"w");
    if (pf == NULL) {
        fprintf(stderr,"open file error");
        return 0;
    }
    for (i=start; i<end; i++)
        fprintf(pf,"%d ",i);

    fclose(pf);
    return 1;
}



int read_data (FILE* pf,int * data,int num) {
    int i;
    for(i=0; i<num; ++i) {
        fscanf(pf,"%d ",data++);
        if (feof(pf))
            return i;
    }
    return i;
}
        

int find_repeat_number () {
    FILE *pf;
    int data[LIMIT_MEM];
    int 
    char filename[50] = "sample.dat";
    pf = fopen(filename,"r");
    if (pf == NULL) {
        fprintf(stderr,"read file error\n");
        return -1;
    }
    memset (data,0,sizeof(data));
    
}




int main(int argc, const char *argv[])
{
    if (create_sample(1,1000))
        printf("write sample succeful\n");
    return 0;
}
