#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int file = open("data.txt", O_RDONLY);
    if (file < 0) {
        perror("Error opening the file");
        return EXIT_FAILURE;
    }

    char buffer[8];
    ssize_t bytes_read;

    while((bytes_read = read(file, buffer, 8-1)) > 0) {
        buffer[bytes_read] = '\0';
        printf("%s", buffer);
        sleep(5);
    }

    if (bytes_read < 0) {
        perror("Error reading from the file");
        close(file);
        return EXIT_FAILURE;
    }

    close(file);
    printf("\nDone.\n");

    return EXIT_SUCCESS;
}