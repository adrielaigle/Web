window.addEventListener("load", main);

let carrinho = [];
const carrinho_lc = localStorage.getItem("carrinho");
if (carrinho_lc == null) {
    localStorage.setItem("carrinho", "[]");
} else {
    carrinho = JSON.parse(carrinho_lc);
}

let refrigerantes = [];

async function main() {
    const catalogo = document.getElementsByClassName("menu-container")[0];
    const resposta = await fetch("http://localhost:55555/api/cardapio");
    const todos_os_produtos = await resposta.json();

    for (let x = 0; x < todos_os_produtos.length; x++) {
        if (todos_os_produtos[x].tipo === "refrigerantes") {
            refrigerantes.push(todos_os_produtos[x]);
        }
    }

    for (let x = 0; x < refrigerantes.length; x++) {
        const refrigerante = document.createElement("div");
        const img = document.createElement("img");
        const titulo = document.createElement("h3");
        const descricao = document.createElement("p");
        const valor = document.createElement("p");
        const quantidadeLabel = document.createElement("label");
        const quantidadeInput = document.createElement("input");
        const button = document.createElement("button");

        refrigerante.id = refrigerantes[x].id;
        img.src = refrigerantes[x].img;
        img.alt = refrigerantes[x].titulo;
        titulo.textContent = refrigerantes[x].titulo;
        descricao.textContent = refrigerantes[x].descricao;
        valor.textContent = `R$ ${refrigerantes[x].valor.toFixed(2).replace('.', ',')}`;
        valor.classList.add("price");

        quantidadeLabel.textContent = "Quantidade:";
        quantidadeInput.type = "number";
        quantidadeInput.min = "1";
        quantidadeInput.step = "1";
        quantidadeInput.value = "1";
        quantidadeInput.classList.add("quantidade");

        button.textContent = "Adicionar ao Carrinho";
        button.setAttribute("data-id", refrigerantes[x].id);
        button.setAttribute("data-titulo", refrigerantes[x].titulo);
        button.setAttribute("data-valor", refrigerantes[x].valor);
        button.setAttribute("data-img", refrigerantes[x].img);
        button.addEventListener("click", adicionarrefrigeranteNoCarrinho);

        refrigerante.appendChild(img);
        refrigerante.appendChild(titulo);
        refrigerante.appendChild(descricao);
        refrigerante.appendChild(valor);
        refrigerante.appendChild(quantidadeLabel);
        refrigerante.appendChild(quantidadeInput);
        refrigerante.appendChild(button);
        refrigerante.classList.add("menu-item");

        catalogo.appendChild(refrigerante);
    }
}

function adicionarrefrigeranteNoCarrinho(evento) {
    const botao = evento.target;

    const refrigerante_id = botao.getAttribute("data-id");
    const titulo = botao.getAttribute("data-titulo");
    const valor = parseFloat(botao.getAttribute("data-valor"));
    const img = botao.getAttribute("data-img");

    const refrigeranteDiv = botao.closest(".menu-item"); 
    const quantidadeInput = refrigeranteDiv.querySelector(".quantidade");
    const quantidade = parseInt(quantidadeInput.value);

    if (isNaN(quantidade) || quantidade <= 0) {
        alert("Por favor, insira uma quantidade válida.");
        return;
    }

    let itemExistente = carrinho.find(item => item.id === refrigerante_id);
    if (itemExistente) {
        itemExistente.quantidade += quantidade;
    } else {
        carrinho.push({
            id: refrigerante_id,
            titulo: titulo,
            valor: valor,
            img: img, 
            quantidade: quantidade
        });
    }

    console.log(carrinho); 
    localStorage.setItem("carrinho", JSON.stringify(carrinho));
}