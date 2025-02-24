const nota1 = prompt("Primeira nota: ")
const nota2 = prompt("Segunda nota: ")
const nota3 = prompt("Terceira nota: ")
const nota4 = prompt("Quarta nota: ")

const p = document.getElementById("media")

const media = (+nota1 + +nota2 + +nota3 + +nota4) / 4
if (media >=7) {
    p.textContent = `Aprovado: Media ${media}`
}
if (media < 7) {
    p.textContent = `Reprovado: Media ${media}`
}