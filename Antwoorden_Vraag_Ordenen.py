from copyreg import pickle
import pandas as pd
from docx import Document
import os

os.chdir("Z:\medewerkers\Elske\FamilyCheckUp")

# Vraag code, vragen en de antwoorden worden aan elkaar gekoppeld
path = 'Z:\\medewerkers\\Elske\\FamilyCheckUp\\df_FCU_Vragenlijst_Kind'
path_Excel = 'Z:\\medewerkers\\Elske\\FamilyCheckUp\\automatiseren bijlagen AST Elske\\export_FCUlijsten.xlsx'

df_Def = pd.read_pickle(path)
df_Excel = pd.read_excel(path_Excel)
df_Excel = pd.DataFrame(df_Excel.iloc[0])

antwoorden = df_Excel[32:141]
vragen = pd.DataFrame(df_Def[2][1:110])
vraag_cod = pd.DataFrame(df_Def[0][1:110])

# Vragen en antwoorden samenvoegen
results = pd.DataFrame()
results['Vraag_cod'] = vraag_cod
results['Vragen'] = vragen
results['Antwoorden'] = antwoorden.values

# Vragen reordenen op basis van het document Ontwerp_Bijlage_FCU
# Verkregen vanuit het script 'VragenVolgordeExtraheren.py'
volgorde = ['SDQ5', 'SDQ7R', 'SDQ12', 'SDQ18', 'SDQ22', 'SDQ2', 'SDQ10', 'SDQ15', 'SDQ21R', 'SDQ25R', 'Q16', 'Q17', 'Q18_1', 'Q18_2', 'Q19', 'Q20', 'Q21_1', 'Q21_2', 'Q22_1', 'Q22_2', 'SDQ3', 'SDQ8', 'SDQ13', 'SDQ16', 'SDQ24', 'SDQ6', 'SDQ11R', 'SDQ14R', 'SDQ19', 'SDQ23', 'Q24_1', 'Q24_2', 'Q25_1', 'Q25_2', 'Q25_3', 'Q25_4', 'Q23_1', 'Q23_2', 'Q23_3', 'Q26_1', 'Q26_2', 'Q26_3', 'Q26_4', 'Q26_5', 'Q38_1', 'Q38_2', 'Q38_3', 'Q38_4', 'Q9', 'Q10', 'Q33_1R', 'Q33_2', 'Q33_3', 'Q33_4R', 'Q33_5', 'Q34_1', 'Q34_2', 'Q34_3', 'Q34_4R', 'Q34_5', 'Q35_1R', 'Q35_2R', 'Q35_3R', 'Q35_4R', 'Q36_1', 'Q36_2R', 'Q37_1', 'Q37_2', 'Q37_3', 'SDQ1', 'SDQ4', 'SDQ9', 'SDQ17', 'SDQ20', 'Q39_1', 'Q39_2', 'Q39_3', 'Q39_4', 'Q39_5', 'Q40_1', 'Q40_2', 'Q40_3', 'Q40_4', 'Q30_1', 'Q30_2', 'Q30_3', 'Q30_4', 'Q30_5', 'Q31_1', 'Q31_2', 'Q31_3', 'Q31_4', 'Q32', 'Q27_1', 'Q27_2', 'Q28_1', 'Q28_2', 'Q29_1', 'Q29_2', 'Q29_3', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6','Q7','Q8', 'Q41_1', 'Q41_2']
results['Vraag_cod'] = pd.Categorical(results['Vraag_cod'], volgorde) 

nr = [i for i in range(109)]
order = dict(zip(volgorde, nr))

results['Vraag_cod'].replace(order)
results.sort_values("Vraag_cod")

results["Vraag_cod"] = results["Vraag_cod"].astype("category")
results["Vraag_cod"].cat.set_categories(volgorde, inplace=True)

results = results.sort_values(["Vraag_cod"])  ## 'sort' changed to 'sort_values'
print('Ordered:', results)

results.to_pickle('df_ordered_results')
print('Antwoord_Vraag_Ordenen.py is gerund')



