# ⚙️ Setup — Configuração Rápida

Guia para instalar e configurar a automação GEDI em sua máquina.

---

## 📋 Pré-requisitos

- **Python 3.10+** instalado (`python --version`)
- **pip** (gerenciador de pacotes)
- Acesso ao banco **MySQL** (tim_producao)
- Credenciais da **API GEDI** (token, endpoint)

---

## 🚀 1. Instalação

### Clone o repositório

```bash
git clone https://github.com/IsabelleJelic/gedi-automacao.git
cd gedi-automacao
```

### Crie ambiente virtual (recomendado)

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Instale dependências

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- sqlalchemy
- pandas
- pymysql
- requests
- python-dotenv
- PyMuPDF (fitz)
- python-dateutil

---

## 🔐 2. Configuração (.env)

### 2.1 Crie arquivo `.env`

Na raiz do projeto:

```bash
cp .env.example .env
```

### 2.2 Preencha as variáveis

Edite `.env` com suas credenciais:

```env
# ===== BANCO DE DADOS =====
DB_HOST=seu-host-mysql
DB_PORT=3306
DB_NAME=tim_producao
DB_USER=seu-usuario
DB_PASSWORD=sua-senha-segura

# ===== USUÁRIO =====
COD_USUARIO=seu-codigo

# ===== API GEDI =====
URL_EMAIL=https://api.gedi.com/send-email
EMAIL_API_TOKEN=seu-token-api

# ===== E-MAILS =====
GEDI_EMAIL=gedi@email.com.br
BCC=seu-email@empresa.com,outro@empresa.com

# ===== CAMINHOS =====
PATH_RELATORIO=./output/relatorios
```

### ⚠️ Segurança

- **Nunca commite `.env`** (já está em `.gitignore`)
- Use `.env.example` como template (sem senhas)
- Se senha tem caracteres especiais, use aspas:
  ```env
  DB_PASSWORD="p@ss#word"
  ```

---

## ✅ 3. Verificação

### Teste a conexão com banco

```bash
python -c "
from src.banco import conectar
try:
    engine = conectar()
    print('✅ Conexão com banco OK!')
except Exception as e:
    print(f'❌ Erro: {e}')
"
```

### Teste carregamento de config

```bash
python -c "
from src.config import GEDI_EMAIL, DB_HOST
print(f'✅ GEDI_EMAIL: {GEDI_EMAIL}')
print(f'✅ DB_HOST: {DB_HOST}')
"
```

---

## 🎯 4. Primeiro Run

### Modo Interativo

```bash
python src/main.py
```

**Você será perguntado:**
```
Modo (normal/backlog): normal
```

**Fluxo esperado:**
1. Busca faturas no período
2. Valida dados
3. Gera CSVs
4. Carimbba PDFs
5. Log em `logs/automacao.log`

### Saída

```
Período: 2026-08-23 até 2026-09-23

Buscando faturas...
[Total de registros: 123]

Validando...

Resumo dos erros:
Sem PO: 5
Sem Boleto: 2

[118 prontas para envio]
[5 para validação]

Carimbando PDFs...

Processo concluído.
```

---

## 📂 5. Estrutura de Saída

Após execução, verifique:

```
output/
├── relatorios/
│   ├── pronto_envio.csv        # Faturas OK
│   └── validacao_gestao.csv    # Faturas com erro
├── pdfs/
│   ├── originais/              # PDFs baixados
│   └── carimbados/             # PDFs com carimbo
└── pendentes_envio/            # [Futuro]

logs/
└── automacao.log               # Histórico
```

### Verifique CSVs

```bash
# Faturas prontas
head -5 output/relatorios/pronto_envio.csv

# Faturas com erro
head -5 output/relatorios/validacao_gestao.csv
```

---

## 📌 6. Notas Importantes

### Modo Normal vs Backlog

| Modo | Período | Uso |
|------|---------|-----|
| **normal** | Mês atual + mês anterior | Execução diária |
| **backlog** | 6 meses atrás (sem overlap) | Processamento histórico |

**Exemplo (hoje = 23/09/2026):**
- Normal: 23/08/2026 a 23/09/2026
- Backlog: 23/02/2026 a 23/08/2026

### Validações Aplicadas

```python
# Em validacoes.py, valida:
- PO (não vazio)
- NF (não vazio)
- Valor (não zero)
- Boleto (não vazio)
```

### Carimbo PDF

```python
# Em carimbar_pdfs.py:
# - Insere PO, CNPJ, SGE TIM
# - Usa lista_posicoes_carimbo() para encontrar posição
# - Salva em output/pdfs/carimbados/
```

---

## 🔄 7. Agendamento (Opcional)

### Linux/Mac (Cron)

```bash
# Abra crontab
crontab -e

# Adicione (executa 8AM todos os dias):
0 8 * * * cd /caminho/gedi-automacao && python src/main.py normal >> logs/cron.log 2>&1
```

### Windows (Task Scheduler)

1. Abra **Task Scheduler**
2. **Create Basic Task**
3. **Trigger**: Daily, 08:00 AM
4. **Action**:
   - Program: `C:\Python310\python.exe`
   - Arguments: `C:\caminho\gedi-automacao\src\main.py`
   - Start in: `C:\caminho\gedi-automacao`

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"

```bash
pip install -r requirements.txt
```

### "Connection refused" (banco)

Verifique em `.env`:
- `DB_HOST` está correto?
- `DB_PORT` é 3306?
- Firewall libera conexão?

Teste conexão manualmente:
```bash
mysql -h DB_HOST -u DB_USER -p tim_producao -e "SELECT 1"
```

### CSV não foram gerados

Verifique se:
- `output/relatorios/` existe?
- `PATH_RELATORIO` está correto em `.env`?
- Tem espaço em disco?

Veja mais em [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## ✨ Próximos Passos

1. **Leia** [TECNICA.md](TECNICA.md) para entender o código
2. **Teste** com dados reais em pequeno volume
3. **Configure** agendamento (cron/scheduler)
4. **Monitore** logs em `logs/automacao.log`

---

**Pronto! Você está configurado.** 🚀

Dúvidas? Veja [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
