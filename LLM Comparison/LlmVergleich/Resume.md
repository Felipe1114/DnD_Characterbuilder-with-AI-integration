
Ich habe mit Mistral, ChatGpt und Gemini meinen beiden Prompts getestet. 

Bei der aufgabe den `user_prompt`um zuschreiben, waren alle Modelle gleich auf. 
Allein Gemini hatte ein bischen weniger `character_details`in seiner Antwort, aber nichts, was all zu stark ins Gewicht fällt. 

Daher ist mein Resume in noten für die drei Modelle:


### rewrite_user_prompt resume:
>[!Warning]+ **Rewrite_user_prompt Resume:
>
>**Mistral:** **B** 
>Gutes ergebnis, Struktur war wie befohlen.
>Das Ergebnis der ‚Rewritten_Prompts‘ war gut, aber die Klasse wurde einfach nur an den ursprünglichen user_prompt angehängt: 
>```
>Erstelle einen Robin Hood, aus Robin Hood. Level 10. ranger.			
>```
>
>**ChatGpt: A**
>Ebenso gut, wie Mistral im Endergebnis. 
>Allerdings hat ChatGpt einen besseren ‚rewritten_user_prompt‘ abgegeben: 
>```
>Erstelle einen Robin Hood, ein ranger auf Level 10.
>```
>
>**Gemini: B**
>Gemini hat den ‚rewritten_user_prompt‘ auch besser als Mistral geschrieben. Aber dafür hat Gemini ein bischen zu wenige details.

### Generate Character Resume:
>[!Warning]+ **CharGen Resume Mistral**:
>Prompt_lenght: `199869`
>
>Mistral hatte gar keine probleme den Prompt anzunehmen. 
>Ich konnte den Text direckt in das Browserfenster eingeben und kurz darauf wurde der Character erstellt.
>
>Mein Resume ist daher: **A**

>[!Warning]+ **CharGen Resume ChatGpt:**
>Prompt_lenght: `199877`
>
>ChatGPT konnte den Prompt zwar nicht direckt von der Textleiste übernehmen, aber ein großes File wurde von ChatGpt gelesen.
>
>Der Erstellte Character ist nicht ganz vollständig. Es fehlen: 
>- Prepared_spells
>- skills
>  
> Das fehlen der skills ist ein großer Malus. Ohne diese ist der Character unspielbar.
> 
>Mein Resume ist daher: **D**

>[!Warning]+ **CharGen Resume Gemini:**
>
>Prompt_lenght: `191562`
>Gemini ist komplett durchgefallen. 
>Gemini konnte weder den Prompt direkt ausführen, da er zu groß war; noch konnte Gemini den Prompt als file oder gesplitted in 11 kleinere files, verarbeiten. 
>
>die Antwort von Gemini auf die 11 angehängten files war: 
>```
>The provided files contain information about Dungeons and Dragons (D&D) classes and spells in JSON format, along with details for creating a character. I will act as a D&D expert to create a character based on this information.
>
>My task is to construct a D&D character, selecting abilities and spells that align with the themes of 'Necromancy', 'dark magic', and 'fire magic' as described in the character details example. The final character will be returned in JSON format.
>
I have successfully retrieved the content from all the provided files:
>
>- `gemini_texts_1.txt`
  >  
>- `gemini_texts_2.txt`
mini_texts_3.txt`
  >  
>- `gemini_texts_4.txt`
  >  
>- `gemini_texts_5.txt`
  >  
>- `gemini_texts_6.txt`
  >  
>- `gemini_texts_7.txt`
  >  
>- `gemini_texts_8.txt`
  >  
>- `gemini_texts_9.txt`
  >  
>- `gemini_texts_10.txt`
  >  
>
Now I will proceed to combine and parse the content to generate the character.
>```
>
>Mein Resume ist daher: **F


### Schluss Resume:

>[!Warning]+ **Schluss Resume**:
>Mistral schneidet mit **-A** am besten ab. 
>
>Kurz darauf folgt ChatGpt mit **-C**. Es macht zwar insgesammt einen guten Job bei der user_prompt_analyse, aber die Character Generierung ist nur sehr dürftig brauchbar. 
>
>Am schluss folgt Gemini, mit einem glatten **F**. Zwar funktioniert das umschreiben des user_prompts, aber wenn kein character erstellt werden kann, dann ist Gemini nicht zu gebrauchen

