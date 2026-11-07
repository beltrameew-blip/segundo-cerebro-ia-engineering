"""Validação local não destrutiva do pacote do portfólio DIO.

Uso: python VALIDAR_ENTREGA.py
A ausência de prints/notebook é registrada como pendência real, nunca mascarada.
"""
from pathlib import Path
import csv

root = Path(__file__).resolve().parent
obrigatorios = [
    "README.md", "COMO_FINALIZAR.md", "ENTREGA_DIO.txt",
    "prompts/diretriz-do-notebook.md", "prompts/perguntas-e-testes.md",
    "fontes/fontes.csv", "materiais/guia-de-estudos-autoral.pdf",
    "materiais/mapa-conceitual-autoral.png",
    "evidencias/registro-das-respostas.md", "estudio/README.md", "estudio/AI_Second_Brain_Architecture.pdf", "estudio/REVISAO_TECNICA_DA_APRESENTACAO.md",
]
faltantes = [str(x) for x in obrigatorios if not (root/x).is_file() or (root/x).stat().st_size == 0]
assert not faltantes, f"Faltam arquivos: {faltantes}"
with (root/"fontes/fontes.csv").open(encoding="utf-8-sig", newline="") as f:
    linhas = list(csv.DictReader(f))
assert len(linhas) == 5
assert len(set(x["id"] for x in linhas)) == len(linhas)
readme = (root/"README.md").read_text(encoding="utf-8")
assert "https://notebook.google.com/notebook/3f126bd0-0531-4f2b-a92e-90604b2ab848" in readme
for filename in obrigatorios:
    assert (root/filename).exists()
print("OK: arquivos estruturais, fontes e materiais autorais presentes.")
print("PENDENTE: prints de citacoes abertas; mapa mental real; teste externo do notebook; publicacao Github.")
print("STATUS FINAL: PREPARADO PARA EXECUCAO, AINDA NAO SUBMETIVEL A DIO.")
