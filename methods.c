#include <stdio.h>

typedef struct foo {
    int (*method)(int, int);
}Foo;

int add (int a, int b)
{
    return a + b;
}

int main(int argc, char** argv)
{
    Foo bar;
    bar.method = &add;
    int result = bar.method(1, 2);
    
    printf("%d\n", result);
    return 0;
}
