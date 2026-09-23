import requests
from pathlib import Path


PASTA_PDFS = Path("output/pdfs")
PASTA_PDFS.mkdir(
    parents=True,
    exist_ok=True
)