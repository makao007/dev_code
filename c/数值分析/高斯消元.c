/*
 * ��˹��Ԫ���ⷽ����
 * date: 2010/12/20 17:16
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 10

void output(int n,float temp[MAX][MAX]){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<=n;j++)
            printf("%f ",temp[i][j]);
        printf("\n");
    }
    printf("\n");
    return;
}

int main(int argc, const char *argv[])
{
    int i,j,k,n;
    float data[MAX][MAX],temp,yy[MAX];
    scanf("%d",&n);

    // ��ȡ��������
    for(i=0;i<n;i++)
        for(j=0;j<=n;j++)
            scanf("%f",&data[i][j]);

    // ����������
    for(i=0;i<n-1;i++){
        if(data[i][i]==0){
            printf("�÷�����û��ʵ����\n");
            exit(0);
        }
        for(j=i+1;j<n;j++){
            temp = data[i][i]/data[j][i];
            for(k=i;k<=n;k++){
                data[j][k] = temp*data[j][k]-data[i][k];
            }
        //    output(n,data);
        }
    }

    //�������������
    k = 0;
    yy[k++] = data[n-1][n] / data[n-1][n-1];
    for(i=n-2;i>=0;i--){
        temp = data[i][n];
        for(j=n-1;j>i;j--){
            temp -= data[i][j]*yy[n-j-1];
        }
        yy[k++] = temp/data[i][j];
    }

    // �����
    for(i=n-1;i>=0;i--)
        printf("%f ",yy[i]);
    printf("\n");
    return 0;
}
