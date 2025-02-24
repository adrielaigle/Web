let num = +prompt("Digite um número: ")
const p = document.getElementById("tabuada")

for (let n = +1; n <= 10; n++) {
    p.textContent = `${p.textContent} ----- ${num} x ${n} = ${num * n}`
}