#include <stdio.h>

double add(double a, double b)
{
    return a + b;
}

double sub(double a, double b)
{
    return a - b;
}

double mult(double a, double b)
{
    return a * b;
}

double divide(double a, double b)
{
    return a / b;
}

int main(int argc, char** argv)
{
    void* foo[] = {&add, &sub, &mult, &divide};
    double (*func_ptr)(double, double);
    
    for (int i = 0; i <= 4; i++)
    {   
        func_ptr = foo[i];
        printf("%lf\n", func_ptr(50, 10));
    }
    return 0;
}
