/* 
数值分析课程设计
实验四　　非线性方程求根
２。牛顿迭代法

*/

#include <stdio.h>
#include <math.h>
int main(int argc,char * argv[]){
	float x,xx,y0,y1,temp;
	float xe,ye,pre_x;
	int i,n;
	i = 0;
	scanf("%f %f %f %d",&x,&xe,&ye,&n);
	pre_x = x;
	y1 = 3*x*x+2*x-3;
	while(i<n && y0 != 0){
		y0 = x*x*x+x*x-3*x-3;
		y1 = 3*x*x+2*x-3;
		xx = x - y0/y1;
		if( fabs(xx-x)< xe || fabs(y1)<ye )
			break;
		x = xx;
	}
	printf("f(%f) = %f\n",pre_x,x);
	return 0;
}
