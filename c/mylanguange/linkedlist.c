#include <stdio.h>
#include <stdlib.h>

#include "linkedlist.h"

void printLinkedList(struct node *p)
{
    while (p != NULL)
    {
        printf("%s, %s\n", p->value[0], p->value[1]);
        p = p->next;
    }
}

struct node * initLinkedList(char *value[])
{
    struct node *newNode =  malloc(sizeof(struct node));

    newNode->value[0] = value[0];
    newNode->value[1] = value[1];
    newNode->next = NULL;
    newNode->previous = NULL;
    newNode->tail = NULL;

    return newNode;
};

void push(struct node *p, char *value[])
{
    struct node *newNode =  initLinkedList(value);

    newNode->previous = p->tail;
    
    if (p->tail == NULL) {
        p->next = newNode;
        p->tail = newNode;
    } else {
        p->tail->next = newNode;
        p->tail = p->tail->next;
    }
}

struct node * popx(struct node *p)
{
    struct node *temp = p->tail;

    p->tail = temp->previous;
    temp->previous->next = NULL;
    temp->previous = NULL;

    return temp;
}

int main(int argc, char const *argv[])
{
    char * x[] = {"var", "identifier"};
    struct node * lk = initLinkedList(x);
    printf("------------\n");
    char * a[] = {"myname", "identifier"};
    push(lk, a);
    char * b[] = {"=", "equal"};
    push(lk, b);

    char * c[] = {"marcio ramos", "string"};
    push(lk, c);
    printLinkedList(lk);

    printf("------------\n");
    struct node * poped = popx(lk);
    printf("%s, %s\n", poped->value[0], poped->value[1]);
    
    struct node * poped1 = popx(lk);
    printf("%s, %s\n", poped1->value[0], poped1->value[1]);

    printf("------------\n");
    printLinkedList(lk);

    return 0;
}
