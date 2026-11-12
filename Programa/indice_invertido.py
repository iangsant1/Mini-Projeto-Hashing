import re
from collections import defaultdict


def padronizar_palavras(palavra: str) -> str:
    return re.sub(r'[^\w\s]', '', palavra).lower() #Remove a pontuação e deixa minúscula, para padronizar


def construir_indice(texto: str) -> dict:
    indice = defaultdict(set)

    for i, linha in enumerate(texto.splitlines(), start=1):
       palavras = padronizar_palavras(linha).split()  #As palavras são divididas e separadas 
       for palavra in palavras:
           if palavra:              #Identificando se há strings vazias
               indice[palavra].add(i)

    return dict(indice)
           

def buscar(indice: dict, palavra: str ) -> set:
    palavra_padr = padronizar_palavras(palavra)
    return indice.get(palavra_padr, set())
    

def buscar_e(indice, palavras):
    if not palavras: #Verificando se há strings vazias, caso não retorna um conjunto vazio
        return set()

    resultados = None
    for palavra in palavras:
        linhas = buscar(indice, palavra)
        if resultados is None:
            resultados = set(linhas)
        else: 
            resultados.intersection_update(linhas) #Uso da intersecção 
        if not resultados: #Em caso que a intersecção fique vazia, irá parar
            break

    return resultados or set()

def buscar_ou(indice, palavras):  
    resultados = set()
    for palavra in palavras:
        resultados.update(buscar(indice, palavra))
    return resultados 