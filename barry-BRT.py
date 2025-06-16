#Não mexa aqui.
import random
import time
MINIMO = 1
MAXIMO = 9_223_372_036_854_775_807
random.seed(42)  # Para garantir a reprodutibilidade dos testes

#SEU TRABALHO COMEÇA DAQUI PRA FRENTE
#VOCÊ PODE MODIFICAR A CLASSE NOH E CRIAR
#FUNÇÕES ADICIONAIS 

#Quando você estiver submetendo no RunCodes, mude para True
ESTOU_SUBMETENDO_NO_RUNCODES = True

class noh:
  def __init__(self, dado):
    self.dado = dado
    self.esq = None
    self.dir = None
    self.cor = True

def rotacionaEsquerda(y):
  x = y.dir
  y.dir = x.esq
  x.esq = y
  x.cor = y.cor
  y.cor = True
  return x

def rotacionaDireita(y):
  x = y.esq
  y.esq = x.dir
  x.dir = y
  x.cor = y.cor
  y.cor = True
  return x

def sobeVermelho(y):
  y.cor = True
  y.esq.cor = False
  y.dir.cor = False   

def verificaVermelho(y):
  if y is None:
    return False
  return y.cor

def verificaPreto(y):
  return not verificaVermelho(y)

def _insere_recursivo(raiz, dado):
  #VOCÊ DEVE FAZER ESSA FUNÇÃO
  ##recebe uma arvore e devolve o endereço da nova arvore com o dado adicionado
  if raiz is None:
    return noh(dado)
  elif dado < raiz.dado:
    raiz.esq = _insere_recursivo(raiz.esq, dado)
  elif dado > raiz.dado:
    raiz.dir = _insere_recursivo(raiz.dir, dado)
  else:
    return raiz
  
  if verificaVermelho(raiz.dir) and verificaPreto(raiz.esq):
    raiz = rotacionaEsquerda(raiz)
  if verificaVermelho(raiz.esq) and verificaVermelho(raiz.esq.esq):
    raiz = rotacionaDireita(raiz)
  if verificaVermelho(raiz.dir) and verificaVermelho(raiz.esq):
    sobeVermelho(raiz)
  return raiz 

def insere(raiz, dado):
  raiz = _insere_recursivo(raiz, dado)
  raiz.cor = False
  return raiz
  
  
  
def em_ordem(no):
  #VOCÊ DEVE FAZER ESSA FUNÇÃO
  ##Imprime os dados da árvore em ordem crescente
  if no is None:
    return 
  em_ordem(no.esq)
  print(no.dado)
  em_ordem(no.dir)


def _encontra_mais_proximo_recursivo(no, x, mais_proximo):
  if no is None:
    return mais_proximo

  if no.dado == x:
    return no.dado
  
  if abs(no.dado - x) < abs(mais_proximo - x):
    mais_proximo = no.dado

  if x < no.dado:
    return _encontra_mais_proximo_recursivo(no.esq, x, mais_proximo)
  else:
    return _encontra_mais_proximo_recursivo(no.dir, x, mais_proximo)

def encontra_mais_proximo(no, x):
  #VOCÊ DEVE FAZER ESSA FUNÇÃO
  ##Encontra o valor mais próximo de x na árvore
  mais_proximo = _encontra_mais_proximo_recursivo(no, x, no.dado)
  return mais_proximo




## A PARTIR DAQUI NÃO MUDE NADA.
## PARTES DESTE CÓDIGO ESTÃO PROPOSITALMENTE
## INEFICIENTES PARA DEIXAR O PROBLEMA MAIS DIFÍCIL.

##Não mexa aqui.
def inicializa_arvore(n):
  numeros = random.sample(range(MINIMO, MAXIMO), n)
  #Essa linha de baixo é só para deixar o problema
  #mais difícil. Deixe assim.
  numeros.sort()
  raiz = None
  for num in numeros:
    raiz = insere(raiz, num)
  return raiz

def insere_novos_numeros(arvore, n):
  numeros = random.sample(range(MINIMO, MAXIMO), n)
  for num in numeros:
    arvore = insere(arvore, num)
  return arvore


nivel = int(input("Digite o nivel do jogo 1-fácil, 2-normal, 3-difícil, 4-insano: "))
if nivel == 1:
  MAXIMO = 100
  n = 5
elif nivel == 2:
  MAXIMO = 1000
  n = 100
elif nivel == 3:
  n = 5
else:
  n = 50000

arvore = inicializa_arvore(n)
print("\nNúmeros inseridos no jogo:")
if not ESTOU_SUBMETENDO_NO_RUNCODES:
  em_ordem(arvore)
x = random.randint(MINIMO, MAXIMO)
print(f"\n\nQual o valor mais próximo de {x} digite -1 para sair:")

inicio = time.time()
chute = int(input(""))
print()
while chute >= 0:
  #Não é eficiente ficar encontrando o mais próximo
  #toda vez, mas está assim para deixar o problema mais difícil.
  #Deixe assim.
  mais_proximo = encontra_mais_proximo(arvore, x)
  if chute == mais_proximo:
    fim = time.time()
    tempo = fim - inicio
    print(f"Parabéns! Você acertou! O número mais próximo de {x} é {mais_proximo}.")
    if not ESTOU_SUBMETENDO_NO_RUNCODES:
      print(f"Você levou {tempo:.2f} segundos.")
    arvore = insere_novos_numeros(arvore, 3)
    
    if not ESTOU_SUBMETENDO_NO_RUNCODES:
      print("\n**************************")
      print("Números inseridos no jogo:")
      em_ordem(arvore)
    x = random.randint(MINIMO, MAXIMO)
    print(f"\n\nQual o valor mais próximo de {x}:")
    inicio = time.time()
    chute = int(input(""))
  else:
    chute = int(input(f"\nErrou! {chute} não é a resposta!\nTente novamente: "))

print("Saindo!")