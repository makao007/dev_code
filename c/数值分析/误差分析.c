/*
	数值分析,误差分析

  求方程的ax^2+bx+x = 0的根，其中a=1,b=-(5*10^8+1),c=5*10^8;
  方案一
	x1 = (-b+sqrt(b*b-4*a*c))/(2*a);
	x2 = (-b-sqrt(b*b-4*a*c))/(2*a);
  方案二
    x1 = -(b+sgn(b)*(sqrt(b*b-4*a*c))/(2*a);
	x2 = c/(a*x1);

  其中： sgn(x) : if(x>0) return 1; else if(x==0) return 0; else return -1;
  

*/

#include <stdio.h>
#include <math.h>

int sgn(int);

int main(int argc, const char *argv[])
{
    float a,b,c;
    float y11,y12,y21,y22,temp;
    a = 1;
    b = -500000001;
    c = 500000000;
    temp = sqrt(b*b-4*a*c);
    y11 = (-b+temp)/(2*a);
    y12 = (-b-temp)/(2*a);
    y21 = -(b+sgn(b)*temp)/(2*a);
    y22 = c/(a*y21);
    printf("方案一: y1=%.0f ; y2=%.0f\n",y11,y12);
    printf("方案二: y1=%.0f ; y2=%.0f\n",y21,y22);  
    return 0;
}

int sgn(int x){
    if (x>0)
        return 1;
    else if(x==0)
        return 0;
    else
        return -1;
}
