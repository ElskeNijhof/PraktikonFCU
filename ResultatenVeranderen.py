import pandas as pd

df_Def = pd.read_pickle(r"Z:\medewerkers\Elske\FamilyCheckUp\df_ordered_results")
df_Valuedef = pd.read_pickle(r"Z:\medewerkers\Elske\FamilyCheckUp\df_FCU_Kind_ValueLabels")


# in de onderstaande regel wordt de vraag nummer en het antwoord samengevoegd
df_Valuedef['Pkey'] = df_Valuedef[0] + df_Valuedef[1]
df_Def['Pkey'] = str(df_Def["Vraag_cod"]) + str(df_Def["Antwoorden"])

#print(df_Valuedef)

# Pkey zoeken in de dataframe en de bijbehoorende variable value aantoevoegen

Pkey_Def = []
for i in range(len(df_Def['Vraag_cod'])):
    Pkey_Def.append(str(df_Def['Vraag_cod'].iloc[i]) + str(df_Def['Antwoorden'].iloc[i]))

df_Def['Pkey'] = Pkey_Def
print(df_Def) # Dataframe met de vragen en antwoorden op volgorde waarin ze gesteld worden
print(df_Valuedef) # Dataframe met de verschillende antwoord mogelijkheden en de bijhorende label (gewenste antwoord)

# Vind code SDQ51 in df_Valuedef
print(df_Valuedef.loc[df_Valuedef['Pkey'] ==  "SDQ51"])

# Extraheer het gewenste antwoord in plaats van het antwoord code
antwoord_woord = df_Valuedef.loc[df_Valuedef['Pkey'] ==  "SDQ7R1"][2].values[0]
print(antwoord_woord)

# Antwoord label vervangen met antwoord code wanneer dat mogelijk is anders orginele antwoord laten staan

df_Vraag_antwoord = pd.DataFrame(columns = ['Vraag', 'Antwoord'])
print(df_Vraag_antwoord)

for index, row in df_Def.iterrows():
    try: 
        antwoord_code = row['Pkey']
        antwoord_woord = df_Valuedef.loc[df_Valuedef['Pkey'] ==  antwoord_code][2].values[0]
        #print(antwoord_woord)
        df_Vraag_antwoord = df_Vraag_antwoord.append({"Vraag": row['Vragen'],
                                    "Antwoord": antwoord_woord}, ignore_index=True)

    except:
        #print('Code niet gevonden voor:', antwoord_code)
        print(row['Antwoorden'])

        df_Vraag_antwoord = df_Vraag_antwoord.append({"Vraag": row['Vragen'],
                                    "Antwoord": row['Antwoorden']}, ignore_index=True)


print(df_Vraag_antwoord)
# df_Vraag_antwoord.to_excel('Z:/medewerkers/Elske/FamilyCheckUp/Resultaten/Vraag_Antwoord_Kind.xlsx') # DataFram exporteren naar Excel bestand