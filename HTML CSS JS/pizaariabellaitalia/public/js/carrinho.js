window.addEventListener("load", () => {
    renderizarCarrinho();
});

function main() {
    const carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];
    renderizarCarrinho(carrinho);
}

function renderizarCarrinho(carrinho = JSON.parse(localStorage.getItem("carrinho")) || []) {
    const carrinhoContainer = document.getElementById("carrinho-produtos");
    const subtotalElem = document.getElementById("subtotal");
    const totalElem = document.getElementById("total");

    if (!carrinhoContainer) {
        console.error("Contêiner do carrinho não encontrado.");
        return;
    }

    carrinhoContainer.innerHTML = "";

    if (carrinho.length === 0) {
        carrinhoContainer.innerHTML = "<p>Seu carrinho está vazio.</p>";
        subtotalElem.textContent = "R$ 0,00";
        totalElem.textContent = "R$ 7,00"; 
        return;
    }

    let total = 0;

    carrinho.forEach((item, index) => {
        item.quantidade = item.quantidade || 1;

        const precoUnitario = parseFloat(item.valor) || 0;
        const precoTotal = precoUnitario * item.quantidade;

        const produtoDiv = document.createElement("div");
        produtoDiv.classList.add("produto");

        produtoDiv.innerHTML = `
            <div class="coluna">
                <img src="${item.img}" alt="${item.titulo}" onerror="this.src=''">
                <p>${item.titulo}</p>
            </div>
            <div class="coluna">
                <p>${item.descricao}</p>
            </div>
            <div class="coluna">
                <div class="botao-quantidade-produto">
                    <button class="btn-diminuir" onclick="alterarQuantidade(${index}, -1)">−</button>
                    <span id="quantidade${index}">${item.quantidade}</span>
                    <button class="btn-aumentar" onclick="alterarQuantidade(${index}, 1)">+</button>
                </div>
            </div>
            <div class="coluna">
                <p id="totalItem${index}"> R$${precoTotal.toFixed(2).replace('.', ',')}</p>
            </div>
            <div class="coluna">
                <button class="remover-produto" onclick="removerDoCarrinho(${index})">Excluir produto</button>
            </div>
        `;

        carrinhoContainer.appendChild(produtoDiv);
        total += precoTotal;
    });

    subtotalElem.textContent = `R$ ${total.toFixed(2).replace('.', ',')}`;
    totalElem.textContent = `R$ ${(total + 7).toFixed(2).replace('.', ',')}`; 

    localStorage.setItem("carrinho", JSON.stringify(carrinho));
}

function alterarQuantidade(index, quantidade) {
    let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];
    
    if (carrinho[index]) {
        carrinho[index].quantidade += quantidade;

        if (carrinho[index].quantidade <= 0) {
            carrinho.splice(index, 1); 
        }
        
        localStorage.setItem("carrinho", JSON.stringify(carrinho));
        renderizarCarrinho(carrinho);
    }
}

function removerDoCarrinho(index) {
    let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];

    if (carrinho.length > 0) {
        carrinho.splice(index, 1); 
        localStorage.setItem("carrinho", JSON.stringify(carrinho)); 
        renderizarCarrinho(carrinho); 
    }
}

function adicionarAoCarrinho(id, img, titulo, descricao, valor) {
    let carrinho = JSON.parse(localStorage.getItem("carrinho")) || [];
    let itemExistente = carrinho.find(item => item.id === id);

    if (itemExistente) {
        itemExistente.quantidade += 1; 
    } else {
        carrinho.push({
            id: id,
            img: img,
            titulo: titulo,
            descricao: descricao,
            valor: valor,
            quantidade: 1 
        });
    }

    localStorage.setItem("carrinho", JSON.stringify(carrinho));
    renderizarCarrinho();
}