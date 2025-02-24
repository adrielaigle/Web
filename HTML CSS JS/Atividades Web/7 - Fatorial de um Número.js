let numero = parseInt(prompt("Digite um número inteiro positivo (menor ou igual a 10):"));
const p = document.getElementById("fatorial")
let fatorial = 1;

while(numero > 10 || isNaN(+numero)) {
    numero = parseInt(prompt("Digite um número inteiro positivo (menor ou igual a 10):"));
}

for (let i = 1; i <= numero; i++) {
  fatorial *= i;
}

p.textContent = (`O fatorial de ${numero} é ${fatorial}`);