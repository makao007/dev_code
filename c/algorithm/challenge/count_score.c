#include <stdio.h>

int total = 0;

int recure_cal (int num,int max,int target,int data){
    int i;
    if (num <= 0) {
        if (data == target)
            total ++;
        return 0;
    }
    //printf("%d %d %d %d\n",num,max,target,data);
    for (i=0;i<=max;i++) {
        recure_cal (num-1,max,target,data+i);
    }
}

int find_count_score (int data[],int line) {
    int i,unknow=0,sum = 0;
    total = 0;
    for (i=0; i<line; ++i) {
        if (data[i] == -1)
            unknow++;
        else
            sum += data[i];
    }
    recure_cal (unknow,line-1,(line*(line-1))/2-sum,0);
    return total;
}

int main(int argc, const char *argv[])
{
    int cases,line,data[40] = {0};
    int i,j,temp,result,sum,flag ;
    scanf("%d",&cases);

    for (i=0; i<cases; ++i) {
        scanf("%d",&line);
        temp = 0;
        flag = 0;
        for(j=0; j<line; ++j) { 
            scanf("%d",&data[j]);
            if (data[j] == -1)
                flag = 1;
            else
                temp += data[j];
        }
        result = line*(line-1) - temp*2;
        if (result < 0)          //大于line*(line-1)/2 出错
            printf("0\n");           
        else if ( result == 0)    //正好等于line*(line-1)/2,只能一种可能
            printf("1\n");
        else if ( flag == 0 )     //出错，
            printf("0\n");
        else 
            printf("%d\n",find_count_score(data,line));
    }

    return 0;
}
