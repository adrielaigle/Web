import { db } from "./db.js"

const cardapio = [
    
    {
        tipo: "os-mais-pedidos",
        id: "item-0",
        img: "../images/pizzas-tradicionais/pizza-margherita.jpg",
        titulo: "Margherita",
        descricao: "Molho de tomate, mussarela, tomate fresco e manjericão.",
        valor: 25.0
    },

    {
        tipo: "os-mais-pedidos",
        id: "item-1",
        img: "../images/pizzas-doces/pizza-romeu-e-julieta.jpg",
        titulo: "Romeu e Julieta",
        descricao: "Mussarela, goiabada, açúcar mascavo.",
        valor: 25.0
    },

    {
        tipo: "os-mais-pedidos",
        id: "item-2",
        img: "../images/refrigerantes/refrigerante-coca-cola.jpg",
        titulo: "Refrigerante Coca-Cola",
        descricao: "2 Litros",
        valor: 10.0
    },

    {
        tipo: "os-mais-pedidos",
        id: "item-3",
        img: "../images/pizzas-tradicionais/pizza-moda-da-casa.jpg",
        titulo: "A Moda da Casa",
        descricao: "Mussarela, peito de frango desfiado, bacon e azeitonas.",
        valor: 30.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-0",
        img: "../images/pizzas-tradicionais/pizza-margherita.jpg",
        titulo: "Margherita",
        descricao: "Molho de tomate, mussarela, tomate fresco e manjericão.",
        valor: 25.0
    },
    
    {
        tipo: "pizzas-tradicionais",
        id: "pizza-1",
        img: "../images/pizzas-tradicionais/pizza-calabresa.jpg",
        titulo: "Calabresa",
        descricao: "Molho de tomate, mussarela, calabresa fatiada e cebola.",
        valor: 25.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-2",
        img: "../images/pizzas-tradicionais/pizza-frango-com-catupiry.jpg",
        titulo: "Frango com Catupiry",
        descricao: "Molho de tomate, frango desfiado, catupiry e orégano.",
        valor: 25.0
    }, 

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-3",
        img: "../images/pizzas-tradicionais/pizza-quatro-queijos.jpg",
        titulo: "Quatro Queijos",
        descricao: "Mussarela, parmesão, gorgonzola e provolone.",
        valor: 25.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-4",
        img: "../images/pizzas-tradicionais/pizza-portuguesa.jpg",
        titulo: "Portuguesa",
        descricao: "Mussarela, presunto, ovo, cebola, pimentão e azeitonas.",
        valor: 25.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-5",
        img: "../images/pizzas-tradicionais/pizza-napolitana.jpg",
        titulo: "Napolitana",
        descricao: "Molho de tomate, mussarela, tomate seco e manjericão.",
        valor: 30.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-6",
        img: "../images/pizzas-tradicionais/pizza-pepperoni.jpg",
        titulo: "Pepperoni",
        descricao: "Molho de tomate, mussarela e pepperoni fatiado.",
        valor: 25.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-7",
        img: "../images/pizzas-tradicionais/pizza-veggie.jpg",
        titulo: "Veggie",
        descricao: "Mussarela, cogumelos, abobrinha, berinjela e pimentões.",
        valor: 25.0
    },

    {
        tipo: "pizzas-tradicionais",
        id: "pizza-8",
        img: "../images/pizzas-tradicionais/pizza-bacon-com-cheddar.jpg",
        titulo: "Bacon com Cheddar",
        descricao: "Molho de tomate, mussarela, bacon crocante e cheddar.",
        valor: 25.0
    },
    
    {
        tipo: "pizzas-tradicionais",
        id: "pizza-9",
        img: "../images/pizzas-tradicionais/pizza-moda-da-casa.jpg",
        titulo: "A Moda da Casa",
        descricao: "Mussarela, peito de frango desfiado, bacon e azeitonas.",
        valor: 30.0
    },

    {
        tipo: "pizzas-doces",
        id: "pizza-10",
        img: "../images/pizzas-doces/pizza-chocolate-com-morango.jpg",
        titulo: "Chocolate com Morango",
        descricao: "Creme de chocolate, morangos frescos e chantilly.",
        valor: 25.0
    },

    {
        tipo: "pizzas-doces",
        id: "pizza-11",
        img: "../images/pizzas-doces/pizza-banana-com-canela.jpg",
        titulo: "Banana com Canela",
        descricao: "Fatias de banana, açúcar, canela e cobertura de chocolate.",
        valor: 25.0
    },

    {
        tipo: "pizzas-doces",
        id: "pizza-12",
        img: "../images/pizzas-doces/pizza-brigadeiro.jpg",
        titulo: "Brigadeiro",
        descricao: "Creme de brigadeiro, granulado e bolinhas de brigadeiro.",
        valor: 25.0
    },

    {
        tipo: "pizzas-doces",
        id: "pizza-13",
        img: "../images/pizzas-doces/pizza-romeu-e-julieta.jpg",
        titulo: "Romeu e Julieta",
        descricao: "Mussarela, goiabada, açúcar mascavo.",
        valor: 25.0
    },

    {
        tipo: "pizzas-doces",
        id: "pizza-14",
        img: "../images/pizzas-doces/pizza-delícia-de-coco.jpg",
        titulo: "Delícia de Coco",
        descricao: "Massa com Nutella, coco ralado e pedaços de chocolate branco.",
        valor: 25.0
    },

    {
        tipo: "refrigerantes",
        id: "refrigerante-0",
        img: "../images/refrigerantes/refrigerante-coca-cola.jpg",
        titulo: "Refrigerante Coca-Cola",
        descricao: "2 Litros",
        valor: 10.0
    },

    {
        tipo: "refrigerantes",
        id: "refrigerante-1",
        img: "../images/refrigerantes/refrigerante-guaraná-antarctica.jpg",
        titulo: "Guaraná Antarctica",
        descricao: "2,5 Litros",
        valor: 8.0
    },

    {
        tipo: "refrigerantes",
        id: "refrigerante-2",
        img: "../images/refrigerantes/refrigerante-sprite.jpg",
        titulo: "Refrigerante Sprite",
        descricao: "2 Litros",
        valor: 9.0
    },

    {
        tipo: "refrigerantes",
        id: "refrigerante-3",
        img: "../images/refrigerantes/refrigerante-fanta-uva.jpg",
        titulo: "Fanta Uva",
        descricao: "2 Litros",
        valor: 7.0
    },

    {
        tipo: "refrigerantes",
        id: "refrigerante-4",
        img: "../images/refrigerantes/refrigerante-lata.jpg",
        titulo: "Refrigerante Lata",
        descricao: "350ml | Especificar Sabor",
        valor: 5.0
    }
];

for (let x = 0; x < cardapio.length; x++) {
    await db.run(`
        INSERT INTO cardapio (tipo, id, titulo, img, descricao, valor) 
        VALUES (?,?,?,?,?,?)
        `, [cardapio[x].tipo,
        cardapio[x].id,
        cardapio[x].titulo,
        cardapio[x].img,
        cardapio[x].descricao,
        cardapio[x].valor]
    )
}