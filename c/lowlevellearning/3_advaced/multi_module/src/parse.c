#include<stdio.h>
#include <unistd.h>

#include"common.h"
#include"parse.h"

int parse_file_header(int fd, int *numEmployees) {
    if (fd == -1) {
        printf("Bad file descriptor provided\n");
        return STATUS_ERROR;
    }

    struct dbheader_t header = {0};
    if (read(fd, &header, sizeof(header)) != sizeof(header)) {
        printf("Failed to read file header\n");
        return STATUS_ERROR;
    }

    *numEmployees = header.count;
    return STATUS_SUCCESS;
}
