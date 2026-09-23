# GEDI - Automação de Envio de Faturas

Automação completa do processo de envio de faturas, reduzindo o tempo de processamento de **8 horas para 15 minutos.**

## 📊 Resultados

| Métrica | Antes | Depois |
|---------|-------|--------|
| **Tempo de processamento** | 8 horas | 15 minutos |
| **Taxa de erros** | ~5% | 0% |
| **Faturas/dia** | 50 | 500+ |

## 🔧 O que faz

- ✅ Consulta faturas no banco de dados
- ✅ Valida dados automaticamente
- ✅ Carimba PDFs com data/hora
- ✅ Envia via API GEDI
- ✅ Gera relatórios de sucesso/falha

## 📦 Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas** – validação de dados
- **ReportLab** – carimbo de PDFs
- **Requests** – integração com API
- **SQLite** – banco de dados

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/IsabelleJelic/gedi-automacao.git
cd gedi-automacao

# Instale as dependências
pip install -r requirements.txt
```

## 💻 Como Usar

### Via linha de comando:

```bash
python src/main.py
```

### Via Python:

```python
from src.validacoes import validar_faturas
from src.envio_gedi import enviar_gedi

# Valida as faturas
resultados = validar_faturas("./faturas")

# Envia para GEDI
enviar_gedi(resultados)
```

## 📂 Estrutura do Projeto

```
gedi-automacao/
├── src/                    # Scripts principais
│   ├── main.py            # Orquestrador
│   ├── validacoes.py      # Validação de dados
│   ├── envio_gedi.py      # Envio via API
│   ├── carimbar_pdfs.py   # Carimbo de PDFs
│   └── banco.py           # Conexão com BD
├── docs/                  # Documentação
├── requirements.txt       # Dependências
└── README.md             # Este arquivo
```

## 📧 Contato

- **LinkedIn:** [Isabelle Jelic](https://www.linkedin.com/in/isabelle-jelic-1439841b9/)
- **E-mail:** isabellevic.jelic@gmail.com

---

**Desenvolvido por Isabelle Jelic**
