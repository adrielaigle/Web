window.addEventListener("load", main)

function main() {
    const inputAlice = document.getElementById("Alice");
    const inputBob = document.getElementById("Bob");
    inputAlice.addEventListener("keyup", criarConversa);
    inputBob.addEventListener("keyup", criarConversa);
}

function criarConversa(evento) {
    if (evento.key === "Enter") {
        const mensagem = evento.target.value;
        const divConversa = document.querySelector(".conversa");
        const p = document.createElement("p");
        p.textContent = mensagem;
        if (evento.target.id === "Alice") {
            p.classList.add("mensagem-alice"); 
        } else if (evento.target.id === "Bob") {
            p.classList.add("mensagem-bob"); 
        }
        divConversa.appendChild(p);
        evento.target.value = "";
    }
}
