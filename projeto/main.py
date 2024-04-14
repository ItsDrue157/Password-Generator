#GERADOR DE SENHA
import string as s
import random as r
import time
from itertools import chain
NUMERO_DE_REPETICOES = 12
tamanho_senha = 0
letras_minusculas = s.ascii_lowercase
numeros = "0123456789"
simbolos = "!@#$%^&*()-_+={}[]|;':<>,.?/"
def gerar_historico():
    f = True
    if f == True:
        gerar_senha(12)# Chamando a função com o tamanho da senha desejado
    else:
        f = open("historioco de senha (dev).txt", "x")
        print("arquivo de log criado, reexecute o codigo para criar a senha.")
        exit

def gerar_senha(tamanho_senha):
    todas_letras = list(letras_minusculas + numeros + simbolos)  # Converte em lista
    r.shuffle(todas_letras)
    senha = "".join(map(str, r.sample(todas_letras, tamanho_senha)))
    f= open("historioco de senha (dev).txt","a")
    f.write(senha)
    f.close()
    print(senha)
    
    
    
print("sua senha ficara disponivel por 60 segundos: ")
print("Sua senha é: ")


gerar_historico()

    
        
        
        
     

