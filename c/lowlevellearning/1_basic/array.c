#include<stdio.h>

#define MAX_IDS 32

int main() {
    int ids[MAX_IDS] = {0,1,2,3};
    ids[MAX_IDS - 2] = 0x41;
    for(int i = 0; i < MAX_IDS; i++) {
        printf("%d\n", ids[i]);
    }

    char mystr[] = {'h', 'e', 'l', 'l', 'o', 0};
    char *myotherstr = "hello, world";

    printf("%s\n", mystr);
    printf("%s\n", myotherstr);

    // strcpy(dest, src);
    // strncpy(dest, src, n_bytes_long);
    // 
}