window.addEventListener("load", main);

let carrinho = [];
const carrinho_lc = localStorage.getItem("carrinho");
if (carrinho_lc == null) {
    localStorage.setItem("carrinho", "[]");
} else {
    carrinho = JSON.parse(carrinho_lc);
}

let produtos = [];

async function main() {
    const catalogo = document.getElementsByClassName("menu-container")[0];
    const resposta = await fetch("http://localhost:55555/api/cardapio");
    const todos_os_produtos = await resposta.json();

    for (let x = 0; x < todos_os_produtos.length; x++) {
        if (todos_os_produtos[x].tipo === "os-mais-pedidos") {
            produtos.push(todos_os_produtos[x]);
        }
    }

    for (let x = 0; x < produtos.length; x++) {
        const produto = document.createElement("div");
        const img = document.createElement("img");
        const titulo = document.createElement("h3");
        const descricao = document.createElement("p");
        const valor = document.createElement("p");
        const quantidadeLabel = document.createElement("label");
        const quantidadeInput = document.createElement("input");
        const button = document.createElement("button");

        produto.id = produtos[x].id;
        img.src = produtos[x].img;
        img.alt = produtos[x].titulo;
        titulo.textContent = produtos[x].titulo;
        descricao.textContent = produtos[x].descricao;
        valor.textContent = `R$ ${produtos[x].valor.toFixed(2).replace('.', ',')}`;
        valor.classList.add("price");

        quantidadeLabel.textContent = "Quantidade:";
        quantidadeInput.type = "number";
        quantidadeInput.min = "1";
        quantidadeInput.step = "1";
        quantidadeInput.value = "1";
        quantidadeInput.classList.add("quantidade");

        button.textContent = "Adicionar ao Carrinho";
        button.setAttribute("data-id", produtos[x].id);
        button.setAttribute("data-titulo", produtos[x].titulo);
        button.setAttribute("data-valor", produtos[x].valor);
        button.setAttribute("data-img", produtos[x].img);
        button.addEventListener("click", adicionarprodutoNoCarrinho);

        produto.appendChild(img);
        produto.appendChild(titulo);
        produto.appendChild(descricao);
        produto.appendChild(valor);
        produto.appendChild(quantidadeLabel);
        produto.appendChild(quantidadeInput);
        produto.appendChild(button);
        produto.classList.add("menu-item");

        catalogo.appendChild(produto);
    }
}

function adicionarprodutoNoCarrinho(evento) {
    const botao = evento.target;

    const produto_id = botao.getAttribute("data-id");
    const titulo = botao.getAttribute("data-titulo");
    const valor = parseFloat(botao.getAttribute("data-valor"));
    const img = botao.getAttribute("data-img");

    const produtoDiv = botao.closest(".menu-item");
    const quantidadeInput = produtoDiv.querySelector(".quantidade");
    const quantidade = parseInt(quantidadeInput.value);

    if (isNaN(quantidade) || quantidade <= 0) {
        alert("Por favor, insira uma quantidade válida.");
        return;
    }

    let itemExistente = carrinho.find(item => item.id === produto_id);
    if (itemExistente) {
        itemExistente.quantidade += quantidade;
    } else {
        carrinho.push({
            id: produto_id,
            titulo: titulo,
            valor: valor,
            img: img,
            quantidade: quantidade
        });
    }

    console.log(carrinho);
    localStorage.setItem("carrinho", JSON.stringify(carrinho));
}