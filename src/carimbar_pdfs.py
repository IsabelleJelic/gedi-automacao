import os
import fitz

from lista_posicoes_carimbo import (
    lista_posicoes_carimbo
)


def obter_posicao(
    concessionaria,
    tamanho_kb
):

    posicoes = lista_posicoes_carimbo()

    if concessionaria not in posicoes:
        return None

    regras = posicoes[concessionaria]

    for regra in regras:

        if regra["modo"] == "":
            return regra

        if (
            regra["modo"] == ">"
            and tamanho_kb > regra["tamanho"]
        ):
            return regra

        if (
            regra["modo"] == "<="
            and tamanho_kb <= regra["tamanho"]
        ):
            return regra

    return None


def carimbar_pdf(
    pdf_origem,
    pdf_destino,
    concessionaria,
    po,
    cnpj
):

    tamanho_kb = round(
        os.path.getsize(pdf_origem)
        / 1024
    )

    regra = obter_posicao(
        concessionaria,
        tamanho_kb
    )

    if not regra:
        print(
            f"Sem posição cadastrada: "
            f"{concessionaria}"
        )
        return False

    doc = fitz.open(pdf_origem)

    for pagina in doc:

        pagina.insert_text(
            regra["pedido"],
            str(po),
            fontname="helvetica-bold",
            fontsize=10
        )

        pagina.insert_text(
            regra["cnpj"],
            str(cnpj),
            fontname="helvetica-bold",
            fontsize=10
        )

        pagina.insert_text(
            regra["sge"],
            "SGE TIM",
            fontname="helvetica-bold",
            fontsize=10,
            fill=(0.247, 0.2, 1)
        )

    doc.save(pdf_destino)

    return True