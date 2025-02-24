package avl;

public class No {
    int info;
    No esquerda;
    No direita;
    int altura;

    No(int info) {
        this.info = info;
        this.altura = 1;
    }
}