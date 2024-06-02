#include<stdio.h>
#include<stdbool.h>

#define MAX_IDS 32
#define MAX_EMPLOYEES 1000

__attribute__((__packed__)) struct employee_t_modified {
    int id;
    char firstnam[64];
    char lastname[64];
    float income;
    bool ismanager;
};

struct employee_t {
    int id;
    char firstnam[64];
    char lastname[64];
    float income;
    bool ismanager;
};


int main(){

    printf("Size of employees: %ld\n", sizeof(struct employee_t_modified));

    printf("Size of employees: %ld\n", sizeof(struct employee_t));
}