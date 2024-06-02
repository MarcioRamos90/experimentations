#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct worker_t {
    int id;
    char * name;
    int age;
    float salary;
};

void new_worker(struct worker_t *w, char *n, int ag, float slr) {
    static int theNumber = 0;
    theNumber++; 

    w->id = theNumber;
    w->name = n;
    w->age = ag;
    w->salary = slr;
}

int main() {
    int n = 4;
    struct worker_t *workers = malloc(sizeof(struct worker_t) * n);
    
    new_worker(&workers[0], "Marcio Ramos", 33, 9995.00);
    new_worker(&workers[1], "Caroline Rosa", 30, 10.0);
    new_worker(&workers[2], "Fabio Ramos", 27, 8000.0);
    new_worker(&workers[3], "Pitico", 6, -100.0);

    for (int i = 0; i < n; i++)
    {
        printf("My name in %s my id is %d, my income is %f and I have %d years old\n", workers[i].name, workers[i].id, workers[i].salary, workers[i].age);
    }
    
    free(workers);
    workers = NULL;

    return 0;
}