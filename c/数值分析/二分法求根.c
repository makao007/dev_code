/*
��ֵ������ҵ
ʵ���ġ��������Է������
�ö��ַ��󷽳̵�һ��ʵ��
date: 2010/12/1
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define MAX 100

float zhi(int,float[],float,float);
float ffabs(float );

int main(){
	int n,i,cha,flag = 0;
	float xishu[MAX],tail,a,b,x,e,y,left,right,mid;
	printf("���η��̣�");
	scanf("%d",&n);
	printf("�������ϵ���ͳ���(�������Ӵ�С): ");
	for(i=0;i<n;i++)
		scanf("%f",&xishu[i]);
	 scanf("%f",&tail);
	 printf("�������������Χ ");
	 scanf("%f",&e);
	 printf("���������ֵ�ķ�Χ ");
	 scanf("%f %f",&a,&b);
	 while(zhi(n,xishu,tail,a)*zhi(n,xishu,tail,b)>=0){
		  printf("��ѡ��������ֵ��Χ");
		  scanf("%f %f",&a,&b);
	 }
	 while(fabs(a-b)>e){
		  x = (a+b)/2;
		  mid = zhi(n,xishu,tail,x);
		  left = zhi(n,xishu,tail,a);
		  right = zhi(n,xishu,tail,b);
		  if (fabs(mid)<e){
			   y = x;
			   flag = 1;
			   break;
		  }
		  if (left*mid<0)
				b = x;
		  else if(mid*right<0)
				a = x;
	 }
	 if (flag == 0)
		y = (a+b)/2;
	 printf("ֵ��: %f\n",y);
	 return 0;
}


float zhi(int n,float data[], float tail,float x){
	 int i;
	 float y;
	 y = tail;
	 for(i=0;i<n;i++)
		y += pow(x,n-i)*data[i];
	 return y;
}
