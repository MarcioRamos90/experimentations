
struct node
{
    char *value[2];
    struct node *next;
    struct node *previous;
    struct node *tail;
};

void printLinkedList(struct node *p);
struct node * initLinkedList(char *value[]);
void push(struct node *p, char *value[]);
struct node * pop(struct node *p, char *value[]);