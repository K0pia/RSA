
from numeroPrimo import GeradorNumeroPrimo
from gerarChaves import Chaves
from criptografia import Criptografia

p = int(input("Digite o P: "))

q = int(input("Digite o Q: "))

chaves = Chaves(p, q)
chaves.gerar_chaves()

encripta = chaves.encripta_mensagem()
chaves.decripta_mensagem(encripta)