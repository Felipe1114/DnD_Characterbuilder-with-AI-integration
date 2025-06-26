[[RewritePrompt]]

# Robin Hood

>[!Info]+ user_prompt:
>```
Robin hood, aus Robin hood. Level 10

>[!Info]+ rewrite_user_prompt_prompt:
>```
Gegeben ist der folgende Nutzer-Prompt:  
Robin hood, aus Robin hood. Level 10. Finde die zu diesem Prompt am besten passenden Klassen aus folgender 'class_name' Liste:  
>- barbarian  
>- bard  
>- cleric  
>- druid  
>- fighter  
>- monk  
>- paladin  
>- ranger  
>- rogue  
>- sorcerer  
>- warlock  
>- wizard  
  >
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
  >
Gebe als Antwort nur das Json zurück. Keine erklärungen, oder kommentare. Keine ''' oder ``` am Anfang oder Ende deiner antwort. Auch kein 'Json:' oder 'json' am Anfnag der Antwort.  
Nur den reinen text, der mit '{' beginnt und mit '}' endet.  
  >
Hier noch mal das format in dem du die antwort zurück geben sollst.  >
Rückgabeformat: text  
Verbotene formate: Markdwon

## Mistral
```{
"matched_classes": ["ranger", "rogue", "fighter"],
"keywords": ["Robin Hood", "Level 10", "Bogenschütze", "Dieb", "Geschicklichkeit", "Tarnung"],
"rewritten_prompt_template": [
"Robin Hood, aus Robin Hood. Level 10. ranger",
"Robin Hood, aus Robin Hood. Level 10. rogue",
"Robin Hood, aus Robin Hood. Level 10. fighter"
]
}
```

## Gemini 2.5 Flash
```
{
"matched_classes": ["ranger", "rogue", "fighter"],
"keywords": ["Robin Hood", "Dieb", "Bogenschütze", "gerecht"],
"rewritten_prompt_template": [
"Robin Hood als Ranger, Level 10.",
"Robin Hood als Rogue, Level 10.",
"Robin Hood als Fighter, Level 10."
]
}
```


## ChatGpt 4
```
{  
"matched_classes": ["ranger", "rogue", "fighter"],  
"keywords": ["Robin Hood", "Bogenschütze", "Wald", "Dieb", "Geschicklichkeit", "Heimlichkeit", "Gerechtigkeit"],  
"rewritten_prompt_template": [  
"Robin Hood, ein ranger auf Level 10",  
"Robin Hood, ein rogue auf Level 10",  
"Robin Hood, ein fighter auf Level 10"  
]  
}
```
