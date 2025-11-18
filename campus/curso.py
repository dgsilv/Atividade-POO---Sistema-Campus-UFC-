class Curso:
    def __init__(self, id_curso: int, nome: str, carga_horaria: int):
        self.id = id_curso
        self.nome = nome
        self.carga_horaria = carga_horaria

    def atualizar(self, novo_nome: str, nova_carga: int):
        self.nome = novo_nome
        self.carga_horaria = nova_carga

    def __str__(self):
        return f"[ID {self.id}] {self.nome} - {self.carga_horaria}h"
