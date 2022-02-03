
/**
 * [1] - Varaiáveis:
 *      Existem algumas formas para se declarar uma váriavel no JavaScript:
 *          a. usando var:
 *                 var nome_variavel = valor;
 *                 
 *          b. usando let:
 *                  let nome_variavel = valor;
 * 
 *                  Variavel declarada como let não pode ser 'redeclarada' no escopo do programa.
 * 
 *          c. usando const:
 *                  const nome_variavel = valor;
 *                  
 *                  Ao usar const para declarar uma variavel, ela não poderá ter seu valor
 *                  alterado durante a execução do programa.
 *  
 */


// Usando var:
var x = 5;
var y = 6;
var z = x + y;

// Usando let
let a = 10;
let b = 13;
let c = a - b;

// Usando const
const pi = 3.1415;
const preco1 = 4;
const preco2 = 5;
let total = preco1 + preco2;

// Redeclarando variaveis
var x = 100;
var x = 0;  // isso funciona

let y = 50;
let y = 0; // isso não funciona e gera um SyntaxError

