#include <iostream>

using namespace std;


int main()
{
    int tam;
    cout<<"Tamaño: ";
    cin>>tam;

    int matriz1[tam][tam];
    int matriz2 [tam][tam];
    int resultado[tam][tam];

        for(int i =0;i<tam;i++){
            for(int j=0;j<tam;j++){
                matriz1[i][j] = 1;
                matriz2[i][j] = 2;
            }
        }


     for(int i=0; i<tam; ++i){
         for(int j=0; j<tam; ++j){
            resultado[i][j] = 0;
         }

     }

        for (int x=0; x < tam; x++) {
            for (int y=0; y < tam; y++) {
                for (int z=0; z<tam; z++) {
                   resultado [x][y] += matriz1[x][z]*matriz2[z][y];
                }
            }
        }

  for (int n=0;n<tam;n++){
            for (int w=0;w<tam;w++){
                cout<<resultado[n][w]<<" ";
            }
            cout<<endl;
        }

    return 0;
}
