from copyreg import pickle
import pandas as pd
from docx import Document
import os

os.chdir("Z:\medewerkers\Elske\FamilyCheckUp")
pd.set_option('display.max_rows', 500)

# Onderstaande twee regels aanpassen
vragenlijstnaam = 'FCU - Ouder over Kind 11-17 (1)' # naam van de vragenlijst zoals die genoemd wordt in het export excel bestand
aantal_vragen = 142

# Vraag code, vragen en de antwoorden worden aan elkaar gekoppeld
path = 'Z:\\medewerkers\\Elske\\FamilyCheckUp\\df_FCU_Vragenlijst_{}'.format(vragenlijstnaam)
path_Excel = 'Z:\\medewerkers\\Elske\\FamilyCheckUp\\automatiseren bijlagen AST Elske\\export_FCUlijsten.xlsx'

df_Def = pd.read_pickle(path)

df_Excel = pd.read_excel(path_Excel, sheet_name= vragenlijstnaam)
df_Excel = pd.DataFrame(df_Excel.iloc[0])
print('Excel antwoorden', df_Excel)

antwoorden = df_Excel[32:32+aantal_vragen]
vragen = pd.DataFrame(df_Def[2][1:1+aantal_vragen]) 
vraag_cod = pd.DataFrame(df_Def[0][1:1+aantal_vragen])

# Vragen en antwoorden samenvoegen
results = pd.DataFrame()
results['Vraag_cod'] = vraag_cod
results['Vragen'] = vragen
results['Antwoorden'] = antwoorden.values

# Vragen reordenen op basis van het document Ontwerp_Bijlage_FCU
# Verkregen vanuit het script 'VragenVolgordeExtraheren.py'
volgorde = ['Q9_5', 'Q10_2R', 'Q11_2', 'Q12ZESELF_3', 'Q13ZESELF_2', 'Q9_2', 'Q10_5', 'Q11_5', 'Q13ZESELF_1R', 'Q13VIER_5R', 'Q15ELF', 'Q16ELF', 'Q17ELF', 'Q18ELF', 'Q9_3', 
'Q10_3', 'Q11_3', 'Q12VIER_1', 'Q13VIER_4', 'Q10_1', 'Q11_1R', 'Q11_4R', 'Q12VIER_4', 'Q13VIER_3', 
'Q19_1', 'Q19_2', 'Q20_1', 'Q20ZES_2', 'Q20ELF_3', 'Q20ELF_4', 'Q21ZES', 'Q21ELF_2', 'Q21ELF_3', 'Q3_1', 'Q3_2', 'Q22_1', 'Q22_2', 'Q22_3', 'Q22_4', 'Q22_5', 'Q28_1R', 'Q28_2R', 
'Q28_3', 'Q28_4', 'Q28_5R', 'Q29_1', 'Q29_2R', 'Q29_3R', 'Q29_4', 'Q29_5', 'Q30_1', 'Q30_2R', 'Q31_1', 'Q31_2', 'Q31_3', 'Q9_1', 'Q9_4', 'Q10_4', 'Q12VIER_2', 'Q12VIER_5', 'Q32_1', 'Q32VIER_2', 
'Q32VIER_3', 'Q32_5', 'Q33_1', 'Q36VIER_5', 'Q40_1', 'Q40_2', 'Q40_3', 'Q40_4', 'Q40_5', 'Q38_1', 'Q38_2', 'Q38_3', 'Q38_4', 'Q38_5', 'Q38_6', 'Q39_1', 'Q39_2', 'Q39_3', 'Q39_4', 'Q39_5', 'Q12_1', 
'Q12_2', 'Q12_3', 'Q12_4', 'Q12_5', 'Q12_6', 'Q32_4', 'Q33VIER_2', 'Q37_1', 'Q37_2', 'Q34_1', 'Q34_2', 'Q34_3', 'Q34_4', 'Q34_5', 'Q35_1', 'Q35_2', 'Q24ELF_3', 'Q24ELF_4', 'Q24ELF_5', 'Q25ELF_1', 
'Q25ELF_2', 'Q25ELF_3', 'Q25ELF_4', 'Q26ELF_1', 'Q26ELF_2', 'Q24ELF_4_II', 'Q23 ZESELF _1', 'Q23 ZESELF _2', 'Q23 ZESELF _3', 'Q23 ZESELF _4', 'Q23 ZESELF _5', 'Q24ELF_1', 'Q24ELF_2', 'Q41_1', 'Q41_2', 
'Q41_3', 'Q41_4R', 'Q41_5', 'Q35VIER_3', 'Q35VIER_4', 'Q35VIER_5', 'Q36VIER_1', 
'Q36_1', 'Q36VIER_2', 'Q36_2', 'Q36VIER_3', 'Q36VIER_4', 'Q2', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q42', 'Q43']

results['Vraag_cod'] = pd.Categorical(results['Vraag_cod'], volgorde) 

nr = [i for i in range(aantal_vragen)]
order = dict(zip(volgorde, nr))

results['Vraag_cod'].replace(order)
results.sort_values("Vraag_cod")

results["Vraag_cod"] = results["Vraag_cod"].astype("category")
results["Vraag_cod"].cat.set_categories(volgorde, inplace=True)

results = results.sort_values(["Vraag_cod"])  ## 'sort' changed to 'sort_values'
print('Ordered:', results)

results.to_pickle('df_ordered_results_{}'.format(vragenlijstnaam))
print('Antwoord_Vraag_Ordenen.py is gerund')



