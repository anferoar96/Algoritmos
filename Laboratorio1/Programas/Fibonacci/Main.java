import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class Main {
    static  long fibonacci( long n) {
        if (n == 0){
            return 0;
        }
        long anterior = 0;
        long actual = 1;
        for (  long i = 1; i < n; ++i) {
            long siguiente = (long) (anterior + actual);
            anterior = actual;
            actual = siguiente;
        }
        return actual;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader leer = new BufferedReader(new InputStreamReader(System.in));
        String  a = leer.readLine();
        long numero = Long.parseLong(a);
        System.out.println(fibonacci(numero));

    }


}
