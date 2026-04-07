from models import Disciplina


class DisciplinaRepository:
    def __init__(self):
        self.disciplinas = []
        self.proximo_id = 1

    def resetar(self):
        self.disciplinas = []
        self.proximo_id = 1

    def listar_todas(self):
        return self.disciplinas

    def buscar_por_id(self, disciplina_id):
        for disciplina in self.disciplinas:
            if disciplina.id == disciplina_id:
                return disciplina
        return None

    def criar(self, titulo, data_inicio, data_termino, numero_vagas, eh_verao):
        disciplina = Disciplina(
            id=self.proximo_id,
            titulo=titulo,
            data_inicio=data_inicio,
            data_termino=data_termino,
            numero_vagas=numero_vagas,
            eh_verao=eh_verao
        )
        self.disciplinas.append(disciplina)
        self.proximo_id += 1
        return disciplina

    def atualizar(self, disciplina_id, dados):
        disciplina = self.buscar_por_id(disciplina_id)
        if not disciplina:
            return None

        disciplina.titulo = dados["titulo"]
        disciplina.data_inicio = dados["data_inicio"]
        disciplina.data_termino = dados["data_termino"]
        disciplina.numero_vagas = dados["numero_vagas"]
        disciplina.eh_verao = dados["eh_verao"]
        return disciplina

    def remover(self, disciplina_id):
        disciplina = self.buscar_por_id(disciplina_id)
        if not disciplina:
            return False

        self.disciplinas.remove(disciplina)
        return True