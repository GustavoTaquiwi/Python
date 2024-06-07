document.addEventListener('DOMContentLoaded', function() {
    const tabuadaContainer = document.getElementById('tabuadaContainer');

    function gerarTabuada(numero) {
        let tabuada = '<table>';
        tabuada += `<caption>Tabuada do ${numero}</caption>`;
          // Loop que itera de 1 a 10 para gerar os valores da tabuada
        for (let i = 1; i <= 10; i++) {
            // Adiciona uma linha à tabela com o resultado da multiplicação
            tabuada += `<tr><td>${numero} x ${i}</td><td>${numero * i}</td></tr>`;
        }
        tabuada += '</table>';
        tabuadaContainer.innerHTML = tabuada;
    }

    const botao = document.querySelector('button');
    // Adiciona um ouvinte de evento para o evento de clique no botão
    botao.addEventListener('click', function(event) {
        event.preventDefault(); // Evita a atualização da página
        const numero = parseInt(document.getElementById('numero').value);
        // Verifica se o valor digitado é um número inteiro
        if (Number.isInteger(numero)) {
            gerarTabuada(numero);
            // Se não for um número inteiro, exibe uma mensagem de erro
        } else {
            tabuadaContainer.innerHTML = '<p style="color: red;">Por favor, insira um número inteiro válido.</p>';
        }
    });
});
