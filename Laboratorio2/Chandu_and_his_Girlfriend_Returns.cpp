    #include <stdio.h>

    using namespace std;

    void llenado(int ar[],int tam){
            for(int i=0;i<tam;i++){
                int elemento;
                scanf("%d",&elemento);
                ar[i] = elemento;
            }
        }

    int main() {
        	int casos;
        	scanf("%d",&casos);
        	for(int i=0;i<casos;i++){
        	    int arr,arr2;
        	    scanf("%d",&arr);
        	    scanf("%d",&arr2);
        	    int ar[arr];
        	    llenado(ar,arr);
        	    int cont=0;
        	    for(int j=0;j<arr2;j++){
                    int num;
                    scanf("%d ",&num);
                    if(num>ar[cont]){
                        printf("%d ",num);
                    }else{
                        while(num<ar[cont] && (cont<arr)){
                            printf("%d ",ar[cont]);
                            cont++;
                        }
                        printf("%d ",num);
                    }
                }
                while(cont<arr){
                    printf("%d ",ar[cont]);
                    cont++;
                }
                printf("\n");

            }

        }
