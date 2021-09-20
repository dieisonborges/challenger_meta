# challenger_meta

[<img src="https://www.meta.com.br/wp-content/uploads/2021/01/1.png" width="250"/>](meta.png)

# Build
[![Build Status](https://app.travis-ci.com/dieisonborges/challenger_meta.svg?branch=main)](https://app.travis-ci.com/dieisonborges/challenger_meta)

# DESAFIO
## DESENVOLVEDOR FULLSTACK

### O QUE BUSCAMOS?

Buscamos pessoas que gostem muito de programar e se preocupam com
excelência técnica, boas práticas de programação e uma visão sistêmica do
negócio. Além de ter boa capacidade de comunicação e habilidade de trabalhar e
construir um relacionamento com os times no nosso ambiente dinâmico e ágil.

# STACK

Trabalhamos hoje com aplicações com backend em python e node.js.
Já no frontend, uniformizamos todas as aplicações com o vue.js.

## PARTE I

**BACKEND**

# O DESAFIO

Teremos 4 questões para avaliar a capacidade de análise e
resolução de problemas através de algoritimos.
Escolha entre as linguagens python e node.js.
Tente resolver o maior número de questões que
conseguir :)

## QUESTÃO I

Dado um array de números inteiros, retorne os índices dos
dois números de forma que eles se somem a um alvo
específico.
Voc ê pode assumir que cada entrada teria exatamente uma

### EXEMPLO

Dado nums = [2, 7, 11, 15], alvo = 9,
Como nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
solu ç ão, e voc ê não pode usar o mesmo elemento duas
vezes.

## QUESTÃO II

Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, }, [ ou ].
Dois brackets são considerados um par combinado se o bracket de abertura (isto
é, (, [ou {) ocorre à esquerda de um bracket de fechamento (ou seja,),] ou} do
mesmo tipo exato. Existem tr ê s tipos de pares de brackets : [ ], { } e ( ). 

### EXEMPLO

Um par de brackets correspondente não é balanceado se o de abertura e o de {[()]} SIM
{[(])} NAO
{{[[(())]]}} SIM
fechamento não corresponderem entre si. Por exemplo, { [ ( ] ) } não é balanceado
porque o conteúdo entre {e} não é balanceado. O primeiro bracket inclui o de
abertura, (, e o segundo inclui um bracket de fechamento desbalanceado,].
Dado sequencias de caracteres, determine se cada sequ ê ncia de brackets é
balanceada. Se uma string estiver balanceada, retorne SIM. Caso contrário, retorne
NAO.

## QUESTÃO III

Digamos que voc ê tenha um array para o qual o elemento i
é o preço de uma determinada ação no dia i.
Se voc ê tivesse permissão para concluir no máximo uma
transa ç ão (ou seja, comprar uma e vender uma a ç ão), crie
um algoritmo para encontrar o lucro máximo.
Note que voc ê não pode vender uma a ç ão antes de
comprar.

### EXEMPLO

Input: [7,1,5,3,6,4]
Output: 5 (Comprou no dia 2 (preço
igual a 1) e vendeu no dia 5 (preço
igual a 6), lucro foi de 6 – 1 = 5
Input: [7,6,4,3,1]
Output: 0 (Nesse caso nenhuma
transação deve ser feita, lucro máximo
igual a 0)

## QUESTÃO IV

Dados n inteiros não negativos representando um mapa de
eleva ç ão onde a largura de cada barra é 1, calcule quanta
água é capaz de reter após a chuva.

### EXEMPLO
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6