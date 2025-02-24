window.addEventListener("load", main)

let carrinho = []

const carrinho_lc = localStorage.getItem("carrinho")
if (carrinho_lc == null) {
    localStorage.setItem("carrinho", "[]")
} else {
    carrinho = JSON.parse(carrinho_lc);
}

let refrigerantes = [
]

async function main() {
    const catalogo = document.getElementsByClassName("menu-container")[0]
    const resposta = await fetch("http://localhost:55555/api/cardapio")
    todos_os_produtos = await resposta.json()
    for (let x = 0; x < todos_os_produtos.length; x++) {
        if (todos_os_produtos[x].tipo === "refrigerantes") {
            refrigerantes.push(todos_os_produtos[x])
        }
    }

    for (let x = 0; x < refrigerantes.length; x++) {

        const refrigerante = document.createElement("div");
        const img = document.createElement("img");
        const titulo = document.createElement("h3");
        const descricao = document.createElement("p");
        const valor = document.createElement("p");
        const button = document.createElement("button");

        refrigerante.id = refrigerantes[x].id;

        img.src = refrigerantes[x].img;
        titulo.textContent = refrigerantes[x].titulo;
        descricao.textContent = refrigerantes[x].descricao;
        valor.textContent = `R$ ${refrigerantes[x].valor.toFixed(2).replace('.',',')}`;
        valor.classList.add("price")
        button.textContent = "Adicionar ao Carrinho";
        button.addEventListener("click", adicionarRefrigeranteNoCarrinho);



        refrigerante.appendChild(img)
        refrigerante.appendChild(titulo)
        refrigerante.appendChild(descricao)
        refrigerante.appendChild(valor)
        refrigerante.appendChild(button)
        refrigerante.classList.add("menu-item")

        catalogo.appendChild(refrigerante);
    }
}

function adicionarRefrigeranteNoCarrinho(evento) {
    const refrigerante_id = evento.target.parentElement.id;
    const refrigerante = obterRefrigerantePorId(refrigerante_id);

    const { id, titulo, valor } = refrigerante

    carrinho.push({ id, titulo, valor });
    console.log(carrinho)
    localStorage.setItem("carrinho", JSON.stringify(carrinho))
}

function obterRefrigerantePorId(id) {
    for (let refrigerante of refrigerantes) {
        if (refrigerante.id === id) {
            return refrigerante;
        }
    }
    return null;
}