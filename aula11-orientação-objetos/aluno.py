# aluno.py
from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = []                # lista de objetos Disciplina
        self.notas_por_disciplina = {}       # dict: nome_da_disciplina -> [notas]

    def matricular(self, disciplina: Disciplina):
        """Adiciona a disciplina ao aluno e prepara a lista de notas desse aluno naquela disciplina."""
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
        # usa o nome da disciplina como chave simples
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        """Adiciona uma nota do aluno **naquela disciplina**."""
        if disciplina.nome not in self.notas_por_disciplina:
            # se não estiver matriculado, matricula automaticamente
            self.matricular(disciplina)
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def media_em(self, disciplina: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(disciplina.nome, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)

    def media_geral(self) -> float:
        medias = []
        for disc in self.disciplinas:
            m = self.media_em(disc)
            if m > 0:
                medias.append(m)
        if not medias:
            return 0.0
        return sum(medias) / len(medias)

    def exibir_boletim(self):
        print(f"\nAluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}")
        if not self.disciplinas:
            print("Sem disciplinas matriculadas.")
            return
        for d in self.disciplinas:
            notas = self.notas_por_disciplina.get(d.nome, [])
            media = self.media_em(d)
            d.exibir_informacoes()
            print(f"  Notas do aluno em {d.nome}: {notas if notas else '—'}")
            print(f"  Média do aluno em {d.nome}: {media:.1f}")
        print(f"MÉDIA GERAL: {self.media_geral():.1f}")
