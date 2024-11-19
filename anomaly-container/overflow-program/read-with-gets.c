#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main() {
    sleep(15);

    char* buf = (char*)malloc(16*sizeof(char));
    char buf2[100];

    clock_t start = clock();

    for (int i=0; i<100; i++) {
        gets(buf);
        printf("string is: %s\n", buf);
        printf("%lu\n", clock()-start);
        sleep(20);
    }
    

    printf("Done.\n");

    free(buf);

    return 0;
}