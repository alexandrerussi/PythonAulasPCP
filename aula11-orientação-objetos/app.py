# app.py
from aluno import Aluno
from disciplina import Disciplina

# cria aluno
aluno1 = Aluno("João Silva", "2025001", "Ciência da Computação")

# cria disciplinas
mat = Disciplina("Matemática", "Prof. Carlos")
fis = Disciplina("Física", "Prof. Ana")

# matricula aluno nas disciplinas
aluno1.matricular(mat)
aluno1.matricular(fis)

# adiciona **notas do aluno** em cada disciplina
aluno1.adicionar_nota(mat, 8.0)
aluno1.adicionar_nota(mat, 6.5)
aluno1.adicionar_nota(fis, 9.0)
aluno1.adicionar_nota(fis, 7.5)

# exibe boletim do aluno (com médias por disciplina e média geral)
aluno1.exibir_boletim()


