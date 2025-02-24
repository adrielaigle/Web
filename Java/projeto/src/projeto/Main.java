package projeto;

public class Main {
    public static void main(String[] args) {
        Lista lista = new Lista();

        lista.insere(1);
        lista.insere(1);
        lista.insere(1);
        lista.insere(1);
        lista.insere(1);
        lista.insere(1);
        lista.insere(1);
        lista.insere(1);

        lista.remove(1,true);
        
        System.out.println(lista.imprime());
        
    }
}