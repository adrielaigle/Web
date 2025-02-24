let soma = 0;
for(let x = 2; x <= 100; x+=2){
    soma += x;
}

const p = document.getElementById("soma");

p.textContent = "Soma total: " + soma