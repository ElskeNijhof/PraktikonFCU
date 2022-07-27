READ ME

Converterting_Datadefinitie.py

* leest word doc: Datadefinitie FCU Vragenlijst Kind.docx in en zet het om in twee pandas dataframe
* DFs wordt opgeslagen als pickle
* Output: 
	- pickle df vragenlijst kind (vragen en bijbehorende codes)
	- pickle df antwoord variabel en bijpassende label 

Antwoorden_Vraag_Ordenen.py

* leest de gegeven antwoorden van de vragenlijst in
* Koppelt vragen en antwoorden bij elkaar
* Vragen worden gereordend (de volgorde van de vragen is verkregen door het python bestand: VragenVolgordeExtraheren.py)
* Vragen en antwoorden worden opgeslagen als pickle bestand


VragenVolgordeExtraheren.py

* Leest automatiseren bijlagen AST in
* Extraheert de vraagcodes op volgorde waarin ze gesteld worden

ResultatenVeranderen.py

* Converteert de antwoorden (5.8, 6.3 etc) naar de label antwoorden (bijv. Vóor 6 uur, tussen 6 uur en half zeven)



