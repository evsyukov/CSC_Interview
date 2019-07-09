#include <iostream>
using namespace std;


char *resize(const char *str, unsigned size, unsigned new_size)
{
	char * str_resize = new char [new_size];
    for (unsigned i = 0; i < size && i < new_size; i++) {
        str_resize[i] = str[i];
    }
    delete [] str;
    return str_resize;
}


char *getline()
{
    char c = '\0';
    unsigned curr_size = -1, new_size = 8;
    char * new_line = new char [new_size];
    while(cin.get(c) && c != '\n') {
        curr_size++;
        if ( curr_size == new_size) {
            new_size *= 2; 
            new_line = resize(new_line, curr_size, new_size);
        }
        new_line[curr_size] = c;
    }
    new_line[++curr_size] = '\0';
    return new_line;
}