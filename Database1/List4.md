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

8. **Consultas** (Respostas abaixo)

9. **Consultas** (Respostas abaixo)

10. **Consultas** (Respostas abaixo)

11. **Consultas** (Respostas abaixo)

12. **Consultas** (Respostas abaixo)

13. **Consultas** (Respostas abaixo)

14. **Consultas** (Respostas abaixo)

15. **Consultas** (Respostas abaixo)

16. **Consultas** (Respostas abaixo)

17. **Consultas** (Respostas abaixo)

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

21. **Consultas** (Respostas abaixo)

22. **Consultas** (Respostas abaixo)

23. **Consultas** (Respostas abaixo)

24. **Consultas** (Respostas abaixo)

---

**Respostas:**

**BANCO 01: Loja de Roupas**

8. [Sua resposta aqui]
9. [Sua resposta aqui]
10. [Sua resposta aqui]
11. [Sua resposta aqui]
12. [Sua resposta aqui]
13. [Sua resposta aqui]
14. [Sua resposta aqui]
15. [Sua resposta aqui]
16. [Sua resposta aqui]
17. [Sua resposta aqui]

**BANCO 02: ESCOLA**

21. [Sua resposta aqui]
22. [Sua resposta aqui]
23. [Sua resposta aqui]
24. [Sua resposta aqui]