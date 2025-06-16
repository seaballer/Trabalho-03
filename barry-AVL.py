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
    self.altura = 0

def altura(y):
  if y == None:
    return -1
  return y.altura
    
def rotacaoDireita(y):
  x = y.esq
  y.esq = x.dir
  x.dir = y
  
  y.altura = max(altura(y.esq), altura(y.dir)) + 1
  x.altura = max(altura(x.esq), altura(x.dir)) + 1
  
  return x
  
def rotacaoEsquerda(y):
  x = y.dir
  y.dir = x.esq
  x.esq = y
  
  y.altura = max(altura(y.esq), altura(y.dir)) + 1
  x.altura = max(altura(x.esq), altura(x.dir)) + 1
  
  return x
  
#FB = FATOR DE BALANCEAMENTO
# Positivo: esquerda; Negativo: Direita
def fb(y):
  return altura(y.esq) - altura(y.dir)

def insere(raiz, dado):
  #VOCÊ DEVE FAZER ESSA FUNÇÃO
  ##recebe uma arvore e devolve o endereço da nova arvore com o dado adicionado
  if raiz == None:
    return noh(dado)
  
  if dado < raiz.dado:
    raiz.esq = insere(raiz.esq, dado)

    # balanceamento
    if fb(raiz) == 2: # esquerda
      if dado > raiz.esq.dado:
        raiz.esq = rotacaoEsquerda(raiz.esq)  # esquerda-direita
      raiz = rotacaoDireita(raiz) # esquerda-esquerda
  elif dado > raiz.dado:
    raiz.dir = insere(raiz.dir, dado)

    #balanceamento
    if fb(raiz) == -2:  # direita
      if dado < raiz.dir.dado:
        raiz.dir = rotacaoDireita(raiz.dir) # direita-esquerda
      raiz = rotacaoEsquerda(raiz)  # direita-direita
  else:
    return raiz
  
  raiz.altura = max(altura(raiz.dir), altura(raiz.esq)) + 1

  return raiz
  
def em_ordem(no):
  #VOCÊ DEVE FAZER ESSA FUNÇÃO
  ##Imprime os dados da árvore em ordem crescente
  if no == None:
    return

  em_ordem(no.esq)
  print(no.dado, end=" ")
  em_ordem(no.dir)

def encontra_mais_proximo(no, x, mais_proximo=None):
  #VOCÊ DEVE FAZER ESSA FUNÇÃO
  ##Encontra o valor mais próximo de x na árvore

  # Casos base
  if no == None:
    return mais_proximo
  
  if no.dado == x:
    return no.dado
  
  # inicializar mais_proximo / atualizar mais_proximo
  if mais_proximo == None or abs(no.dado - x) < abs(mais_proximo - x):
    mais_proximo = no.dado

  # percorrer árvore
  if x < no.dado:
    return encontra_mais_proximo(no.esq, x, mais_proximo=mais_proximo)
  elif x > no.dado:
    return encontra_mais_proximo(no.dir, x, mais_proximo=mais_proximo)

  
  



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

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
