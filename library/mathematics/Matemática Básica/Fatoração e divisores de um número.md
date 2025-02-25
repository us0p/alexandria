Todo [número composto](Termos%20gerais.md#Número%20Composto) pode ser re-escrito como um [produto](Termos%20gerais.md#Produto) de números [primos](Termos%20gerais.md#Número%20Primo). Sendo esse [produto](Termos%20gerais.md#Produto), único para todo [número composto](Termos%20gerais.md#Número%20Composto), ou seja, dois [números compostos](Termos%20gerais.md#Número%20Composto) distintos não podem gerar o mesmo grupo de números [primos](Termos%20gerais.md#Número%20Primo) como [produto](Termos%20gerais.md#Produto), independente da ordem. 
## Regra prática
Ao realizar a famosa [fatoração](Fatoração%20e%20divisores%20de%20um%20número), não existe uma ordem crescente ou decrescente a ser seguida:
![[Pasted image 20250225140726.png]]
## Quantidade de divisores de um número inteiro positivo
Podemos descobrir a quantidade de divisores de um número inteiro aplicando a regra prática acima, por exemplo:
Quantos divisores naturai possui o número 20?
![[Pasted image 20250225142449.png]]
Sendo $nd$ a quantidade de divisores para um número inteiro positivo, os termos da [fatoração](Fatoração%20e%20divisores%20de%20um%20número) de um [número composto](Termos%20gerais.md#Número%20Composto) podem ser interpretados como:
$$
a^n . b ^ m ... z ^ y \implies (n + 1) . (m + 1) ... (y + 1) = \text{nd}
$$
![[Pasted image 20250225143009.png]]
## Encontrando os divisores de um número inteiro positivo
Após realizar a [fatoração](Fatoração%20e%20divisores%20de%20um%20número) do número em questão, os seguintes passos:
1. traçamos outra reta ao lato dos termos da [fatoração](Fatoração%20e%20divisores%20de%20um%20número) e iniciamos com o número 1, o divisor universal.
2. multiplicamos o 1 pelo primeiro fator da [fatoração](Fatoração%20e%20divisores%20de%20um%20número).
3. depois multiplicamos o 1 e o novo número pelo segundo fator, e assim por diante.
4. os divisores encontrados são colocados ao lado do fator de origem, separados por uma virgula.
5. divisores encontrados que já estiverem presentes, não devem ser adicionados novamente.
![[Pasted image 20250225143814.png]]