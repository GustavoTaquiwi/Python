let textoString = "10,25";

numero = parseFloat(textoString);
console.log(typeof(numero));

const tabela = document.querySelector("#tabela");
let linha_nova = tabela.insertRow();
let celula_nova = linha_nova.insertCell()
let celula_nova2 = linha_nova.insertCell();;

celula_nova.innerHTML = "Putaqpario";
celula_nova2.innerHTML = "10";

const exemplo_1 = document.querySelector('exemplo_1');
exemplo_1.TextContent = "<p>eu</p>";