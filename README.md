# GEDI - Automação de Envio de Faturas

Projeto que automatiza o processo de envio de faturas, reduzindo o tempo de 8 horas para 15 minutos.

* Resultados

| Métrica | Antes | Depois |
|---------|-------|--------|
| Tempo de processamento | 8 horas | 15 minutos |
| Erros manuais | ~5% | 0% |
| Capacidade diária | 50 faturas | 500+ faturas |

* O que faz

• Consulta faturas no banco de dados
• Valida dados automáticamente  
• Carimba PDFs com data/hora
• Envia via API GEDI
• Gera relatórios de sucesso/falha

* Tecnologias Usadas

- Python 3.10+
- Pandas (validação de dados)
- ReportLab (carimbo de PDFs)
- Requests (integração com API)
- SQLite (banco de dados)

* Instalação

```bash
# Clone o repositório
git clone https://github.com/IsabelleJelic/gedi-automacao.git
cd gedi-automacao

# Instale as dependências
pip install -r requirements.txt
```

* Como Usar

```python
# Execute o script principal
python src/main.py
```

Ou em Python:

```python
from src.validacoes import validar_faturas
from src.envio_gedi import enviar_gedi

# Valida as faturas
resultados = validar_faturas("./faturas")

# Envia para GEDI
enviar_gedi(resultados)
```

* Estrutura do Projeto

gedi-automacao/
├── src/ # Scripts principais
│ ├── main.py # Orquestrador
│ ├── validacoes.py # Validação de dados
│ ├── envio_gedi.py # Envio via API
│ ├── carimbar_pdfs.py # Carimbo de PDFs
│ └── banco.py # Conexão com BD
├── docs/ # Documentação
├── requirements.txt # Dependências
└── README.md # Este arquivo

* Contato

- * * LinkedIn:* *  [https://www.linkedin.com/in/isabelle-jelic-1439841b9/]
- * * Email:* *  isabellevic.jelic@gmail.com

---

* * Desenvolvido por Isabelle Jelic* * 
