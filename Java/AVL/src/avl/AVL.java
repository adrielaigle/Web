package avl;

public class AVL {
    private No raiz;

    public AVL(int info) {
        raiz = new No(info);
    }

    public void insere(int info) {
        raiz = insere(raiz, info);
    }

    private No insere(No no, int info) {
        if (no == null) {
            return new No(info);
        }

        if (info < no.info) {
            no.esquerda = insere(no.esquerda, info);
        } else if (info > no.info) {
            no.direita = insere(no.direita, info);
        } else {
            return no;
        }

        no.altura = 1 + Math.max(altura(no.esquerda), altura(no.direita));
        int balanceamento = getBalanceamento(no);

        if (balanceamento > 1 && info < no.esquerda.info) {
            return rotacaoDireita(no);
        }
        if (balanceamento < -1 && info > no.direita.info) {
            return rotacaoEsquerda(no);
        }
        if (balanceamento > 1 && info > no.esquerda.info) {
            no.esquerda = rotacaoEsquerda(no.esquerda);
            return rotacaoDireita(no);
        }
        if (balanceamento < -1 && info < no.direita.info) {
            no.direita = rotacaoDireita(no.direita);
            return rotacaoEsquerda(no);
        }

        return no;
    }

    public void remove(int info) {
        raiz = remove(raiz, info);
    }

    private No remove(No no, int info) {
        if (no == null) {
            return null;
        }

        if (info < no.info) {
            no.esquerda = remove(no.esquerda, info);
        } else if (info > no.info) {
            no.direita = remove(no.direita, info);
        } else {
            if (no.esquerda == null || no.direita == null) {
                No temp = (no.esquerda != null) ? no.esquerda : no.direita;
                no = temp;
            } else {
                No temp = menorNo(no.direita);
                no.info = temp.info;
                no.direita = remove(no.direita, temp.info);
            }
        }

        if (no == null) {
            return null;
        }

        no.altura = 1 + Math.max(altura(no.esquerda), altura(no.direita));
        int balanceamento = getBalanceamento(no);

        if (balanceamento > 1 && getBalanceamento(no.esquerda) >= 0) {
            return rotacaoDireita(no);
        }
        if (balanceamento > 1 && getBalanceamento(no.esquerda) < 0) {
            no.esquerda = rotacaoEsquerda(no.esquerda);
            return rotacaoDireita(no);
        }
        if (balanceamento < -1 && getBalanceamento(no.direita) <= 0) {
            return rotacaoEsquerda(no);
        }
        if (balanceamento < -1 && getBalanceamento(no.direita) > 0) {
            no.direita = rotacaoDireita(no.direita);
            return rotacaoEsquerda(no);
        }

        return no;
    }

    private No menorNo(No no) {
        while (no.esquerda != null) {
            no = no.esquerda;
        }
        return no;
    }

    public String preOrdem() {
        StringBuilder sb = new StringBuilder();
        preOrdem(raiz, sb);
        return sb.toString();
    }

    private void preOrdem(No no, StringBuilder sb) {
        if (no != null) {
            sb.append(no.info).append("(").append(getBalanceamento(no)).append(")");
            preOrdem(no.esquerda, sb);
            preOrdem(no.direita, sb);
        }
    }

    private int altura(No no) {
        return (no == null) ? 0 : no.altura;
    }

    private int getBalanceamento(No no) {
        return (no == null) ? 0 : altura(no.esquerda) - altura(no.direita);
    }

    private No rotacaoDireita(No y) {
        No x = y.esquerda;
        No T2 = x.direita;

        x.direita = y;
        y.esquerda = T2;

        y.altura = Math.max(altura(y.esquerda), altura(y.direita)) + 1;
        x.altura = Math.max(altura(x.esquerda), altura(x.direita)) + 1;

        return x;
    }

    private No rotacaoEsquerda(No x) {
        No y = x.direita;
        No T2 = y.esquerda;

        y.esquerda = x;
        x.direita = T2;

        x.altura = Math.max(altura(x.esquerda), altura(x.direita)) + 1;
        y.altura = Math.max(altura(y.esquerda), altura(y.direita)) + 1;

        return y;
    }
}