import sqlite3
import pandas as pd

alunos = pd.read_excel('test-interview.xlsx', sheet_name='Alunos')
cursos = pd.read_excel('test-interview.xlsx', sheet_name='Cursos')
conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

alunos.to_sql('alunos', conn, if_exists='replace', index=False)
cursos.to_sql('cursos', conn, if_exists='replace', index=False)

id_aluno = input("Digite o ID do aluno: ")

query = f"""SELECT cursos.nome_curso, cursos.id_curso, alunos.nome FROM cursos INNER JOIN alunos ON alunos.id_aluno = cursos.id_aluno WHERE alunos.id_aluno = '{id_aluno}'"""

cursor.execute(query)
resultados = cursor.fetchall()

index = 1

nome_aluno = '' 
for resultado in resultados:
    nome_aluno = resultado[2]

print(f"O(A) aluno(a) {nome_aluno} está matriculado(a) no(s) seguinte(s) curso(s): ")
for resultado in resultados:
    print(f"{index}. {resultado[0]} - ID Curso: {resultado[1]}")
    index+= 1
