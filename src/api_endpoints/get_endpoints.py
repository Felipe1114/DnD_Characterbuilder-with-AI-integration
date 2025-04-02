"""
Endpunkte sind:

Daten von DnD5e API laden(GET)

alle Klassen daten werden von der DnD5e API gezogen

analyse user promt(POST)

promt wird analysiert

analysierte daten werden in datenbank abgespeichert

pro user promt gibt es bis zu vier request-promts.

bsp: request promt:'dunkler {Klassen_name} der tote beschwören kann und feuer Magie nutzt'
Klassen_namen : ['wizard', ‘sorcerer’, ‘celric’, ‘warlock’]

generate Charcters(GET, POST)

analysierte request-promts werden geladen und mit lokalen daten (Klassen daten von DnD5e API) an LLM gegeben.

Aus den daten werden dann vier Charactere erstellt und als Json zurück gegeben.

erstelle Charactere werden in Datenbank gespeichert
"""