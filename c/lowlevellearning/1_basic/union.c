#include<stdio.h>
#include<stdbool.h>

#define MAX_IDS 32
#define MAX_EMPLOYEES 1000

struct employee_t {
    int id;
    char firstnam[64];
    char lastname[64];
    float income;
    bool ismanager;
};

union myunion_u
{
    int x;
    char c;
    short s;
};


int main(){
    struct employee_t employees[MAX_EMPLOYEES];
    
    union myunion_u u;
    u.x = 0x41424345;

    printf("%hx %hhx", u.s, u.c);
}