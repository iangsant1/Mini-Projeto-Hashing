class TabelaHashing:
    def __init__(self, capacidade_inicial: int = 12, fator_carga: float = 0.66):
        self.capacidade = self.capacidade_inicial
        self.fator_carga = fator_carga
        self.tamanho = 0
        self.tablea = [None] * self.capacidade

        self._DELETED = object()

    def _hash(self, chave) -> int:
        return hash(chave)%self.capacidade

    def _fator_carga(self) -> float:
        return self.tamanho/self.capacidade

    def _inserir(self)



    