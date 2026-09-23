# 📚 Documentação Técnica — Automação GEDI

**Automação do Envio de Faturas ao GEDI**  
_Guia técnico do código-fonte_

---

## 📋 Informações do Projeto


| Informação | Descrição |
|-----------|-----------|
| **Projeto** | Automação GEDI — TIM |
| **Linguagem** | Python 3.10+ |
| **Responsável** | Isabelle Jelic |
| **Execução** | Local (máquina do desenvolvedor) |
| **Banco de Dados** | MySQL (`tim_producao`) |

### Bibliotecas Principais
- `pandas` – manipulação de dados
- `SQLAlchemy` – ORM para banco de dados
- `PyMuPDF` (fitz) – processamento de PDFs
- `numpy` – operações numéricas
- `requests` – chamadas HTTP

---

## 🔄 1. Visão Geral do Fluxo

O pipeline é executado por `main.py` e passa pelas seguintes etapas, **nesta ordem**:

```
1. periodo.py          → Define janela de datas (normal/backlog)
2. consulta_faturas.py → Busca faturas pendentes no banco
3. validacoes.py       → Separa faturas OK de faturas com erro
4. gerar_arquivos.py   → Grava CSV de validação
5. download_pdfs.py    → Baixa PDFs das faturas
6. carimbar_pdfs.py    → Carimbagem (PO, CNPJ, SGE TIM)
7. envio_gedi.py       → Envia via API + grava protocolo
8. pendentes_envio/    → Fila de reprocessamento (falhas)
```

### 🗓️ Agendamento

- **Modo Normal**: sempre executa
- **Modo Backlog**: executa 1x por semana (controlado por `controle_backlog.json`)

---

## 🔐 2. Variáveis de Ambiente (.env)

| Variável | Descrição |
|----------|-----------|
| `DB_HOST` / `DB_PORT` / `DB_NAME` / `DB_USER` / `DB_PASSWORD` | Credenciais MySQL (tim_producao) |
| `COD_USUARIO` | Código do usuário responsável pelos envios |
| `URL_EMAIL` | Endpoint da API de e-mail (GEDI) |
| `EMAIL_API_TOKEN` | Token de autenticação da API |
| `GEDI_EMAIL` | Destinatário (ex: gedi@email.com.br) |
| `BCC` | Lista de e-mails em cópia (separados por vírgula) |
| `PATH_RELATORIO` | Pasta para relatórios adicionais |

> ⚠️ **Segurança**: Senhas e tokens reais não estão neste documento. Consulte `.env` no ambiente de execução.

---

## 📂 3. Estrutura de Diretórios

```
Automacao_GEDI/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── banco.py
│   ├── periodo.py
│   ├── consulta_faturas.py
│   ├── validacoes.py
│   ├── gerar_arquivos.py
│   ├── download_pdfs.py
│   ├── posicionador_carimbo.py
│   ├── carimbar_pdfs.py
│   ├── envio_gedi.py
│   ├── testar_carimbo.py
│   └── teste_envio_gedi.py
├── .env                         # Variáveis de ambiente
├── __pycache__/                 # Bytecode compilado (auto-gerado)
├── logs/
│   └── automacao.log           # Histórico de execuções
├── output/
│   ├── pdfs/
│   │   ├── originais/{CONCESSIONÁRIA}/
│   │   ├── carimbados/{CONCESSIONÁRIA}/
│   │   ├── SEM_CARIMBO/
│   │   ├── teste_carimbo/
│   │   └── teste_envio/{CONCESSIONÁRIA}/
│   ├── pendentes_envio/{data}/
│   └── relatorios/
│       ├── pronto_envio.csv
│       └── validacao_gestao.csv
└── README.md
```

### Detalhamento do `output/pdfs/`

| Pasta | Conteúdo |
|-------|----------|
| `originais/{CONCESSIONÁRIA}/` | PDF original, sem carimbo |
| `carimbados/{CONCESSIONÁRIA}/` | PDF com carimbo (PO, CNPJ, SGE TIM) — pronto para envio |
| `SEM_CARIMBO/` | PDFs onde nenhuma área livre foi encontrada |
| `teste_carimbo/` | (Manual) PDFs para testes de posicionamento |
| `teste_envio/{CONCESSIONÁRIA}/` | (Manual) PDFs para testes de envio |

### Detalhamento do `output/pendentes_envio/`

Cada subpasta `{data}/` contém pares de arquivos:
- `{nome}.pdf` – PDF da fatura
- `{nome}.json` – Metadados para reenvio

**Nota**: O nome da subpasta (ex: `2026-08-01`) é a **data do envio falho**, não o mês de referência da fatura (que fica no JSON). Essas datas podem ser diferentes.

---

## ⚙️ 4. config.py

**Função**: Carrega variáveis de ambiente e centraliza caminhos/constantes.

- Usa `python-dotenv` para ler `.env`
- Expõe credenciais de banco, token API, e-mail de destino, lista BCC, caminhos de saída
- Garante criação de pastas (`RELATORIOS`, `logs`) na primeira execução

### ⚠️ Atenção

`GEDI_EMAIL` deve apontar para o e-mail real em produção. Durante testes, é comum usar um e-mail pessoal — **sempre confirme qual está ativo antes de rodar em volume**.

---

## 🔌 5. banco.py

**Função**: Cria conexão SQLAlchemy com banco MySQL (tim_producao).

```python
from banco import conectar

engine = conectar()  # Retorna sqlalchemy.Engine
```

### Função: `conectar()`

```python
conectar() -> Engine
```

Cria e retorna uma nova engine SQLAlchemy usando as credenciais de `config.py`.

**Detalhes**:
- Monta connection string com `urllib.parse.quote_plus()` (escapa caracteres especiais na senha)
- Driver: `pymysql`

### ⚡ Performance

`enviar_fatura_gedi()` chama `conectar()` **uma vez por fatura**. Em volumes grandes, isso acumula custo de reconexão. **Futuro**: considerar reaproveitar uma única engine entre chamadas.

---

## 📊 6. consulta_faturas.py

**Função**: Consulta faturas pendentes de envio, já filtradas e enriquecidas com PO/CNPJ.

### Função: `buscar_faturas()`

```python
buscar_faturas(data_inicio: date, data_fim: date) -> pd.DataFrame
```

Retorna DataFrame com uma linha por fatura pendente dentro do período.

**Parâmetros**:
| Param | Tipo | Descrição |
|-------|------|-----------|
| `data_inicio` | date | Início do período (inclusive) |
| `data_fim` | date | Fim do período (inclusive) |

**Retorno**: DataFrame com colunas:
- Unidade, Cod_UC, Mês de referência, Concessionária
- Data de Vencimento, Boleto, NF, Data de emissão, Valor
- PO, CNPJ do Pedido, CNPJ, POs_Abertos, Link do PDF

### Query Principal (resumo)

```sql
SELECT ntc.UC AS 'Unidade', f.Cod_UC AS 'Cod_UC', ...
FROM Faturas_Registradas_Cache f
INNER JOIN Nova_Tab_UC ntc 
  ON ntc.Cod_UC = f.Cod_UC AND ntc.Cod_Empresa = f.Cod_Empresa
INNER JOIN tab_tracking_copy t 
  ON t.Cod_UC = f.Cod_UC AND t.Mes_Ref = f.Mes_Ref AND f.Cod_Empresa = 2
LEFT JOIN Tab_Pedidos_Datas p ON p.Cod_UC = f.Cod_UC ...
LEFT JOIN Tab_PO_CNPJ tpc ON tpc.Numero_Pedido = p.Numero_Pedido
WHERE t.Mes_Ref BETWEEN %(data_inicio)s AND %(data_fim)s
  AND f.Status_Fatura <> 'Simulada'
  AND NULLIF(t.id_arquivo, '') IS NULL
GROUP BY f.Cod_UC, f.Mes_Ref
ORDER BY f.Dt_Venc_NF
```

### 📌 Regras de Negócio

- O JOIN com `tab_tracking_copy` já restringe escopo a **Pagamento Manual (PM)** — sem filtro adicional necessário
- `NULLIF(t.id_arquivo, '') IS NULL` garante apenas faturas ainda não vinculadas a arquivo de envio

---

## 📅 7. periodo.py

**Função**: Calcula intervalo de datas (Mes_Ref) para cada modo de execução.

### Função: `obter_periodo()`

```python
obter_periodo(modo: str) -> tuple[date, date]
```

**Parâmetros**:
| Param | Tipo | Descrição |
|-------|------|-----------|
| `modo` | str | `'normal'` ou `'backlog'` |

**Retorno**: Tupla `(data_inicio, data_fim)`

### Exemplo

Referência: 01/08/2026

| Modo | Período |
|------|---------|
| **Normal** | 01/07/2026 a 01/08/2026 (julho + agosto) |
| **Backlog** | 01/01/2026 a 01/06/2026 (6 meses fechados, sem sobreposição) |

---

## ✅ 8. validacoes.py

**Função**: Separa faturas entre "prontas para envio" e "com pendência", registrando motivos.

### Função: `validar_faturas()`

```python
validar_faturas(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]
```

Aplica regras linha a linha, retorna `(df_ok, df_erro)`.

**Parâmetros**:
| Param | Tipo | Descrição |
|-------|------|-----------|
| `df` | DataFrame | Resultado de `buscar_faturas()` com coluna `Modo` |

**Retorno**: Tupla `(df_ok, df_erro)`
- `df_erro` ganha colunas extras: `Status` e `Motivo`

### Regras Aplicadas

| Verificação | Motivo Registrado | Condição de Falha |
|-------------|-------------------|--------------------|
| **PO** | Sem PO | Vazio, NaN, ou: NAN, NONE, N/A, NA |
| **CNPJ do Pedido** | Sem CNPJ do Pedido | Mesmas condições |
| **NF** | Sem NF | Vazio ou: SemFaturamento, N/A, NAN |
| **Valor** | Sem Valor | Não converte para float, ou valor = 0 |
| **Boleto** | Sem Código de Barras | Vazio, N_A, N/A, NA, NONE, NAN |
| **Data de emissão** | Sem Data de emissão | Vazio, 0000-00-00, ou textos de nulo |
| **Data de Vencimento** | Sem Data de Vencimento | Vazio, 0000-00-00, ou textos de nulo |

### 📌 Decisão de Negócio

Validações de CNPJ, Data de emissão e Data de Vencimento foram **adicionadas** à especificação original — incluídas porque dados vêm direto do banco e, quando ausentes, exigem verificação manual antes do envio.

---

## 📄 9. gerar_arquivos.py

**Função**: Gera relatórios CSV a partir dos DataFrames validados.

### Função: `gerar_csvs()`

```python
gerar_csvs(df_ok: pd.DataFrame, df_erro: pd.DataFrame) -> None
```

Grava:
- `pronto_envio.csv` – faturas aprovadas
- `validacao_gestao.csv` – faturas com pendência

**Detalhes**:
- Separador: `;`
- Codificação: UTF-8 com BOM (`utf-8-sig`) — garante abertura correta no Excel com acentuação
- Remove versões anteriores antes de gravar (com tratamento amigável se arquivo estiver aberto)

---

## 📥 10. download_pdfs.py

**Função**: Baixa PDF da fatura via HTTP e organiza por concessionária.

### Função: `baixar_pdf()`

```python
baixar_pdf(url_pdf: str, nome_arquivo: str, concessionaria: str) -> Path
```

**Parâmetros**:
| Param | Tipo | Descrição |
|-------|------|-----------|
| `url_pdf` | str | URL pública do PDF |
| `nome_arquivo` | str | Nome base do arquivo (ex: UC) |
| `concessionaria` | str | Nome da concessionária (subpasta) |

**Retorno**: Path do arquivo salvo em `output/pdfs/originais/`

**Estrutura**:
```
output/pdfs/originais/
├── CPFL PAULISTA/
│   ├── UC001.pdf
│   └── UC002.pdf
├── CPFL PIRATININGA/
│   └── UC003.pdf
```

### ⚠️ Risco Conhecido

Se `Concessionaria` vier NULL/vazio do banco, o PDF cai na raiz de `originais/` sem subpasta. **Monitore** — vale tratar como `'SEM_CONCESSIONARIA'` explicitamente.

---

## 🎯 11. posicionador_carimbo.py

**Função**: Analisa página do PDF e encontra melhor posição livre para carimbo (sem sobrepor texto).

### Algoritmo

1. **Renderiza** página como imagem (PyMuPDF/fitz)
2. **Testa candidatos** em grade regular
3. **Valida** contra 2 camadas de segurança:
   - Texto vetorial real (nunca pode cobrir)
   - Verificação de pixels para texto rasterizado (scanners)
4. **Fundo branco próprio** do carimbo cobre decorações (cores, tabelas)

### Funções Principais

#### `encontrar_area_livre()`

```python
encontrar_area_livre(doc, concessionaria='', arquivo='') -> tuple | None
```

Função de entrada. Tenta, em ordem, **3 tamanhos de carimbo**:
1. 180×60 pontos (original)
2. 140×45 pontos (fallback 1)
3. 110×35 pontos (fallback 2)

Prioriza: primeira página → primeiro tamanho → melhor posição.

**Retorno**: Tupla `(indice_pagina, x_pdf, y_pdf, largura_carimbo, altura_carimbo)` ou `None`

#### `melhor_regiao()`

```python
melhor_regiao(imagem, blocos, largura_c_img, altura_c_img, margem_c_img) -> tuple | None
```

Percorre linhas candidatas (Y) e escolhe candidato com **menor percentual de tinta**. Usa **early-exit** — não continua testando linhas piores (acelera busca).

#### `gerar_ordem_y()`

Define prioridade das linhas:
1. Topo da página (35% superiores, de cima para baixo)
2. Restante ordenado pela proximidade do centro vertical

#### `possui_texto_pdf()` e `possui_texto_pequeno()`

Duas camadas de segurança:
- `possui_texto_pdf()` – detecta texto vetorial
- `possui_texto_pequeno()` – detecta padrões de texto rasterizado (pixels escuros)

### 🚀 Otimizações

- `renderizar_pagina()` e `get_text('blocks')` chamados **uma vez por página** (não por tentativa)
- `melhor_regiao()` usa **early-exit por linha** — reduz drasticamente tempo em páginas densas

---

## 🖨️ 12. carimbar_pdfs.py

**Função**: Desenha carimbo (PO, CNPJ, SGE TIM) e organiza saída.

### Função: `carimbar_pdf()`

```python
carimbar_pdf(pdf_origem, concessionaria, po, cnpj) -> bool
```

**Parâmetros**:
| Param | Tipo | Descrição |
|-------|------|-----------|
| `pdf_origem` | str \| Path | Caminho do PDF original |
| `concessionaria` | str | Nome da concessionária |
| `po` | str | Número do Pedido |
| `cnpj` | str | CNPJ (cru, sem formatação) |

**Retorno**: `True` (sucesso) ou `False` (movido para SEM_CARIMBO)

### Função: `formatar_cnpj()`

```python
formatar_cnpj(cnpj: str) -> str
```

Formata 14 dígitos no padrão `XX.XXX.XXX/XXXX-XX`.

### Fluxo

1. Abre PDF original
2. Busca área livre (via `posicionador_carimbo`)
3. Desenha pequeno retângulo branco + 3 linhas de texto
4. Se **sucesso**: move para `output/pdfs/carimbados/{CONCESSIONÁRIA}/`
5. Se **falha** (nenhuma área em nenhuma página): copia para `output/pdfs/SEM_CARIMBO/`

---

## 📧 13. envio_gedi.py

**Função**: Envia PDF carimbado via API de e-mail, com duplicidade, retry e fila.

### Fluxo Crítico

1. **Verifica duplicidade**: Consulta `tab_arquivos_enviados` / `tab_protocolos_enviados`
2. **Monta assunto**: Aplica regra de negócio
3. **Envia com retry**: Até 3 tentativas imediatas
4. **Grava protocolo**: No banco (sucesso)
5. **Fila local**: Se falhar (pendências para reprocessamento)

### Função: `enviar_fatura_gedi()`

```python
enviar_fatura_gedi(pdf_path, dados_fatura) -> tuple[bool, dict]
```

**Parâmetros**:
| Param | Tipo | Descrição |
|-------|------|-----------|
| `pdf_path` | str \| Path | Caminho do PDF carimbado |
| `dados_fatura` | dict | concessionaria, uc, cod_uc, nota_fiscal, mes_referencia, backlog, data_vencimento, link_pdf_fatura, refaturamento, reenvio |

**Retorno**: Tupla `(sucesso, resposta_json)`

### Função: `montar_assunto()`

```python
montar_assunto(concessionaria, backlog, data_vencimento) -> str
```

Aplica regra de negócio:

| Cenário | Assunto |
|---------|---------|
| Backlog + vencida | `{CONCESSIONARIA} - BACKLOG` |
| Backlog + prestes a vencer (0-10 dias) | `{CONCESSIONARIA} - BACKLOG - PRESTES A VENCER` |
| Normal + já vencida | `{CONCESSIONARIA} - VENCIDA - PRIORIDADE` |
| Normal + prestes a vencer (0-10 dias) | `{CONCESSIONARIA} - PRESTES A VENCER - PRIORIDADE` |
| Normal + sem urgência (>10 dias) | `{CONCESSIONARIA}` |

### Outras Funções

| Função | Descrição |
|--------|-----------|
| `_ja_foi_enviado()` | Consulta banco para saber se fatura já foi enviada |
| `_chamar_api_envio()` | Faz chamada HTTP real à API |
| `_enviar_com_tentativas()` | Retry até 3 vezes |
| `_salvar_pendente()` | Copia PDF + JSON para fila local |
| `_gravar_protocolo_e_arquivo()` | Grava registro no banco (sucesso) |
| `reprocessar_pendentes()` | Percorre pendências e tenta reenviar |

### 📋 Contrato da API

**Método**: `POST` para `URL_EMAIL`  
**Content-Type**: `multipart/form-data`  
**Autenticação**: Header `X-Api-Token` (não Bearer, não no corpo)

**Campos**:
- `email` (texto) – destinatário
- `subject` (texto) – assunto
- `cc` (texto, opcional) – cópia
- `file` (arquivo) – PDF

**Resposta (sucesso)**:
```json
{
  "success": true,
  "data": { ... }
}
```

### 📌 Pendência Conhecida

Campo `cod_fatura` não é populado — `consulta_faturas.py` não expõe identificador equivalente ao `Cod_Fatura` das tabelas legadas (sistema PHP anterior). Isso **não afeta duplicidade** (que usa `cod_uc + mes_referencia`), mas deixa campo vazio nas tabelas de envio.

---

## 🎯 14. main.py

**Função**: Orquestra pipeline completo com medição de performance.

### Função: `main()`

```python
main() -> None
```

Executa pipeline para cada modo (normal + backlog 1x/semana), medindo tempo de cada etapa.

### Função: `deve_rodar_backlog()`

```python
deve_rodar_backlog() -> bool
```

Retorna `True` se `controle_backlog.json` não existe ou passaram 7+ dias.

### Características

- **Sequencial**: Um item por vez (simples depuração, sem concorrência)
- **Medição**: Tempo de cada bloco (busca, validação, download, carimbo, envio)
- **Backlog**: Controlado por `controle_backlog.json` (1x/semana)

---

## ⚡ 15. Notas de Performance e Paralelismo

**Teste real**: 1.437 faturas (modo normal)

| Etapa | Tempo/item | % do Total | Notas |
|-------|-----------|-----------|-------|
| Download PDF | ≈0,57 s | — | I/O rede — bom candidato a threads |
| Carimbagem | ≈0,77–0,92 s | — | CPU-bound (PyMuPDF/numpy) |
| **Envio GEDI** | **≈3,2–3,5 s** | **68%** | **Gargalo dominante** |

### Decisão Atual

Execução **sequencial** (consciente) por:
- ✅ Simplicidade
- ✅ Previsibilidade
- ✅ Evita concorrência no banco + API

### Futuro

Se volume crescer:
- ✅ Paralelizar download + envio com **threads**
- ⚠️ Exige monitorar **rate-limit** da API do GEDI antes de aumentar concorrência

---

## 🧪 16. Scripts de Teste (uso manual)

### `testar_carimbo.py`

Percorre PDFs em `output/pdfs/teste_carimbo/` e chama `carimbar_pdf()` diretamente.

**Uso**: Validar visualmente posicionamento em casos difíceis (fundos coloridos, tabelas densas) sem rodar pipeline completo.

### `teste_envio_gedi.py`

Chama `enviar_fatura_gedi()` com dados fictícios, sem passar pelo banco/carimbagem.

**Uso**: Validar isoladamente regra de assunto, duplicidade e contrato da API antes de testar fluxo completo.

### 💡 Boa Prática

```python
# Antes de testar main.py com dados reais:
df_ok = df_ok.head(3)  # Restrinja a poucas linhas
```

Valida fluxo de ponta a ponta sem processar volume total na primeira tentativa.

---

## 📞 Contato

- **Responsável**: Isabelle Jelic
- **E-mail**: isabellevic.jelic@gmail.com
- **LinkedIn**: [Isabelle Jelic](https://www.linkedin.com/in/isabelle-jelic-1439841b9/)

---

**Última atualização**: Setembro 2026  
**Versão**: 1.0
