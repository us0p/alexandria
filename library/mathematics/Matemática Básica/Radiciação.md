Sendo $a$ um número real e $n$ um número natural diferente de zero. Dizemos que $\sqrt[n]{a}$ é um número $b$, tal que $b^n = a$.

Da definição, temos que:
- $\sqrt[n]{a^n} = a$ para todo $a \ge 0$.
- $\sqrt[PAR]{x} \implies x \ge 0$
	- Não existe uma solução no conjunto dos números reais que satisfaça uma raiz de [índice](Termos%20gerais.md#Índice%20da%20raiz) par e [radicando](Termos%20gerais.md#Radicando%20da%20raiz) negativo.
	- $\sqrt{-8} \notin \mathbb{R}$
- $\sqrt[ímpar]{x} \implies x \in \mathbb{R}$
	- Um [radicando](Termos%20gerais.md#Radicando%20da%20raiz) negativo implica em um [índice](Termos%20gerais.md#Índice%20da%20raiz) ímpar para uma solução no conjunto dos números reais.
	- $\sqrt[3]{-8} = -2$

A radiciação é a operação inversa da [potenciação](Potenciação.md).
## Módulo
$$
|a| = \begin{cases} a \text{, se } a \ge 0\\ -a \text{, se } a \lt 0\end{cases}
$$
Note que o módulo de um número e ele mesmo se o número for maior ou igual a 0, ou o oposto dele se for menor que 0, portanto:
$$
|10| = |-10| = 10
$$
## Raiz quadrada de um quadrado perfeito:
$$
\sqrt{a^2} = |a|
$$
A raiz quadrada de um número ao quadrado é igual ao [módulo](#Módulo) o [radicando](Termos%20gerais.md#Radicando%20da%20raiz).

Considere a seguinte [equação do segundo grau](Equação%20do%20segundo%20grau.md):
$$
x^2 - 49 = 0 \to x^2 = 49 \to \sqrt{x^2} = \sqrt{49} \to |x| = 7
$$
Note que a resolução apresenta o [módulo](#Módulo) de $x$ igual a $7$.
Pela nossa definição de [módulo](#Módulo):
$$
|7| = |-7| = 7
$$
Portanto o conjunto solução dessa equação contém dois valores: $x \in \lbrace{-7,7\rbrace}$.

> Perceba também que essa definição vale apenas para o caso da equação onde a raiz é incerta e portanto pode assumir um grupo de valores possíveis.
> No caso $\sqrt{49}$ a solução é somente $7$ pois estamos tratando de valor definido.
## Exemplos
![[Pasted image 20250220161608.png]]
## Propriedades
1. $\sqrt[n]{a . b} = \sqrt[n]{a} . \sqrt[n]{b}$
2. $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$
3. $(\sqrt[n]{a})^m = \sqrt[n]{a^m}$
4. $\sqrt[n]{a^m} = \sqrt[n.p]{a^{m.p}}$
5. $\sqrt[m]{\sqrt[n]{a}} = \sqrt[m . n]{a}$
![[Pasted image 20250220163103.png]]