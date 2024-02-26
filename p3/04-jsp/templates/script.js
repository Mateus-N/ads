const botoes = document.querySelectorAll(".botaoConcluido");

botoes.forEach(botao => {
    botao.addEventListener('change', () => {
        const paragrafo = botao.parentNode.parentNode.querySelector("#descricao");
        if(botao.checked){
            paragrafo.classList.add("conclusao");
        } else {
            paragrafo.classList.remove("conclusao")
        }
    })
})
