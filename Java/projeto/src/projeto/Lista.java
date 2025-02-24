package projeto;

public class Lista {
    private No ref;

    public Lista() {
        this.ref = null;
    }

    public void insere(int info) {
        No novo = new No(info);

        if (ref == null) {
            ref = novo;
            ref.setProx(ref);
        } else {
            No atual = ref.getProx(); 
            No anterior = ref;

            while (atual != ref && atual.getInfo() < info) {
                anterior = atual;
                atual = atual.getProx();
            }

            if (atual == ref && ref.getInfo() < info) {
                novo.setProx(ref.getProx());
                ref.setProx(novo);
                ref = novo;
            } else {
                novo.setProx(atual);
                anterior.setProx(novo);
            }
        }
    }

    public String imprime() {
        if (ref == null) {
            return "lista vazia";
        }

        String resultado = "";
        No atual = ref.getProx();

        do {
            resultado += atual.getInfo() + " ";
            atual = atual.getProx();
        } while (atual != ref.getProx());


        return resultado.trim();
    }

    public void remove(int info, boolean duplicados) {
        if (ref == null) return; 

        No atual = ref.getProx();
        No anterior = ref;
        boolean encontrado = false;

        do {
            if (atual.getInfo() == info) {
                encontrado = true;

                if (atual == ref) { 
                    if (atual == ref.getProx()) { 
                        ref = null;
                    } else {
                        anterior.setProx(atual.getProx());
                        ref = anterior;
                    }
                } else {
                    anterior.setProx(atual.getProx());
                }

                if (!duplicados) break;
                atual = anterior.getProx();
            } else {
                anterior = atual;
                atual = atual.getProx();
            }
        } while (atual != ref.getProx() && (!encontrado || duplicados));
    }
}