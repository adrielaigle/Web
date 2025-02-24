package avl;

public class Main {

    public static void main(String[] args) {
        // Teste 1: Inserções simples que não requeiram balanceamento
        AVL avl1 = new AVL(10);
        avl1.insere(20);
        avl1.insere(5);
        System.out.println("Teste 1 - Inserções simples: " + avl1.preOrdem());
        
        // Teste 2: Remoção de nó sem filhos
        AVL avl2 = new AVL(10);
        avl2.insere(20);
        avl2.insere(5);
        avl2.remove(5);
        System.out.println("Teste 2 - Remoção de nó sem filhos: " + avl2.preOrdem());

        // Teste 3: Remoção de nó com 1 filho a direita
        AVL avl3 = new AVL(10);
        avl3.insere(20);
        avl3.insere(15);
        avl3.insere(21);
        avl3.remove(20);
        System.out.println("Teste 3 - Remoção de nó com 1 filho a direita: " + avl3.preOrdem());

        // Teste 4: Remoção de nó com 1 filho a esquerda
        AVL avl4 = new AVL(10);
        avl4.insere(5);
        avl4.insere(3);
        avl4.insere(2);
        avl4.remove(3);
        System.out.println("Teste 4 - Remoção de nó com 1 filho a esquerda: " + avl4.preOrdem());

        // Teste 5: Remoção de nó com 2 filhos, e que seja um filho a direita
        AVL avl5 = new AVL(10);
        avl5.insere(5);
        avl5.insere(20);
        avl5.insere(15);
        avl5.insere(25);
        avl5.remove(20);
        System.out.println("Teste 5 - Remoção de nó com 2 filhos (filho a direita): " + avl5.preOrdem());

        // Teste 6: Remoção de nó com 2 filhos, e que seja um filho a esquerda
        AVL avl6 = new AVL(10);
        avl6.insere(5);
        avl6.insere(20);
        avl6.insere(3);
        avl6.insere(7);
        avl6.remove(5);
        System.out.println("Teste 6 - Remoção de nó com 2 filhos (filho a esquerda): " + avl6.preOrdem());

        // Teste 7: Inserção que requer rotação simples a direita
        AVL avl7 = new AVL(30);
        avl7.insere(20);
        avl7.insere(10); // Requer rotação simples a direita
        System.out.println("Teste 7 - Inserção com rotação simples a direita: " + avl7.preOrdem());

        // Teste 8: Inserção que requer rotação simples a direita (outro caso)
        AVL avl8 = new AVL(30);
        avl8.insere(20);
        avl8.insere(25); // Requer rotação simples a direita
        System.out.println("Teste 8 - Inserção com rotação simples a direita: " + avl8.preOrdem());

        // Teste 9: Inserção que requer rotação simples a esquerda
        AVL avl9 = new AVL(10);
        avl9.insere(20);
        avl9.insere(30); // Requer rotação simples a esquerda
        System.out.println("Teste 9 - Inserção com rotação simples a esquerda: " + avl9.preOrdem());

        // Teste 10: Inserção que requer rotação simples a esquerda (outro caso)
        AVL avl10 = new AVL(10);
        avl10.insere(30);
        avl10.insere(20); // Requer rotação simples a esquerda
        System.out.println("Teste 10 - Inserção com rotação simples a esquerda: " + avl10.preOrdem());

        // Teste 11: Inserção que requer rotação dupla a direita (esquerda-direita)
        AVL avl11 = new AVL(30);
        avl11.insere(10);
        avl11.insere(20); // Requer rotaçãoo dupla a direita
        System.out.println("Teste 11 - Inserção com rotação dupla a direita: " + avl11.preOrdem());

        // Teste 12: Inserção que requer rotação dupla a esquerda (direita-esquerda)
        AVL avl12 = new AVL(10);
        avl12.insere(30);
        avl12.insere(20); // Requer rotação dupla a esquerda
        System.out.println("Teste 12 - Inserção com rotação dupla a esquerda: " + avl12.preOrdem());

        // Teste 13: Remoção que requer balanceamento (rotação simples a direita)
        AVL avl13 = new AVL(30);
        avl13.insere(20);
        avl13.insere(40);
        avl13.insere(10);
        avl13.remove(40); // Requer rotação simples a direita
        System.out.println("Teste 13 - Remoção com rotação simples a direita: " + avl13.preOrdem());

        // Teste 14: Remoção que requer balanceamento (rotação simples a esquerda)
        AVL avl14 = new AVL(10);
        avl14.insere(20);
        avl14.insere(5);
        avl14.insere(30);
        avl14.remove(5); // Requer rotação simples a esquerda
        System.out.println("Teste 14 - Remoção com rotação simples a esquerda: " + avl14.preOrdem());

        // Teste 15: Inserção que requer balanceamento seguido de remoção que também requer balanceamento
        AVL avl15 = new AVL(30);
        avl15.insere(20);
        avl15.insere(40);
        avl15.insere(10); 
        avl15.insere(8); // Requer balanceamento
        avl15.remove(40); // Requer balanceamento
        System.out.println("Teste 15 - Inserção e remoção com balanceamento: " + avl15.preOrdem());

        // Teste 16: Inserção que requer balanceamento seguido de remoção que também requer balanceamento
        AVL avl16 = new AVL(10);
        avl16.insere(20);
        avl16.insere(5);
        avl16.insere(30);
        avl16.insere(31); // Requer balanceamento
        avl16.remove(5); // Requer balanceamento
        System.out.println("Teste 16 - Inserção e remoção com balanceamento: " + avl16.preOrdem());

        // Teste 17: Esvaziar AVL e reinserir elementos
        AVL avl17 = new AVL(10);
        avl17.insere(20);
        avl17.insere(5);
        avl17.remove(10);
        avl17.remove(20);
        avl17.remove(5); // Árvore está vazia
        avl17.insere(15);
        avl17.insere(25);
        System.out.println("Teste 17 - Esvaziar e reinserir: " + avl17.preOrdem());

        // Teste 18: Esvaziar AVL e reinserir elementos
        AVL avl18 = new AVL(30);
        avl18.insere(20);
        avl18.insere(40);
        avl18.remove(30);
        avl18.remove(20);
        avl18.remove(40); // Árvore está vazia
        avl18.insere(10);
        avl18.insere(50);
        System.out.println("Teste 18 - Esvaziar e reinserir: " + avl18.preOrdem());

        // Teste 19: Em aberto (pode ser qualquer teste adicional)
        AVL avl19 = new AVL(10);
        avl19.insere(5);
        avl19.insere(15);
        avl19.insere(3);
        avl19.insere(7);
        System.out.println("Teste 19 - Teste em aberto: " + avl19.preOrdem());

        // Teste 20: Em aberto (pode ser qualquer teste adicional)
        AVL avl20 = new AVL(50);
        avl20.insere(30);
        avl20.insere(70);
        avl20.insere(75);
        avl20.insere(65);
        avl20.insere(20);
        avl20.insere(40);
        avl20.insere(10);
        System.out.println("Teste 20 - Teste em aberto: " + avl20.preOrdem());
    }

}