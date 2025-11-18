from .curso import Curso

class Campus:
    _id_curso_global = 1  

    def __init__(self, nome: str):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, nome: str, carga_horaria: int):
        curso = Curso(Campus._id_curso_global, nome, carga_horaria)
        Campus._id_curso_global += 1
        self.cursos.append(curso)
        print(f"Curso criado: {curso}")

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado neste campus.")
        else:
            print(f"\nCursos do Campus {self.nome}:")
            for curso in self.cursos:
                print(curso)

    def procurar_curso(self, id_curso: int):
        return next((c for c in self.cursos if c.id == id_curso), None)

    def atualizar_curso(self, id_curso: int, novo_nome: str, nova_carga: int):
        curso = self.procurar_curso(id_curso)
        if curso:
            curso.atualizar(novo_nome, nova_carga)
            print("Curso atualizado com sucesso!")
        else:
            print("Curso não encontrado.")

    def remover_curso(self, id_curso: int):
        curso = self.procurar_curso(id_curso)
        if curso:
            self.cursos.remove(curso)
            print("Curso removido com sucesso!")
        else:
            print("Curso não encontrado.")

    def __str__(self):
        return f"Campus: {self.nome} | Total de cursos: {len(self.cursos)}"
