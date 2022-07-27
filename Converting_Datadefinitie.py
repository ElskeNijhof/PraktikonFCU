import pandas as pd
from docx import Document
import os

os.chdir('Z:\\medewerkers\\Elske\\FamilyCheckUp')

vragenlijstnaam = 'FCU - Ouder over Kind 11-17 (1)'
# Converten van datadefinitie naar pandas dataframe
path = 'Z:\\medewerkers\\Elske\\FamilyCheckUp\\automatiseren bijlagen AST Elske\\Datadefinities FCU Ouder over Kind 11-17.docx'

document = Document(path)


tables = []
for table in document.tables:
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            if cell.text:
                df[i][j] = cell.text
    tables.append(pd.DataFrame(df))
#print(tables)

tables[1].to_pickle('df_FCU_Vragenlijst_{}'.format(vragenlijstnaam))
tables[2].to_pickle('df_FCU_ValueLabels_{}'.format(vragenlijstnaam))

print('Done')
