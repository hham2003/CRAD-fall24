#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main() {

    char buf2[100]; // buffer that will be overwritten when input buffer is overflown
    char buf[16];   // input buffer


    sleep(30);

    for (int i=0; i<100; i++) {
        gets(buf);  // read from standard input into inpt buffer
        printf("Overflow buffer holds: %s\n",buf2); // print the contents of overwritten memory
        sleep(6);
    }
    
    printf("\nDone.\n");
    
    return 0;
}