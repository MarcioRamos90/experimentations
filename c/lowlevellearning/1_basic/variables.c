#include<stdio.h>

#define MAX_PERSONS 1024

#define DEBUG

int main() {
    #ifdef DEBUG
    printf("We are in debug mode: %s:%d\n", __FILE__, __LINE__);
    #endif

    return 0;
}