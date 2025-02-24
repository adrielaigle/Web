let cor = prompt("Informe uma cor em inglês")
const p = document.getElementById("cor")

switch(cor) {
    case "red":
        p.textContent = "Vermelho"
        break;
    case "blue":
        p.textContent = "Azul"
        break
    case "black":
        p.textContent = "Preto"
        break
    case "white":
        p.textContent = "Branco"
        break
    case "green":
        p.textContent = "Verde"
        break
    default:
        p.textContent = "Cor desconhecida"
}