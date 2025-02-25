O MDC entre dois ou mais números inteiros é o maior número inteiro que é divisor de tais números.
## Regra prática
O máximo divisor comum entre dois ou mais números inteiros pode ser obtido pelo método da [fatoração](Fatoração%20e%20divisores%20de%20um%20número) simultânea de dois números inteiros.
O MDC é o resultado do produto dos termos da [fatoração](Fatoração%20e%20divisores%20de%20um%20número) que dividiram todos os números envolvidos simultaneamente:
![[Pasted image 20250225153117.png]]
> Note que no MDC é necessário que os [termos](Termos%20gerais.md#Termos) da [fatoração](Fatoração%20e%20divisores%20de%20um%20número) apareçam sempre em ordem crescente e que um novo [termo](Termos%20gerais.md#Termos) só deve ser adicionado quando for impossível continuar a divisão de qualquer fator com o [termo](Termos%20gerais.md#Termos) anterior (o 3 só foi utilizado quando não era mais possível dividir nenhum número por 2).

Caso não exista nenhuma ocorrência de uma divisão simultânea de todos os fatores durante o MDC, então o resultado deve ser 1.
## Propriedades
1. O MDC entre dois ou mais números [primos](Termos%20gerais.md#Número%20Primo) é sempre igual a 1.
2. Se $a$ é divisor de $b$, então $mdc(a,b) = a$.
3. Se os números forem multiplicados/divididos por uma constante $k$, então o MDC entre esses números também será multiplicado/dividido por $k$.