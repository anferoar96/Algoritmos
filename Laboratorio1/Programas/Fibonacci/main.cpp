#include <iostream>

using namespace std;

 unsigned short  int fibonacci(unsigned  short int n) {
    if (n == 0){
        return 0;
    }
     unsigned short  int anterior = 0;
    unsigned short  int actual = 1;
    for (unsigned short  int i = 1; i < n; ++i) {
        unsigned short  int siguiente = anterior + actual;
        anterior = actual;
        actual = siguiente;
    }
    return actual;
}


int main()
{
    unsigned  short int numero;
    cin>> numero;
    cout<<fibonacci(numero);
    return 0;
}
