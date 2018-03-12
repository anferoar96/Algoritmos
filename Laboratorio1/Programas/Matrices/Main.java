import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] multiplicacion(int k){
        int[][] matriz1 = new int[k][k];
        int[][] matriz2 = new int[k][k];
        for(int i =0;i<k;i++){
            for(int j=0;j<k;j++){
                matriz1[i][j] = 1;
                matriz2[i][j] = 2;
            }
        }
        int[][] resultado = new int[k][k];
        for (int x=0; x < k; x++) {
            for (int y=0; y < k; y++) {
                for (int z=0; z<k; z++) {
                   resultado [x][y] += matriz1[x][z]*matriz2[z][y];
                }
            }
        }
        return resultado;
    }

    static void imprimir(int[][] a,int k){
        for (int i=0;i<k;i++){
            for (int j=0;j<k;j++){
                System.out.print(a[i][j]+" ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader lectura = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Tamaño: ");
        int tama = Integer.parseInt(lectura.readLine());
        imprimir(multiplicacion(tama),tama);
    }
}
