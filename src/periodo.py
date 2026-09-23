from datetime import date
from dateutil.relativedelta import relativedelta


def obter_periodo(modo):

    hoje = date.today()

    primeiro_dia_mes_atual = hoje.replace(day=1)

    if modo == "normal":

        data_inicio = (
            primeiro_dia_mes_atual
            - relativedelta(months=1)
        )

        data_fim = primeiro_dia_mes_atual

    elif modo == "backlog":

        data_inicio = (
            primeiro_dia_mes_atual
            - relativedelta(months=7)
        )

        data_fim = (
            primeiro_dia_mes_atual
            - relativedelta(months=2)
        )

    else:
        raise ValueError(
            "Modo inválido"
        )

    return data_inicio, data_fim