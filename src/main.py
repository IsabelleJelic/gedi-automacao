import logging

from consulta_faturas import buscar_faturas
from validacoes import validar_faturas
from gerar_arquivos import gerar_csvs
from periodo import obter_periodo
from carimbar_pdfs import carimbar_pdf

logging.basicConfig(
    filename="logs/automacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


MAPA_CONCESSIONARIAS = {
    "COELBA": "COELBA",
    "CELPE": "CELPE",
    "COSERN": "COSERN",

    "CPFL SANTA CRUZ (JAGUARI)": "CPFL SANTA CRUZ (JAGUARI)",

    "CPFL PIRATININGA": "CPFL",
    "CPFL PAULISTA": "CPFL",

    "RGE": "RGE",
    "RGE SUL": "RGE",

    "ENERGISA MT": "ENERGISA_MT",
    "ENERGISA MS": "ENERGISA_MS",
    "ENERGISA RO": "ENERGISA_RO",
    "ENERGISA TO": "ENERGISA_TO",
    "ENERGISA ACRE": "ENERGISA_ACRE",
    "ENERGISA PB": "ENERGISA_PB",
    "ENERGISA MR": "ENERGISA_MR",
    "ENERGISA SE": "ENERGISA_SE",

    "COPEL": "COPEL",

    "AMAZONAS": "AMAZONAS",

    "EQUATORIAL RS": "EQUATORIAL",
    "EQ GOIAS": "EQUATORIAL_GOIAS",

    "LIGHT": "LIGHT",

    "ENEL CE": "ENEL_CE",
    "ENEL RIO": "ENEL_RIO",
    "ENEL GOIAS": "ENEL_GOIAS",

    "EDP SP": "BANDEIRANTE",
    "EDP ES": "ESCELSA",

    "CELESC": "CELESC",
    "CEMIG": "CEMIG",
}


def normalizar_concessionaria(nome):

    nome = str(nome).strip().upper()

    return MAPA_CONCESSIONARIAS.get(nome)


def main():

    modo = input(
        "Modo (normal/backlog): "
    ).strip().lower()

    data_inicio, data_fim = obter_periodo(
        modo
    )

    print(
        f"\nPeríodo: {data_inicio} até {data_fim}\n"
    )

    logging.info(
        f"Modo selecionado: {modo}"
    )

    logging.info(
        f"Período: {data_inicio} até {data_fim}"
    )

    logging.info("Iniciando automação")

    print("Buscando faturas...")

    df = buscar_faturas(
        data_inicio,
        data_fim
    )

    print(df.head())
    print()
    print(df.columns.tolist())
    print()
    print(f"Total de registros: {len(df)}")

    logging.info(
        f"{len(df)} faturas encontradas"
    )

    print("Validando...")

    df_ok, df_erro = validar_faturas(df)

    print("\nResumo dos erros:\n")

    resumo = df_erro["Motivo"].value_counts()

    for motivo, quantidade in resumo.items():
        print(f"{motivo}: {quantidade}")

    logging.info(
        f"{len(df_ok)} prontas para envio"
    )

    logging.info(
        f"{len(df_erro)} para validação"
    )

    gerar_csvs(
        df_ok,
        df_erro
    )

    logging.info(
        "CSV gerados com sucesso"
    )

    print("\nCarimbando PDFs...\n")

    for _, linha in df_ok.iterrows():

        concessionaria = normalizar_concessionaria(
            linha["Concessionária"]
        )

        if not concessionaria:

            logging.warning(
                f"Concessionária não mapeada: "
                f"{linha['Concessionária']}"
            )

            continue

        nome_pdf = f"{linha['Unidade']}.pdf"

        origem = (
            f"output/pdfs/originais/{nome_pdf}"
        )

        destino = (
            f"output/pdfs/carimbados/{nome_pdf}"
        )

        try:

            carimbar_pdf(
                origem,
                destino,
                concessionaria,
                linha["PO"],
                linha["CNPJ do Pedido"]
            )

        except Exception as erro:

            logging.error(
                f"Erro ao carimbar "
                f"{nome_pdf}: {erro}"
            )

    print(
        "\nProcesso concluído."
    )


if __name__ == "__main__":
    main()