window.addEventListener("load", main)

let carrinho = []

const carrinho_lc = localStorage.getItem("carrinho")
if (carrinho_lc == null) {
    localStorage.setItem("carrinho", "[]")
} else {
    carrinho = JSON.parse(carrinho_lc);
}

let pizzas = [
]

async function main() {
    const catalogo = document.getElementsByClassName("menu-container")[0]
    const resposta = await fetch("http://localhost:55555/api/cardapio")
    todos_os_produtos = await resposta.json()
    for (let x = 0; x < todos_os_produtos.length; x++) {
        if (todos_os_produtos[x].tipo === "pizzas-doces") {
            pizzas.push(todos_os_produtos[x])
        }
    }

    for (let x = 0; x < pizzas.length; x++) {

        const pizza = document.createElement("div");
        const img = document.createElement("img");
        const titulo = document.createElement("h3");
        const descricao = document.createElement("p");
        const valor = document.createElement("p");
        const button = document.createElement("button");

        pizza.id = pizzas[x].id;

        img.src = pizzas[x].img;
        titulo.textContent = pizzas[x].titulo;
        descricao.textContent = pizzas[x].descricao;
        valor.textContent = `R$ ${pizzas[x].valor.toFixed(2).replace('.',',')}`;
        valor.classList.add("price")
        button.textContent = "Adicionar ao Carrinho";
        button.addEventListener("click", adicionarPizzaNoCarrinho);



        pizza.appendChild(img)
        pizza.appendChild(titulo)
        pizza.appendChild(descricao)
        pizza.appendChild(valor)
        pizza.appendChild(button)
        pizza.classList.add("menu-item")

        catalogo.appendChild(pizza);
    }
}

function adicionarPizzaNoCarrinho(evento) {
    const pizza_id = evento.target.parentElement.id;
    const pizza = obterPizzaPorId(pizza_id);

    const { id, titulo, valor } = pizza

    carrinho.push({ id, titulo, valor });
    console.log(carrinho)
    localStorage.setItem("carrinho", JSON.stringify(carrinho))
}

function obterPizzaPorId(id) {
    for (let pizza of pizzas) {
        if (pizza.id === id) {
            return pizza;
        }
    }
    return null;
}