import pandas as pd


def validar_faturas(df):

    registros_ok = []
    registros_erro = []

    for _, row in df.iterrows():

        erros = []

        if pd.isna(row["PO"]):
            erros.append("Sem PO")

        if pd.isna(row["NF"]):
            erros.append("Sem NF")

        if (
            pd.isna(row["Valor"])
            or float(row["Valor"]) == 0
        ):
            erros.append("Sem Valor")

        if pd.isna(row["Boleto"]):
            erros.append("Sem Código de Barras")

        if erros:

            linha = row.copy()

            linha["Status"] = "ERRO"
            linha["Motivo"] = "; ".join(erros)

            registros_erro.append(linha)

        else:

            registros_ok.append(row)

    return (
        pd.DataFrame(registros_ok),
        pd.DataFrame(registros_erro)
    )