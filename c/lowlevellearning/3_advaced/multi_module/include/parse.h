#ifndef PARSE_H
#define PARSE_H

struct dbheader_t {
    short version;
    short count;
};

int parse_file_header(int fd, int *numEmployees);

#endif
