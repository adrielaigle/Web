let nota = +prompt("Digite uma nota de 0 a 100")
const p = document.getElementById("nota")

while(nota < 0 || nota > 100 || isNaN(+nota)) {
    nota = +prompt("Digite uma nota de 0 a 100")
}

if (nota >=90) {
    p.textContent = "A"
} else if (nota >=80) {
    p.textContent = "B"
} else if (nota >= 70) {
    p.textContent = "C"    
} else if (nota >=60) {
    p.textContent = "D"
} else if (nota <60) {
    p.textContent = "F"
}