```
Gegeben ist der folgende Nutzer-Prompt:  
{PLACEHOLDER}Finde die zu diesem Prompt am besten passenden Klassen aus folgender 'class_name' Liste:  
- barbarian  
- bard  
- cleric  
- druid  
- fighter  
- monk  
- paladin  
- ranger  
- rogue  
- sorcerer  
- warlock  
- wizard  
  
Gib als Ergebnis ein JSON mit folgendem Format zurück:  
{  
"matched_classes": [best_class, second_best_class, thrid_best_class],  
"keywords": [keywords aus user_promt, die den character, seine Fähigkeiten und Eingeschaften beschreiben],  
"rewritten_prompt_template": [umgeschriebene user_prompt mit best_class, umgeschriebener user_promt mit second_best_clas, ...]  
}  
Beispiel:  
user_promt: "dunkler Magier, der tote beschwört und feuer Zauber beherrscht"  
Antwort:{  
"matched_classes": ["wizard", "warlock", "cleric"],  
"keywords": ["dunkel", "beschwörung", "feuer", "tote", "zauber"],  
"rewritten_prompt_template": [  
"dunkler wizard, der tote beschwört und Feuerzauber beherrscht",  
"dunkler warlock, der tote beschwört und Feuerzauber beherrscht",  
"dunkler cleric', der tote beschwört und Feuerzauber beherrscht"]}  
  
Gebe als Antwort nur das Json zurück. Keine erklärungen, oder kommentare. Keine ''' oder ``` am Anfang oder Ende deiner antwort. Auch kein 'Json:' oder 'json' am Anfnag der Antwort.  
Nur den reinen text, der mit '{' beginnt und mit '}' endet.  
  
Hier noch mal das format in dem du die antwort zurück geben sollst.  
Rückgabeformat: text  
Verbotene formate: Markdwon
```
