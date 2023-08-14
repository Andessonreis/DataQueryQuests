## Notas da Aula - 11/08

Nesta aula, aprendemos a manipular dados do EMAC (Educação e Matrícula do Ensino Superior) das instituições de ensino. O foco foi na transformação e limpeza dos dados, incluindo a conversão de tipos de dados para melhor análise. Abaixo está o código discutido durante a aula:

```sql
-- Remover a tabela cursos (caso já exista)
DROP TABLE IF EXISTS cursos;

-- Criar a tabela cursos
CREATE TABLE IF NOT EXISTS cursos (
    instituicao VARCHAR(255),
    sigla VARCHAR(70),
    cat_adiministrativa VARCHAR(50),
    cod_curso INTEGER,
    nome_curso VARCHAR(100),
    modalidade VARCHAR(30),
    cc VARCHAR(50),
    ini_funcionamento VARCHAR(30),
    data_criacao VARCHAR(30),
    situacao VARCHAR(30)
);

-- Converter a coluna data_criacao para o tipo DATE
ALTER TABLE cursos
ALTER COLUMN data_criacao TYPE DATE USING data_criacao::DATE;

-- Selecionar todos os registros da tabela cursos
SELECT * FROM cursos;

-- Remover registros com data_criacao igual a '-'
DELETE FROM cursos WHERE data_criacao = '-';
```

O código acima realiza as seguintes tarefas:

1. Cria a tabela "cursos" para armazenar informações sobre cursos nas instituições de ensino.
2. Converte o tipo de dado da coluna "data_criacao" de VARCHAR para DATE, eliminando o valor '-'.
3. Seleciona todos os registros da tabela cursos, possibilitando a análise dos dados.
4. Remove registros com data de criação igual a '-' para limpar os dados.

Lembre-se de que o conjunto de dados utilizado neste exemplo está no diretório "dataset" com o nome do arquivo "cursos.xls.csv". Certifique-se de que o arquivo esteja acessível no caminho correto para que o código funcione corretamente.
