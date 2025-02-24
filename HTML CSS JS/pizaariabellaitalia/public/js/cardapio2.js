window.addEventListener("load", main);

let carrinho = [];
const carrinho_lc = localStorage.getItem("carrinho");
if (carrinho_lc == null) {
    localStorage.setItem("carrinho", "[]");
} else {
    carrinho = JSON.parse(carrinho_lc);
}

let pizzas = [];

async function main() {
    const catalogo = document.getElementsByClassName("menu-container")[0];
    const resposta = await fetch("http://localhost:55555/api/cardapio");
    const todos_os_produtos = await resposta.json();

    for (let x = 0; x < todos_os_produtos.length; x++) {
        if (todos_os_produtos[x].tipo === "pizzas-doces") {
            pizzas.push(todos_os_produtos[x]);
        }
    }

    for (let x = 0; x < pizzas.length; x++) {
        const pizza = document.createElement("div");
        const img = document.createElement("img");
        const titulo = document.createElement("h3");
        const descricao = document.createElement("p");
        const valor = document.createElement("p");
        const quantidadeLabel = document.createElement("label");
        const quantidadeInput = document.createElement("input");
        const button = document.createElement("button");

        pizza.id = pizzas[x].id;
        img.src = pizzas[x].img;
        img.alt = pizzas[x].titulo;
        titulo.textContent = pizzas[x].titulo;
        descricao.textContent = pizzas[x].descricao;
        valor.textContent = `R$ ${pizzas[x].valor.toFixed(2).replace('.', ',')}`;
        valor.classList.add("price");

        quantidadeLabel.textContent = "Quantidade:";
        quantidadeInput.type = "number";
        quantidadeInput.min = "1";
        quantidadeInput.step = "1";
        quantidadeInput.value = "1";
        quantidadeInput.classList.add("quantidade");

        button.textContent = "Adicionar ao Carrinho";
        button.setAttribute("data-id", pizzas[x].id);
        button.setAttribute("data-titulo", pizzas[x].titulo);
        button.setAttribute("data-valor", pizzas[x].valor);
        button.setAttribute("data-img", pizzas[x].img);
        button.addEventListener("click", adicionarPizzaNoCarrinho);

        pizza.appendChild(img);
        pizza.appendChild(titulo);
        pizza.appendChild(descricao);
        pizza.appendChild(valor);
        pizza.appendChild(quantidadeLabel);
        pizza.appendChild(quantidadeInput);
        pizza.appendChild(button);
        pizza.classList.add("menu-item");

        catalogo.appendChild(pizza);
    }
}

function adicionarPizzaNoCarrinho(evento) {
    const botao = evento.target;

    const pizza_id = botao.getAttribute("data-id");
    const titulo = botao.getAttribute("data-titulo");
    const valor = parseFloat(botao.getAttribute("data-valor"));
    const img = botao.getAttribute("data-img");

    const pizzaDiv = botao.closest(".menu-item");
    const quantidadeInput = pizzaDiv.querySelector(".quantidade");
    const quantidade = parseInt(quantidadeInput.value);

    if (isNaN(quantidade) || quantidade <= 0) {
        alert("Por favor, insira uma quantidade válida.");
        return;
    }

    let itemExistente = carrinho.find(item => item.id === pizza_id);
    if (itemExistente) {
        itemExistente.quantidade += quantidade;
    } else {
        carrinho.push({
            id: pizza_id,
            titulo: titulo,
            valor: valor,
            img: img, 
            quantidade: quantidade
        });
    }

    console.log(carrinho); 
    localStorage.setItem("carrinho", JSON.stringify(carrinho));
}