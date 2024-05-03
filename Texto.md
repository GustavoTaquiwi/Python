### SWITCH

A condicional switch avalia uma expressão, combinando o valor da expressão para um cláusula case.
A estrutura condicional switch permite executar um bloco de código diferente de acordo com cada opção (cada case) especificada. Seu uso é indicado quando os valores a serem analisados nessas condições são pré-definidos.

### Exemplo 01:

    switch (expressão) {
        case valor1:
            //Instruções executadas quando o resultado da expressão for igual á valor1
            [break;]
        case valor2:
            //Instruções executadas quando o resultado da expressão for igual á valor2
            [break;]

    O programa primeiro procura por um caso o qual a expressão avalie como tendo o mesmo valor que o input da expressão transferindo assim o controle para a cláusula encontrada e em seguida executando as instruções associadas.

### Exemplo 2:

    switch (expr) {
        case "Laranjas":
            console.log("As laranjas custam $0.59 o quilo.");
            break;

        case "Maçãs":
            console.log("Maçãs custam $0.32 o quilo.");
            break;
        case "Bananas":
            console.log("Bananas custam $0.48 o quilo.");
            break;
         case "Cerejas":
        console.log("Cerejas custam $3.00 o quilo.");
            break;
         case "Mangas":
        case "Mamões":
            console.log("Mangas e mamões custam $2.79 o quilo.");
            break;
    default:
             console.log("Desculpe, estamos sem nenhuma " + expr + ".");

        console.log("Tem algo mais que você gostaria de levar?");

o programa corresponde o valor com o case "Bananas" e executa a instrução associada. Quando break for encontrado, o programa para (break), saindo de switch e executa a instrução localizada após o switch. Se break fosse omitido, a instrução para "Cherries" também seria executada.