FROM gcc:latest

WORKDIR /prog

COPY . /prog

RUN gcc -o read-data read-data.c

CMD ["./read-data"]

