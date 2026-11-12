from indice_invertido import * 

def varredura_completa_buscar(texto: str, palavra: str) -> set:
    palavra_padr = padronizar_palavras(palavra)
    linhas_encontradas = set()

    for i, linha in enumerate(texto.splitlines(), start=1):
        palavras_linha = [padronizar_palavras(p) for p in linha.split()]
        if palavra_padr in palavras_linha:
            linhas_encontradas.add(i)

    return linhas_encontradas

def varredura_buscar_e(texto: str, palavras: list) -> set:
    if not palavras:
        return set()
    
    palavra_padr = {padronizar_palavras(p) for p in palavras}
    linhas_encontradas = set()

    for i, linha in enumerate(texto.splitlines(), start=1):
        palavras_linha = {padronizar_palavras(p) for p in linha.split()}
        if palavra_padr.issubset(palavras_linha): #Verificando se os elementos de um conjunto estão presentes em outro conjunto
            linhas_encontradas.add(i)

    return linhas_encontradas

def varredura_buscar_ou(texto: str, palavras: list) -> set:
    if not palavras:
        return set()

    palavras_padr = {padronizar_palavras(p) for p in palavras}
    linhas_encontradas = set()

    for i, linha in enumerate(texto.splitlines(), start=1):
        palavras_linha = {padronizar_palavras(p) for p in linha.split()}
        if palavras_padr.intersection(palavras_linha):  #Verificando se há ao menos uma palavra buscada
            linhas_encontradas.add(i)  

    return linhas_encontradas