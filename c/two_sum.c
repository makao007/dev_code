/*
输入一个已经按升序排序过的数组和一个数字，
在数组中查找两个数，使得它们的和正好是输入的那个数字。
要求时间复杂度是O(n)。如果有多对数字的和等于输入的数字，输出任意一对即可。
 * 
 */


#include <stdio.h>

typedef int elemType;

int is_exist(elemType data[], int length, elemType target, int *left, int *right) {
    elemType temp;
    (*left) = 0;
    (*right) = length - 1;
    while ((*left) < (*right)) {
        temp = data[*left] + data[*right];
        if (temp == target)
            return 1;
        else if ( temp < target )
            (*left) ++;
        else
            (*right) --;
    }
    return 0;
}


int main(int argc, const char *argv[])
{
    
    elemType data[100] = {1,2,4,7,11,15};
    elemType target = 57;
    int head,tail,length ;

    if (is_exist (data,6,target,&head,&tail) )
        printf ("left:%d   right:%d\n", head,tail);
    else
        printf ("No\n");

    return 0;
}
