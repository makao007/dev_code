/* 测试将单链表中的字符串逆序输出 
 * 本程序默认输入的字符串长度大于2
 * 2012-2-28
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char elem;

typedef struct node {
    elem data;
    struct node* next;
} *pnode;

//将字符数组转换为单链表模式
pnode create_string (elem * origine) {
    pnode head,p,prev;
    prev = NULL;
    while (*origine) {
        p = (pnode) malloc (sizeof(struct node));
        p->data = *origine;
        p->next = NULL;
        if (prev != NULL)
            prev->next = p;
        else
            head = p;
        origine++;
        prev = p;
    }
    return head;
}

//输出打印由链表组成的字符串
void print_string (pnode p) {
    printf("\n");
    while (p) {
        printf("%c",p->data);
        p = p->next;
    }
    return;
}

//用链表将字符串逆序输出
//方法： 用三个变量，分别记录p,p->next,p->next->next;
//第三个变量用于遍历链表， 第一，二个变量用于交换链接
pnode reverse_string1 (pnode p) {
    pnode pprev,pnext,pnnext;
    pprev  = p;
    pnext  = p->next;
    pnnext = p->next->next;
    pprev->next = NULL;           //设置链尾指向空，不然会进入无循环
    while (pnnext) {
        pnext->next = pprev;
        pprev = pnext;
        pnext = pnnext;
        pnnext = pnnext->next;
    }
    pnext->next = pprev;         //设置头节点指向下一个
    return pnext;
}


int main(int argc, const char *argv[])
{
    elem str[20] = "hello world";     //用于测试的字符串
    pnode pp = create_string(str);
    print_string (pp);
    print_string ( reverse_string1 (pp) );
    return 0;
}
