// Seleciona o formulário com o id "formulario_aluno" e armazena-o na variável 'formulario'
const formulario = document.querySelector("#formulario_aluno");
// Seleciona a tabela com o id "corpo_tabela" e armazena-a na variável 'tabela'
const tabela = document.querySelector("#corpo_tabela")
// Adiciona um ouvinte de evento ao formulário que é acionado quando o formulário é submetido
formulario.addEventListener("submit", function (event) {
// Previne o comportamento padrão do formulário, que é recarregar a página
    event.preventDefault();
// Obtém os valores dos campos de entrada do formulário
 let nome = document.querySelector("#nome").value;
 let nota1 = parseFloat(document.querySelector("#nota1").value);
 let nota2 = parseFloat(document.querySelector("#nota2").value); 
 let nota3 = parseFloat(document.querySelector("#nota3").value); 
 let nota4 = parseFloat(document.querySelector("#nota4").value);
//Calculo da Media
 let media = (nota1+nota2+nota3+nota4)/4
// Insere uma nova linha na tabela
 let linha_tabela = tabela.insertRow()
 // Insere células na nova linha da tabela;
 let celula_nome = linha_tabela.insertCell();
 let celula_nota1 = linha_tabela.insertCell();
 let celula_nota2 = linha_tabela.insertCell();
 let celula_nota3 = linha_tabela.insertCell();
 let celula_nota4 = linha_tabela.insertCell();
 let celula_media = linha_tabela.insertCell();
// Define o conteúdo das células da nova linha da tabela
 celula_nome.innerHTML = nome;
 celula_nota1.innerHTML = nota1;
 celula_nota2.innerHTML = nota2;
 celula_nota3.innerHTML = nota3;
 celula_nota4.innerHTML = nota4;
 celula_media.innerHTML = media.toFixed(2); })  // Limita a média a duas casas decimais