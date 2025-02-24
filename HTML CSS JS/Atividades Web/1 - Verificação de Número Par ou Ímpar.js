let numero = +prompt("Digite um número maior que 0")

const p = document.getElementById("parImpar")

while(numero <=0 || isNaN(+numero)) {
    numero = +prompt("Digite um número maior que 0")
}

if (numero % 2 == 0) {
    p.textContent = "número par"
} else {
    p.textContent = "número impar"
}