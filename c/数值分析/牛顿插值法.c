/*
 * 数值分析
 * 牛顿插值法
date: 2010/12/20 15:49
 */
#include <stdio.h>
#include <math.h>
#define MAX 10

float cal(int left,int right,float xx[MAX],float yy[MAX]){
    if(left+1==right)
        return (yy[right]-yy[left])/(xx[right]-xx[left]);
    else
        return (cal(left+1,right,xx,yy)-cal(left,right-1,xx,yy))/(xx[right]-xx[left]);
}

float newton_insert(float xx[MAX],float yy[MAX],int n,float x){
    float result,temp;
    int i,j;
    result = yy[0];
    for(i=1;i<n;i++){
        temp = cal(0,i,xx,yy);
        for(j=0;j<i;j++)
            temp *= x-xx[j];
        result += temp;
    }
    return result;
}


int main(int argc, const char *argv[])
{
    float xx[MAX],yy[MAX];
    float x,y;
    int i,n;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%f %f",&xx[i],&yy[i]);
    scanf("%f",&x);
    y = newton_insert(xx,yy,n,x);
    printf("x=%f ; y=%f\n",x,y);
    return 0;
}
