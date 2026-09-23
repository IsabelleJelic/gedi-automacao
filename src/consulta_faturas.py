import pandas as pd

from banco import conectar


def buscar_faturas(
    data_inicio,
    data_fim
):

    sql = """
    SELECT
        f.Cod_UC AS 'Unidade',
        f.Mes_Ref AS 'Mês de referência',
        f.Concessionaria AS 'Concessionária',
        f.Dt_Venc_NF AS 'Data de Vencimento',
        f.Cod_Barras AS 'Boleto',
        f.NroNF AS 'NF',
        f.Dt_Emissao_NF AS 'Data de emissão',
        f.RS_Total_Fatura AS 'Valor',
        p.Numero_Pedido AS 'PO',
        tpc.CNPJ_Pedido AS 'CNPJ do Pedido',
        COUNT(DISTINCT p.id) AS POs_Abertos,
        f.Link AS 'Link do PDF da fatura'
    FROM Faturas_Registradas_Cache f
    INNER JOIN tab_tracking_copy t
        ON t.Cod_UC = f.Cod_UC
        AND t.Mes_Ref = f.Mes_Ref
        AND f.Cod_Empresa = 2
    LEFT JOIN Tab_Pedidos_Datas p
        ON p.Cod_UC = f.Cod_UC
        AND p.Cod_Empresa = f.Cod_Empresa
        AND f.Mes_Ref >= DATE(p.Dt_Inicio)
        AND f.Mes_Ref <= DATE(
            IF(
                p.Dt_fim IS NULL
                OR p.Dt_fim = 0,
                '2099-12-01',
                p.Dt_fim
            )
        )
    LEFT JOIN (
        SELECT
            Numero_Pedido,
            MAX(CNPJ_Pedido) AS CNPJ_Pedido
        FROM Tab_PO_CNPJ
        GROUP BY Numero_Pedido
    ) tpc
        ON tpc.Numero_Pedido = p.Numero_Pedido
    WHERE
        t.Mes_Ref BETWEEN %(data_inicio)s
    AND %(data_fim)s
        AND f.Status_Fatura <> 'Simulada'
        AND NULLIF(t.id_arquivo, '') IS NULL
    GROUP BY
        f.Cod_UC,
        f.Mes_Ref
    ORDER BY
        f.Dt_Venc_NF
    """

    engine = conectar()

    return pd.read_sql(
    sql,
    engine,
    params={
        "data_inicio": data_inicio,
        "data_fim": data_fim
    }
)