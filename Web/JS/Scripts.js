
 //Faz um alert na pagina 

 //alert('Palmeiras Perde todas em 2024')

// tipos primitivos

var nome = "Eu"; //String
let numero = 01; //Inteiro
let verdade = true; //booleano
let texto; //Indefinido
let texto2 = null; //Vazio


console.log(nome);
let sobrenome = "Nos";
console.log(sobrenome);

// Adiçao

let num1 = 1;
let num2 = 2;

console.log(num1+num2);

//Subtraçao

console.log(num1-num2);
//Multiplicaçao

console.log(num1**num2);
//divisao

console.log(num1/num2);
//potencia

console.log(num1^num2);
// resto divisao

console.log(num1%num2);

// Operadores de comparaçao
console.log(5 == 5); //Verdadeiro numeros iguais

console.log(5 === "5"); // falso pq nao sao identicos

console.log(5 > 7); // Maior

console.log(5 < 7); // Menor

console.log(5 != 5); //Diferente

// Operadores Logicos

 // && AND
 // || OR
 // !  NOT

let a = 5;
let b = 10;

console.log(a > 0 && b > 15); //Operador And se 1 for false, todos sâo.
console.log(a > 2 || b > 15); // se 1 for verdadeiro ja basta
console.log(a > 3 && !b > 10); 

let resposta = confirm ('Palmeiras e Horrivel?'); //Exibe mensagem
console.log(resposta);

let resposta2 = prompt ('Palmeiras e Horrivel?'); //Prompt da funçao de digitar
console.log(resposta2);