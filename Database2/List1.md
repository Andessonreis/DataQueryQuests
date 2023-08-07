# Exercícios: Lista SQL 1

## Criando tabela "clima":

```sql
CREATE TABLE clima (
	cidade VARCHAR(255),
	temp_min INT,
	temp_max INT,
	precp DECIMAL(5, 2),
	data DATE
);
```

```sql
SELECT * FROM clima;
```

1. **Qual foi a maior temperatura registrada?**

```sql
SELECT MAX(temp_max) AS maior_temperatura FROM clima;
```

2. **Qual foi a menor temperatura registrada?**

```sql
SELECT MIN(temp_min) AS menor_temperatura FROM clima;
```

3. **Quais foram os dias que apresentaram a maior temperatura na cidade de Ilhéus?**

```sql
SELECT data, temp_max
FROM clima
WHERE cidade = 'Ilhéus'
ORDER BY temp_max DESC;
```

4. **Quais foram os dias que apresentaram a menor temperatura na cidade de Irecê?**

```sql
SELECT data, temp_min
FROM clima
WHERE cidade = 'Irecê'
ORDER BY temp_min DESC;
```

5. **Calcule a amplitude térmica:**

```sql
SELECT cidade, data, (temp_max - temp_min) AS amplitude_termica
FROM clima;
```

6. **Quais foram os dias mais quentes de março e que apresentam precipitação acima de 0.7?**

```sql
SELECT data, temp_max, precp
FROM clima
WHERE EXTRACT(MONTH FROM data) = 3 AND precp > 0.7
ORDER BY temp_max DESC;
```

7. **Quais as cidades cujos nomes começam com as letras 'Ir'?**

```sql
SELECT cidade
FROM clima
WHERE LEFT(LOWER(cidade), 2) = 'ir';
```

8. **Calcule o acumulado da precipitação de todas as cidades do mês de janeiro.**

```sql
SELECT SUM(precp) AS acumulado_precipitacao
FROM clima
WHERE EXTRACT(MONTH FROM data) = 1;
```

9. **Quais são as cidades cujo o valor de precipitação acumulado no mês de janeiro foi superior a 16?**

```sql
SELECT cidade, SUM(precp) AS precipitacao_acumulada_janeiro
FROM clima
WHERE EXTRACT(MONTH FROM data) = 1
GROUP BY cidade
HAVING SUM(precp) > 16;
```

10. **Quais são as cidades que começam com a letra 'I' cujo valor de precipitação acumulado do mês de junho foi maior do que 18?**

```sql
SELECT cidade, SUM(precp) AS precipitacao_acumulada_junho
FROM clima
WHERE EXTRACT(MONTH FROM data) = 6
GROUP BY cidade
HAVING LEFT(LOWER(cidade), 1) = 'i' AND SUM(precp) > 18;
```

