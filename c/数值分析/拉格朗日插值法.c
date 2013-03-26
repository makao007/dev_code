/*
  数值分析作业
Lagrange 插值
date:2010/12/20 15:18


 */
#include <stdio.h>
#include <math.h>
#define MAX 10
float lagrange(float [],float[],int,float); 
int main(int argc, const char *argv[])
{
    float x[MAX],y[MAX],result,xx;
    int i,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%f %f",&x[i],&y[i]);
    scanf("%f",&xx);
    result = lagrange(x,y,n,xx);
    printf("x=%f, y=%f\n",xx,result);
    return 0;
}

float lagrange(float lx[MAX],float ly[MAX],int n,float x){
    int i,j;
    float temp,tem;
    temp = 0;
    for(i=0;i<n;i++){
        tem = 1;
        for(j=0;j<n;j++){
            if (j==i)
                continue;
            tem *= (x-lx[j])/(lx[i]-lx[j]);
        }
        temp += tem * ly[i];
    }
    return temp;
}

