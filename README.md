# Criptografia do Algoritmo RSA

## O sistema gera números primos grandes até 128 bits, chaves públicas e privada, encripta e decripta com as chaves.

### Funcionamento

O RSA está fortemente ligado à Teoria dos Números, sendo baseado em pilares como as operações de resto e fatoração por números primos. O algoritmo pode ser resumido nos passos descritos abaixo:

*	Obter dois números primos p e q; (Utilizei o teste Miller-Rabin. É um teste probabilístico para saber se  um número n é primo de maneira eficiente).

*	Calcular n = p*q;

*	Calcular phi(n) = (p-1)(q-1); (Função totiente de Euler)

*	Escolher mdc(phi(n), E) == 1, ou seja, E e phi(n) são coprimos (primos relativos);

*	 Calcular D sendo d*e = 1 mod(phi(n)), ou seja, d seja o inverso multiplicativo de E em (mod phi(n)); (Algoritmo de Euclides estendido)

*	Chave pública: (e, n); chave privada: (d, n);

*	Função para cifrar uma mensagem m: m^e = c mod(n);

*	Função para decifrar uma mensagem c: c^d = m mod(n);
