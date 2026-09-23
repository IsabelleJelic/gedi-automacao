# 🐛 Troubleshooting — Problemas Comuns

Soluções para erros frequentes no projeto GEDI.

---

## 🔍 Como Debugar

### 1. Verifique o log

```bash
# Último arquivo
tail -f logs/automacao.log

# Últimas 50 linhas
tail -50 logs/automacao.log

# Busque por erros
grep ERROR logs/automacao.log
```

### 2. Rode com debug

```bash
# Adicione print() no seu código
python src/main.py  # Rode e veja output
```

### 3. Teste módulos isoladamente

```bash
# Teste banco
python -c "from src.banco import conectar; print(conectar())"

# Teste consulta
python -c "
from src.consulta_faturas import buscar_faturas
from src.periodo import obter_periodo
inicio, fim = obter_periodo('normal')
df = buscar_faturas(inicio, fim)
print(f'Faturas: {len(df)}')
"

# Teste validação
python -c "
from src.validacoes import validar_faturas
# ... carregue seu dataframe
df_ok, df_erro = validar_faturas(df)
print(f'OK: {len(df_ok)}, Erro: {len(df_erro)}')
"
```

---

## 🗄️ Problemas com Banco de Dados

### ❌ "Connection refused" ou "No route to host"

**Causa**: Não consegue conectar ao MySQL

**Checklist:**
- [ ] `DB_HOST` está correto? (IP ou hostname)
- [ ] `DB_PORT` é 3306?
- [ ] Usuário/senha sem erros?
- [ ] Banco `tim_producao` existe?
- [ ] Firewall libera conexão?

**Teste:**
```bash
# Verifique conectividade
ping seu-host-mysql

# Teste conexão MySQL
mysql -h DB_HOST -u DB_USER -p DB_PASSWORD -e "USE tim_producao; SELECT 1"

# Teste via Python
python -c "from src.banco import conectar; print(conectar())"
```

---

### ❌ "Access denied for user"

**Causa**: Credenciais erradas

**Soluções:**

```bash
# Teste credenciais direto
mysql -h DB_HOST -u DB_USER -p

# Se funcionar, problema está em .env
```

**Se senha tem caracteres especiais:**
```env
# ❌ ERRADO
DB_PASSWORD=p@ss#word

# ✅ CORRETO
DB_PASSWORD="p@ss#word"
```

---

### ❌ "Unknown database 'tim_producao'"

**Causa**: Banco não existe ou nome errado

```sql
-- Verifique bancos
SHOW DATABASES;

-- Se tim_producao não existe, crie ou use nome correto
```

---

### ⚠️ "Too many connections"

**Causa**: SQLAlchemy criando muitas conexões

**Solução:**

```bash
# Reinicie MySQL
sudo systemctl restart mysql

# Ou aumente limite (SQL)
SET GLOBAL max_connections = 200;
```

---

## 📄 Problemas com Dados

### ❌ "KeyError: 'PO'" ou "KeyError: 'NF'"

**Causa**: Colunas não existem no DataFrame

**Verificação:**

```python
from src.consulta_faturas import buscar_faturas
from src.periodo import obter_periodo

inicio, fim = obter_periodo('normal')
df = buscar_faturas(inicio, fim)
print(df.columns.tolist())  # Veja nomes das colunas
print(df.head())            # Veja dados
```

**Se colunas faltam:**
- Query em `consulta_faturas.py` está correta?
- Tabelas do banco existem?
- Usuário tem permissão SELECT?

---

### ❌ "Todas as faturas em erro"

**Causa**: Dados inválidos ou colunas vazias

**Verificação:**

```python
from src.validacoes import validar_faturas

df_ok, df_erro = validar_faturas(df)
print(df_erro[['Unidade', 'Motivo']].head(10))
```

**Motivos comuns:**
- `Sem PO` → Campo NaN ou NULL
- `Sem NF` → Campo vazio
- `Sem Valor` → 0 ou NULL
- `Sem Boleto` → Campo vazio

---

## 📄 Problemas com PDFs

### ❌ "FileNotFoundError" ao carimbar

**Causa**: PDF não existe em `output/pdfs/originais/`

**Checklist:**
- [ ] `download_pdfs.py` foi executado?
- [ ] PDFs foram baixados?
- [ ] Pasta existe?

**Verificação:**
```bash
ls -la output/pdfs/originais/
# Deve ter PDFs lá
```

---

### ❌ "PDF não foi carimbado"

**Causa**: Módulo `lista_posicoes_carimbo` não existe ou retorna None

**Erro típico:**
```
AttributeError: cannot import name 'lista_posicoes_carimbo'
```

**Solução:**

1. Verifique se `lista_posicoes_carimbo.py` existe
2. Se não existe, crie manualmente:

```python
# lista_posicoes_carimbo.py
import fitz

def lista_posicoes_carimbo():
    return {
        "CPFL": [
            {
                "modo": "",
                "pedido": fitz.Point(50, 50),
                "cnpj": fitz.Point(50, 70),
                "sge": fitz.Point(50, 90)
            }
        ],
        "COELBA": [...],
        # ... mais concessionárias
    }
```

3. Ou ajuste `carimbar_pdfs.py` para usar hardcoded:

```python
# Em carimbar_pdfs.py
regra = {
    "pedido": fitz.Point(50, 50),
    "cnpj": fitz.Point(50, 70),
    "sge": fitz.Point(50, 90)
}
# Ao invés de chamar lista_posicoes_carimbo()
```

---

### ⚠️ PDFs não aparecem em `carimbados/`

**Verificação:**
```bash
ls output/pdfs/originais/        # Tem PDFs?
ls output/pdfs/carimbados/       # Saída do carimbo
```

Se `carimbar_pdfs.py` retorna `False`, PDF não foi carimbado (sem regra ou erro).

---

## 📊 Problemas com Validação

### ❌ "AttributeError: 'float' object has no attribute '__getitem__'"

**Causa**: Tipo errado nos dados

**Solução:**

```python
# Em consulta_faturas.py, converta para string
df['Unidade'] = df['Unidade'].astype(str)
df['PO'] = df['PO'].astype(str)
```

---

### ⚠️ "Muitas faturas com 'Sem PO'"

**Causa**: Campo vazio no banco

**Verificação SQL:**
```sql
SELECT Cod_UC, Numero_Pedido FROM Tab_Pedidos_Datas
WHERE Numero_Pedido IS NULL OR Numero_Pedido = '';
```

Se muitos NULLs:
- Verificar se PO foi registrado no banco
- Ou ajustar validação para aceitar NULL

---

## 📁 Problemas com Pastas

### ❌ "FileNotFoundError: [Errno 2] No such file or directory: 'output/...'"

**Causa**: Pastas não foram criadas

**Solução:**

```bash
# Crie manualmente
mkdir -p output/pdfs/{originais,carimbados,SEM_CARIMBO,teste_carimbo}
mkdir -p output/relatorios
mkdir -p output/pendentes_envio
mkdir -p logs
```

Ou deixe que `config.py` crie (roda automaticamente).

---

### ❌ "Permission denied" ao gravar CSV

**Causa**: Sem permissão de escrita

**Solução:**
```bash
chmod 755 output/relatorios
chmod 755 output/pdfs
sudo chown -R seu-usuario:seu-usuario .
```

---

### ❌ "CSV aberto no Excel" — não consegue reescrever

**Solução:** Feche o Excel e rode novamente

```bash
python src/main.py
```

---

## 🔐 Problemas com Variáveis de Ambiente

### ❌ "KeyError" ao carregar .env

**Causa**: Variável não definida em `.env`

**Verificação:**
```bash
cat .env | grep DB_HOST
# Deve retornar valor
```

**Checklist:**
- [ ] `.env` existe na raiz?
- [ ] Variáveis estão preenchidas?
- [ ] Sem espaços extras?

```env
# ❌ ERRADO
DB_HOST = localhost

# ✅ CORRETO
DB_HOST=localhost
```

---

### ⚠️ "Variáveis carregadas incorretamente"

**Solução:**

```python
from src.config import DB_HOST, GEDI_EMAIL
print(f"DB_HOST: {DB_HOST}")
print(f"GEDI_EMAIL: {GEDI_EMAIL}")
# Verifique valores
```

---

## 📋 Checklist Rápido

Se algo falha, rode isto:

```bash
#!/bin/bash
echo "🔍 DIAGNÓSTICO GEDI"

echo "✓ Python?"
python --version

echo "✓ Banco?"
python -c "from src.banco import conectar; conectar()"

echo "✓ Config?"
python -c "from src.config import GEDI_EMAIL; print(GEDI_EMAIL)"

echo "✓ Pastas?"
ls -la output/ logs/

echo "✓ Consulta?"
python -c "
from src.consulta_faturas import buscar_faturas
from src.periodo import obter_periodo
inicio, fim = obter_periodo('normal')
df = buscar_faturas(inicio, fim)
print(f'Faturas: {len(df)}')
"

echo "✓ Validação?"
python -c "
from src.validacoes import validar_faturas
# ... seu dataframe
print('Validação OK')
"

echo "✅ Diagnóstico concluído"
```

---

## 🆘 Ainda com problemas?

1. **Verifique logs** em `logs/automacao.log`
2. **Rode checklist** acima
3. **Consulte** [SETUP.md](SETUP.md)
4. **Abra issue** no GitHub com erro + logs

---

**Última atualização**: Setembro 2026
