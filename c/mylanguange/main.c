#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int getFileSize(FILE *fp) 
{
    // config file to read from init to end
    fseek(fp, 0, SEEK_END);

    // return the length
    return ftell(fp);
}

enum tokenType {
    VAR = 1,
    LPARAM,
    RPARAM,
    IDENTIFIER,
    EQUAL,
};

struct tokenStruct
{
    char * type;
    char * value;
};

void scanner(char * input, int len, struct tokenStruct *tokenlist) {
    printf("-> %s\n", input);

    int count = 0;

    while (count < len)
    {
        printf("%c\n",  input[count]);
        count++;
    }
    
}

int main(int argc, char **argv)
{

    if (argc <= 1)
    {
        printf("No file atached\n");
        return -1;
    }
    
    FILE *fp;

    fp = fopen(argv[1], "r");
    
    printf("after open \n");

    // If the file exist
    if (fp == NULL)
    {
        perror("Error opening file");
        return -1;
    }

    printf("fp %d \n", fp);
    const int len = getFileSize(fp);

    if (len == 0)
    {
        perror("Error on read len");
        return -1;
    }

    printf("after len %d\n", len);
    char inputStr[len];

    fseek(fp, 0, SEEK_SET);

    if (fgets(inputStr, len, fp) == NULL)
    {
        perror("Error on read fgets");
        return -1;
    }

    // Close the file
    fclose(fp);
    printf("value get form file: '''%s''' \n", inputStr);
    
    struct tokenStruct tokenlist[] = malloc(sizeof(struct tokenStruct) * len);

    scanner(inputStr, len, tokenlist);

    return 0;
}