from dataclasses import dataclass, asdict


@dataclass
class Disciplina:
    id: int
    titulo: str
    data_inicio: str
    data_termino: str
    numero_vagas: int
    eh_verao: bool

    def to_dict(self):
        return asdict(self)