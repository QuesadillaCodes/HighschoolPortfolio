
// Online IDE - Code Editor, Compiler, Interpreter

#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int sub(int a, int b)
{
    return a - b;
}

int main()
{
    int (*func1)(int, int);
    func1 = &add;
    
    int (*func2)(int, int);
    func2 = &sub;
    
    printf("%p | %p\n", func1, func2);
    printf("%d %d\n", func1(5, 5), func2(4, 2));
    
    /* Swap functions */
    int (*temp)(int, int);
    temp = func2;
    func2 = func1;
    func1 = temp;
    printf("%d %d\n", func1(5, 5), func2(4, 2));
    
    return 0;
}
