from indice_invertido import *
from varredura_completa import *

import time
import random


def rodar_testes():
    # Gerando um texto grande para o teste 
    palavras_base = ["python", "codigo", "dados", "busca", "eficiencia", "teste", "algoritmo", "sistema"]
    linhas = [" ".join(random.choices(palavras_base, k=10)) for _ in range(5000)]
    texto_teste = "\n".join(linhas)
    palavras_busca = ["python", "dados"]

    t0 = time.perf_counter()
    indice = construir_indice(texto_teste)
    t1 = time.perf_counter()
    tempo_construcao = t1 - t0
    
    t0 = time.perf_counter()
    for _ in range(1000):
        buscar_e(indice, palavras_busca)
    t1 = time.perf_counter()
    tempo_busca_indice = (t1 - t0) / 1000

    
    t0 = time.perf_counter()
    for _ in range(1000):
        varredura_buscar_e(texto_teste, palavras_busca)
    t1 = time.perf_counter()
    tempo_busca_varredura = (t1 - t0) / 1000


    print(f"RESULTADOS DE DESEMPENHO (5000 linhas, 1000 busca)")
    print(f"Tempo de Construção do Índice: {tempo_construcao:.6f} s")
    print(f"Tempo Médio de Busca (Índice Invertido): {tempo_busca_indice:.8f} s")
    print(f"Tempo Médio de Busca (Varredura Completa): {tempo_busca_varredura:.8f} s")
    print(f"Tempo Construção do Índice + Índice Invertido: {tempo_busca_indice + tempo_construcao:.8f} s")
    print(f"Tempo Construção do Índice + Varredura Completa: {tempo_busca_varredura + tempo_construcao:.8f} s")
    
    if tempo_busca_indice > 0:
        fator = tempo_busca_varredura / tempo_busca_indice
        print(f"O índice invertido foi {fator:.1f}x mais rápido por busca.")
    

if __name__ == "__main__":
    rodar_testes()