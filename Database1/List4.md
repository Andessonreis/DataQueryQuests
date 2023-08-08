**Exercícios de Banco de Dados 2 - Lista 4 (SQL)**

**BANCO 01: Loja de Roupas**

1. **Clientes**
   - Crie a tabela "Clientes" com as colunas:
     - "ID" (inteiro, chave primária, auto incremental)
     - "Nome" (texto)
     - "Email" (texto)
   - Insira 5 Clientes.
   - Insira um novo cliente na tabela "Clientes" com Nome = 'João' e Email = 'joao@example.com'.
   - Atualize o email do cliente adicionado na letra ‘b’ para 'joao@gmail.com'.
   - Exclua o cliente adicionado na letra ‘b’ da tabela "Clientes".
   - Selecione todos os clientes da tabela "Clientes".

**Resposta:**

```sql
CREATE DATABASE IF NOT EXISTS loja_de_roupas;

USE loja_de_roupas;

CREATE TABLE IF NOT EXISTS Clientes (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nome TEXT,
  Email TEXT
);

INSERT INTO Clientes (Nome, Email) VALUES
  ('Cliente 1', 'cliente1@example.com'),
  ('Cliente 2', 'cliente2@example.com'),
  ('Cliente 3', 'cliente3@example.com'),
  ('Cliente 4', 'cliente4@example.com'),
  ('Cliente 5', 'cliente5@example.com');

INSERT INTO Clientes (Nome, Email) VALUES ('João', 'joao@example.com');

UPDATE Clientes SET Email = 'joao@gmail.com' WHERE Nome = 'João';

DELETE FROM Clientes WHERE Nome = 'João';

SELECT * FROM Clientes;
```
---
2. **Categorias**
   - Crie a tabela "Categorias" com as colunas:
     - "id"
     - "nome"
   - Preenchimento:
     ```
     id | nome
     ---|-----
     1  | Casual
     2  | Junino
     3  | Grife
     ```

**Resposta:**

```sql

CREATE TABLE Categorias (
  id INT PRIMARY KEY,
  nome VARCHAR(50)
);

INSERT INTO Categorias (id, nome) VALUES
  (1, 'Casual'),
  (2, 'Junino'),
  (3, 'Grife');
```
---
3. **Produtos**
   - Crie a tabela "Produtos" com as colunas:
     - "ID" (inteiro, chave primária, auto incremental)
     - "CategoriaID" (inteiro, chave estrangeira referenciando a coluna ID da tabela Categorias)
     - "Nome" (texto)
     - "Preco" (decimal)
   - Adicione 5 Produtos.
   - Calcule a média dos preços dos produtos.
   - Obtenha o preço mínimo e máximo dos produtos.
   - Selecione todos os produtos, exibindo o nome e o preço, substituindo valores nulos por 0.
   - Selecione o número total de produtos disponíveis.

**Resposta:**

```sql
CREATE TABLE Produtos (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  CategoriaID INT,
  Nome VARCHAR(255),
  Preco DECIMAL(10,2)
);

INSERT INTO Produtos (CategoriaID, Nome, Preco)
VALUES
  (1, 'Camiseta', 29.99),
  (2, 'Calça Jeans', 59.99),
  (1, 'Blusa', 39.99),
  (3, 'Tênis', 79.99),
  (2, 'Jaqueta', 89.99);

SELECT AVG(Preco) AS MediaPrecos FROM Produtos;

SELECT MIN(Preco) AS PrecoMinimo, MAX(Preco) AS PrecoMaximo FROM Produtos;

SELECT Nome, COALESCE(Preco, 0) AS Preco FROM Produtos;

SELECT COUNT(*) AS TotalProdutos FROM Produtos;
```
---
4. **Departamentos**
   - Crie a tabela "Departamentos" com as colunas:
     - "id"
     - "nome"
   - Preenchimento:
     ```
     id | nome
     ---|-----
     1  | Vendas
     2  | Financeiro
     3  | RH
     ```


**Resposta:**

```sql
CREATE TABLE Departamentos (
  id INT PRIMARY KEY,
  nome VARCHAR(255)
);

INSERT INTO Departamentos (id, nome)
VALUES
  (1, 'Vendas'),
  (2, 'Financeiro'),
  (3, 'RH');
```
---
5. **Cargos**
   - Crie a tabela "Cargos" com as colunas:
     - "id"
     - "nome"
   - Preenchimento:
     ```
     id | nome
     ---|-----
     1  | Vendedor
     2  | Gerente
     3  | Gestor de Pessoas
     4  | Contador
     ```

**Resposta:**

```sql
CREATE TABLE Cargos (
  id INT PRIMARY KEY,
  nome VARCHAR(255)
);

INSERT INTO Cargos (id, nome)
VALUES
  (1, 'Vendedor'),
  (2, 'Gerente'),
  (3, 'Gestor de Pessoas'),
  (4, 'Contador');
```
---
6. **Funcionarios**
   - Crie a tabela "Funcionarios" com as colunas:
     - "id"
     - "nome"
     - "idDepto" (chave estrangeira referenciando a coluna id da tabela Departamentos)
     - "idCargo" (chave estrangeira referenciando a coluna id da tabela Cargos)
   - Preenchimento:
     ```
     id | nome  | idDepto | idCargo
     ---|-------|---------|--------
     1  | Maria | 1       | 1
     2  | João  | 1       | 2
     3  | Ana   | 2       | 4
     ```
**Resposta:**

```sql
CREATE TABLE Funcionarios (
  id INT PRIMARY KEY,
  nome VARCHAR(255),
  idDepto INT,
  idCargo INT
);

INSERT INTO Funcionarios (id, nome, idDepto, idCargo)
VALUES
  (1, 'Maria', 1, 1),
  (2, 'João', 1, 2),
  (3, 'Ana', 2, 4);
```
---
7. **Pedidos**
   - Crie a tabela "Pedidos" com as colunas:
     - "ID" (inteiro, chave primária, auto incremental)
     - "ClienteID" (inteiro, chave estrangeira referenciando a coluna ID da tabela Clientes)
     - "ProdutoID" (inteiro, chave estrangeira referenciando a coluna ID da tabela Produtos)
     - "FuncionarioID" (inteiro, chave estrangeira referenciando a coluna ID da tabela Funcionarios)
     - "Quantidade" (inteiro)
   - Adicione 5 Pedidos.
   - Insira um novo pedido na tabela "Pedidos" com ClienteID = 1, Produto = 1, Funcionario=1, Quantidade = 2.
   - Atualize a quantidade do pedido da letra ‘a’ para 3.
   - Exclua o pedido da letra ‘a’ da tabela "Pedidos".
   - Selecione todos os pedidos da tabela "Pedidos" juntamente com as informações do cliente.

**Resposta:**

```sql
CREATE TABLE Pedidos (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  ClienteID INT,
  ProdutoID INT,
  FuncionarioID INT,
  Quantidade INT
);

INSERT INTO Pedidos (ClienteID, ProdutoID, FuncionarioID, Quantidade)
VALUES
  (1, 1, 1, 2),
  (2, 2, 2, 3),
  (1, 3, 1, 1),
  (3, 2, 1, 5),
  (2, 1, 3, 4);

INSERT INTO Pedidos (ClienteID, ProdutoID, FuncionarioID, Quantidade)
VALUES (1, 1, 1, 2);

UPDATE Pedidos
SET Quantidade = 3
WHERE ID = 1;

DELETE FROM Pedidos
WHERE ID = 1;

SELECT Pedidos.*, Clientes.*
FROM Pedidos
JOIN Clientes ON Pedidos.ClienteID = Clientes.ID;
```
---
8. ***Escreva uma consulta para obter o nome do cliente e o total de pedidos feitos
por cada cliente.***

**Resposta:**

```sql
SELECT Clientes.nome AS NomeCliente, COUNT(*) AS TotalPedidos
FROM Pedidos
JOIN Clientes ON Pedidos.ClienteID = Clientes.ID
GROUP BY Clientes.nome;
```
---     
9. ***Escreva uma consulta para obter o nome do produto, a quantidade pedida e o
nome do cliente que fez cada pedido.***

**Resposta:**

```sql
SELECT Produtos.Nome AS NomeProduto, Pedidos.Quantidade, Clientes.Nome AS NomeCliente
FROM Pedidos
JOIN Produtos ON Pedidos.ProdutoID = Produtos.ID
JOIN Clientes ON Pedidos.ClienteID = Clientes.ID;
```
---     
10. ***Escreva uma consulta para obter o nome do funcionário e o nome do
departamento em que ele trabalha.***

**Resposta:**

```sql
SELECT Funcionarios.nome AS NomeFuncionario, Departamentos.nome AS NomeDepartamento
FROM Funcionarios
JOIN Departamentos ON Funcionarios.idDepto = Departamentos.id;
```
---     
11. ***Escreva uma consulta para obter o nome do produto e a quantidade vendida de
cada produto.***

**Resposta:**

```sql
SELECT Produtos.Nome AS NomeProduto, SUM(Pedidos.Quantidade) AS QuantidadeVendida
FROM Pedidos
JOIN Produtos ON Pedidos.ProdutoID = Produtos.ID
GROUP BY Produtos.Nome;
```
---     
12. ***Escreva uma consulta para obter o nome do cliente, o nome do produto e a
quantidade pedida de cada produto pelo cliente.***

**Resposta:**

```sql
SELECT Clientes.nome AS NomeCliente, Produtos.nome AS NomeProduto, Pedidos.Quantidade
FROM Pedidos
JOIN Produtos ON Pedidos.ProdutoID = Produtos.ID
JOIN Clientes ON Pedidos.ClienteID = Clientes.ID;
```
---     
13. ***Escreva uma consulta para obter o nome do funcionário, o nome do
departamento e o cargo do funcionário.***

**Resposta:**

```sql
SELECT Funcionarios.nome AS NomeFuncionario, Departamentos.nome AS NomeDepartamento, Cargos.nome AS NomeCargo
FROM Funcionarios
JOIN Departamentos ON Funcionarios.idDepto = Departamentos.id
JOIN Cargos ON Funcionarios.idCargo = Cargos.id;
```
---     
14. ***Escreva uma consulta para obter o nome do cliente, o nome do produto e o total
gasto pelo cliente em cada produto.***

**Resposta:**

```sql
SELECT Clientes.nome AS NomeCliente, Produtos.nome AS NomeProduto, SUM(Pedidos.Quantidade * Produtos.Preco) AS TotalGasto
FROM Pedidos
JOIN Produtos ON Pedidos.ProdutoID = Produtos.ID
JOIN Clientes ON Pedidos.ClienteID = Clientes.ID
GROUP BY Clientes.nome, Produtos.nome;
```
---     
15. ***Escreva uma consulta para obter o nome do cliente, o nome do produto e a
média da quantidade pedida de cada produto pelo cliente.***

**Resposta:**

```sql
SELECT Clientes.nome AS NomeCliente, Produtos.nome AS NomeProduto, AVG(Pedidos.Quantidade) AS MediaQuantidade
FROM Pedidos
JOIN Produtos ON Pedidos.ProdutoID = Produtos.ID
JOIN Clientes ON Pedidos.ClienteID = Clientes.ID
GROUP BY Clientes.nome, Produtos.nome;
```
---     
16. ***Escreva uma consulta para obter o nome do funcionário, o nome do
departamento e a quantidade de funcionários no departamento.***

**Resposta:**

```sql
SELECT Funcionarios.nome AS NomeFuncionario, Departamentos.nome AS NomeDepartamento, COUNT(*) AS QuantidadeFuncionarios
FROM Funcionarios
JOIN Departamentos ON Funcionarios.idDepto = Departamentos.id
GROUP BY Funcionarios.nome, Departamentos.nome;
```
---     
17. ***Escreva uma consulta para obter o nome do produto, o nome da categoria e o
total de vendas de cada produto.***

**Resposta:**

```sql
SELECT Produtos.nome AS NomeProduto, Categorias.nome AS NomeCategoria, SUM(Pedidos.Quantidade) AS TotalVendas
FROM Produtos
JOIN Categorias ON Produtos.CategoriaID = Categorias.ID
JOIN Pedidos ON Produtos.ID = Pedidos.ProdutoID
GROUP BY Produtos.nome, Categorias.nome;
```
---     


**BANCO 02: ESCOLA**

18. **Alunos**
   - Crie a tabela "Alunos" com as colunas:
     - "id"
     - "nome"
   - Preenchimento:
     ```
     id | nome
     ---|-----
     1  | Maria
     2  | João
     3  | Ana
     ```
**Resposta:**

```sql
CREATE TABLE Alunos (
  id INT PRIMARY KEY,
  nome VARCHAR(100)
);

INSERT INTO Alunos (id, nome) VALUES
(1, 'Maria'),
(2, 'João'),
(3, 'Ana');
```
---     
19. **Disciplinas**
   - Crie a tabela "Disciplinas" com as colunas:
     - "id"
     - "nome"
   - Preenchimento:
     ```
     id | nome
     ---|-----
     1  | História
     2  | Matemática
     3  | Banco de Dados
     ```

**Resposta:**

```sql
CREATE TABLE Disciplinas (
  id INT PRIMARY KEY,
  nome VARCHAR(100)
);

INSERT INTO Disciplinas (id, nome) VALUES
(1, 'História'),
(2, 'Matemática'),
(3, 'Banco de Dados');
```
---
20. **Notas**
   - Crie a tabela "Notas" com as colunas:
     - "id"
     - "idAluno" (chave estrangeira referenciando a coluna id da tabela Al

unos)
     - "idDisciplina" (chave estrangeira referenciando a coluna id da tabela Disciplinas)
     - "nota" (decimal)
   - Preenchimento:
     ```
     id | idAluno | idDisciplina | nota
     ---|---------|--------------|-----
     1  | 1       | 2            | 7.5
     2  | 1       | 1            | 8.6
     3  | 2       | 3            | 8.0
     4  | 2       | 3            | 6.0
     5  | 3       | 3            | 5.0
     6  | 1       | 2            | 8.5
     7  | 3       | 1            | 7.8
     ```

**Resposta:**

```sql
CREATE TABLE Notas (
  id INT PRIMARY KEY,
  idAluno INT,
  idDisciplina INT,
  nota DECIMAL(4,2)
);

INSERT INTO Notas (id, idAluno, idDisciplina, nota) VALUES
(1, 1, 2, 7.5),
(2, 1, 1, 8.6),
(3, 2, 3, 8.0),
(4, 2, 3, 6.0),
(5, 3, 3, 5.0),
(6, 1, 2, 8.5),
(7, 3, 1, 7.8);
```
---
21. ***Escreva uma consulta para obter o nome do aluno e sua nota em cada disciplina.***

**Resposta:**

```sql
SELECT Alunos.nome AS NomeAluno, Disciplinas.nome AS NomeDisciplina, Notas.nota
FROM Alunos
JOIN Notas ON Alunos.id = Notas.idAluno
JOIN Disciplinas ON Notas.idDisciplina = Disciplinas.id;
```
---
22. ***Escreva uma consulta para obter o nome do aluno, o nome da disciplina e a nota
do aluno em cada disciplina.***

**Resposta:**

```sql
SELECT Alunos.nome AS NomeAluno, Disciplinas.nome AS NomeDisciplina, Notas.nota
FROM Alunos
JOIN Notas ON Alunos.id = Notas.idAluno
JOIN Disciplinas ON Notas.idDisciplina = Disciplinas.id;
```
---
23. ***Escreva uma consulta para obter o nome do aluno, o nome da disciplina e a
média das notas do aluno em cada disciplina.***

**Resposta:**

```sql
SELECT Alunos.nome AS NomeAluno, Disciplinas.nome AS NomeDisciplina, AVG(Notas.nota) AS MediaNota
FROM Alunos
JOIN Notas ON Alunos.id = Notas.idAluno
JOIN Disciplinas ON Notas.idDisciplina = Disciplinas.id
GROUP BY Alunos.nome, Disciplinas.nome;
```
---

24. ***Escreva uma consulta para obter o nome do aluno, o nome da disciplina e a
maior nota obtida pelo aluno em cada disciplina.***

**Resposta:**

```sql
SELECT Alunos.nome AS NomeAluno, Disciplinas.nome AS NomeDisciplina, MAX(Notas.nota) AS MaiorNota
FROM Alunos
JOIN Notas ON Alunos.id = Notas.idAluno
JOIN Disciplinas ON Notas.idDisciplina = Disciplinas.id
GROUP BY Alunos.nome, Disciplinas.nome;

```
---