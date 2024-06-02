#include<stdio.h>

int right_pattern() {
    int rows = 5;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}

int right_pattern_inverted() {
    int rows = 5;
    for (int i = rows; i > 0; i--)
    {
        for (int j = i; j > 0; j--)
        {
            printf("* ");
        }
        printf("\n");
    }
}

int mirrored_right_pattern() {
    int i, j, rows = 5;

    for (i = 0; i < rows; i++)
    {
        for (j = 2 * (rows - i); j >= 0; j--)
        {
            printf(" ");
        }

        for (j = 0; j <= i; j++)
        {
            printf("* ");
        }
        
        printf("\n");
    }
    
}
 
int main() {

    right_pattern();
    printf("\n");
    right_pattern_inverted();
    printf("\n");
    mirrored_right_pattern();
    
}