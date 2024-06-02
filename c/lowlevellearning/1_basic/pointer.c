#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define MAX_EMPLOYEES 1000

struct employee_t
{
    int id;
    int income;
    bool staff;
};


int initialize_employee(struct employee_t *e) {
    static int numEmployees = 0;
    numEmployees++;

    e->id = numEmployees;
    e->income = 0;
    e->staff = true;

    return numEmployees;
}

int main()
{
    int n = 4;

    struct employee_t *employees = malloc(sizeof(struct employee_t) * n);
    if (employees == NULL) {
        printf("The allocator failed\n");
        return -1;
    }

    for (int i = 0; i < n; i++)
    {
        initialize_employee(&employees[i]);
        printf("%d\n", employees[i].id);
    }
    


    free(employees);
    employees = NULL;
}