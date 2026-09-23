from config import (
    PRONTO_ENVIO,
    VALIDACAO_GESTAO
)


def gerar_csvs(df_ok, df_erro):

    colunas_pronto = [
        "Concessionária",
        "Unidade",
        "Mês de referência",
        "Link do PDF da fatura",
        "PO",
        "CNPJ do Pedido",
        "NF",
        "Data de Vencimento",
        "Boleto",
        "Valor",
        "Data de emissão"
    ]

    df_ok[colunas_pronto].to_csv(
        PRONTO_ENVIO,
        sep=";",
        index=False,
        encoding="utf-8-sig"
    )

    colunas_erro = [
        "Status",
        "Motivo",
        "Concessionária",
        "Unidade",
        "Mês de referência",
        "Link do PDF da fatura",
        "PO",
        "CNPJ do Pedido",
        "NF",
        "Data de Vencimento",
        "Boleto",
        "Valor",
        "Data de emissão"
    ]

    df_erro[colunas_erro].to_csv(
        VALIDACAO_GESTAO,
        sep=";",
        index=False,
        encoding="utf-8-sig"
    )