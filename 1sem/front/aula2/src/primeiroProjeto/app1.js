let but = document.querySelector("button")
but.addEventListener('click', somarUm)

function somarUm() {
    console.log("Clicou 🍻")
    let elementoH3 = document.querySelector("h3")
    let valor = elementoH3.textContent
    let novoValor = parseInt(valor) + 1
    elementoH3.textContent = novoValor

    let r = parseInt(Math.random() * 256)
    let g = parseInt(Math.random() * 256)
    let b = parseInt(Math.random() * 256)

    if (novoValor > valor) {
        elementoH3.style.color = `rgb(${r}, ${g}, ${b})`
    } 
}