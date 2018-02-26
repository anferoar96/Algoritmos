#include <stdio.h>
#include <stdlib.h>

int fibonacci( int n) {
    if (n == 0){
        return 0;
    }
     int anterior = 0;
     int actual = 1;
     int i = 1;
    for ( i = 1; i < n; ++i) {
          int siguiente = anterior + actual;
        anterior = actual;
        actual = siguiente;
    }
    return actual;
}

int main()
{
    int c,res;
    scanf("%d",&c);
    res = fibonacci(c);
    printf("%d",res);
    return 0;
}
