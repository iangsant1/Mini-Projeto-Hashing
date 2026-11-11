from indice_invertido import *
texto = (
"Python e dados\n"
"Dados e algoritmos\n"
"Python e algoritmos"
)
indice = construir_indice(texto)
# Teste 1: construção do índice
assert indice["python"] == {1, 3}
assert indice["dados"] == {1, 2}
assert indice["algoritmos"] == {2, 3}
# Teste 2: busca simples
assert buscar(indice, "python") == [1, 3]
assert buscar(indice, "java") == []
# Teste 3: consultas combinadas
assert buscar_e(indice, ["python", "dados"]) == [1]
assert buscar_ou(indice, ["python", "dados"]) == [1, 2, 3]