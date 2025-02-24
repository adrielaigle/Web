package recuperacao;

public class Lista {
    private No ref;

    public Lista() {
        this.ref = null;
    }

    public void insere(int info) {
        No novo = new No(info, ref);

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

        if (!duplicados) {
            if (info == this.ref.getInfo()) {
                if (this.ref.getProx() == this.ref) {
                    this.ref = null;
                    return;
                }
            }
            if (info == this.ref.getProx().getInfo()) {
                this.ref.setProx(this.ref.getProx().getProx());
            } else {
                for (No aux = this.ref.getProx(); aux != this.ref; aux = aux.getProx()) {
                    if (info == aux.getProx().getInfo()) {
                        if (aux.getProx() == this.ref) {
                            aux.setProx(this.ref.getProx());
                            this.ref = aux;
                            return;
                        }
                        aux.setProx(aux.getProx().getProx());
                        return;
                    }
                }
            }

        } else {
            while (this.ref != null && this.ref.getInfo() == info) {
                if (this.ref.getProx() == this.ref) {
                    this.ref = null;
                    return;
                } else {
                    No aux = this.ref;
                    while (aux.getProx() != this.ref) {
                        aux = aux.getProx();
                    }
                    aux.setProx(this.ref.getProx());
                    this.ref = aux;
                }
            }
            for (No aux = this.ref; aux.getProx() != this.ref;) {
                if (info == aux.getProx().getInfo()) {
                    aux.setProx(aux.getProx().getProx());
                } else {
                    aux = aux.getProx();
                }
            }
        }
    }
}