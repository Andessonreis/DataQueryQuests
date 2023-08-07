Lista de Exercícios 1 – Modelagem Entidade Relacionamento (Conceitual)
Exercício 01 - Locadora de Veículos

Elabore um modelo ER para uma LOCADORA DE VEÍCULOS com base nos requisitos e especificações abaixo:

a. A entidade CARRO deve possuir: marca, modelo, placa, país de origem, quilometragem, preço por dia;
b. A entidade CLIENTE deve possuir: nome, endereço, cpf, pendência, telefone;
c. MARCA deve ser descrito como uma entidade;
d. Um CLIENTE pode ALUGAR vários CARROS;

Resposta:

Modelo ER:

![Exercicio1](https://github.com/Andessonreis/DataQueryQuests/assets/105820333/d7d667f5-7a33-48ab-8526-37bc72272c51)

Exercício 02 - Biblioteca

Elabore um modelo ER para uma BIBLIOTECA com base nos requisitos e especificações abaixo:

a. A entidade LIVRO deve possuir: isbn, título, idioma, ano de publicação, quantidade, gênero, autor, editora;
b. A entidade AUTOR deve possuir: nome, país de origem;
c. A entidade EDITORA deve possuir: nome, cnpj, endereço;
d. A entidade CLIENTE deve possuir: nome, cpf, endereço, pendência, telefone;
e. GENERO deve ser descrito como uma entidade;
f. Um CLIENTE pode pegar EMPRESTADO vários LIVROS;
g. Um LIVRO pode ter mais de um GENERO;
h. Um LIVRO pode ter mais de um AUTOR;
i. Um LIVRO pode ter mais de uma EDITORA;
j. O empréstimo possui um custo por dia e uma situação (ativo ou inativo), estas informações devem estar representadas no modelo.

Resposta:

Modelo ER:

![Exercicio2](https://github.com/Andessonreis/DataQueryQuests/assets/105820333/28190eff-6fd1-439a-9c0e-f336659a0071)

Exercício 03 - Clínica

Elabore um modelo ER para uma CLINICA com base nos requisitos e especificações abaixo:

a. A entidade MEDICO deve possuir: nome, crm (registro), especialidade;
b. A entidade PACIENTE deve possuir: nome, cpf, endereço, data de nascimento, contato de emergência, telefone;
c. A entidade CONSULTA deve possuir: data, valor, médico e paciente;
d. ESPECIALIDADE deve ser descrita como uma entidade;
e. Um MEDICO pode CONSULTAR vários PACIENTES;
f. Um PACIENTE pode ser CONSULTADO por vários MÉDICOS;
g. Um MEDICO pode ter mais de uma ESPECIALIDADE;
h. A ESPECIALIDADE deve ter um órgão de registro vinculado.

Resposta:

Modelo ER:

![Exercicio3](https://github.com/Andessonreis/DataQueryQuests/assets/105820333/e6eefd32-6310-4aa0-8de8-250078b49426)


Exercício 04 - Escola

Elabore um modelo ER para uma ESCOLA com base nos requisitos e especificações abaixo:

a. A entidade ALUNO deve possuir: nome, cpf, ano, turma;
b. A entidade PROFESSOR deve possuir: nome, cpf, disciplina;
c. DISCIPLINA deve ser uma entidade;
d. TURMA deve ser uma entidade;
e. Um PROFESSOR pode estar em várias TURMAS;
f. Um PROFESSOR pode ministrar várias DISCIPLINAS;
g. Um ALUNO pode estar em apenas uma TURMA;

Resposta:

Modelo ER:
