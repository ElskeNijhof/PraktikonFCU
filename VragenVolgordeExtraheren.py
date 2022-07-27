# Volgorde van vragen extraheren uit word document

import pandas as pd
import os
from docx import Document

path = 'Z:\\medewerkers\\Elske\\FamilyCheckUp\\automatiseren bijlagen AST Elske\\Ontwerp Bijlage FCU OuderKind4-5.docx'

document = Document(path)

tables = []
for table in document.tables:
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            if cell.text:
                df[i][j] = cell.text
    tables.append(pd.DataFrame(df))

volgorde = []

for table in tables: 
    for value in table[1].values:
        volgorde.append(value.strip('<<>>'))

volgorde = [vraag.strip('\n') for vraag in volgorde]
print(volgorde)


