# DnD Character Generator mit AI funktion

## Beschreibung

Mit diesem Projekt kann man sich DnD-Charactere erstellen lassen. 
Dafür gibt man dem Programm einen einfachen Satz oder eine Beschreibung des gewünschten Characters. 

Z.B 'Conan der Barbar'.

Das Programm wird dann, auf Basis der Eingabe, vier verschiedene Charactere erstellen, die auf die Beschreibung passen. 

Bei 'Conan der Barbar' würde z.B ein Barbar, ein Fighter und ein Ranger als mögliche Charactere herauskommen. 

## Programm Aufbau

Der DnD Character generator besteht aus drei Teilen, die auch in Api-Endpunkten aufgeteilt sind.

**1. Load Class Datas (GET)**

Der DnD Character generator muss erst alle nötigen Daten von der DnD5e-api ziehen. Dafür gibt es einen eigenen 'Loader'.
Der 'Loader' wird weiter unten näher beschrieben

**2. Analyse User Promt (POST)**


Die Beschreibung des Users, für einen Character muss erst einmal für das LLM aufbereitet werden. Dafür werden aus dem User Promt folgende Informationen herausgezogen:
- Alle drei möglichen Klassen
- Alle Wörter, die die Besonderen Eigenschaften der Characterbeschreibung darstellen. Z.B 'Stark', 'Berserker', 'Feuer', 'Mächtig', etc...
- Drei Varianten des User Prompts, aber mit den jeweiligen Klassen eingesetzt.

Beispiel

```JSON
{
"user_prompt": "Aang aus 'Avatar - the last airbender'",
"answer": {
    "matched_classes": ["monk", "ranger", "fighter"], 
    "keywords": ["Aang, Avatar, Luftb\u00e4ndiger, Bender, Kampf, Bewegung, Gleichgewicht"],
    "rewritten_prompt_template": ["Aang aus 'Avatar - the last airbender' als monk", "Aang aus 'Avatar - the last airbender' als ranger", "Aang aus 'Avatar - the last airbender' als fighter"]
    }
  }
```

**3. Generate Character (POST)**

Anhand der generierten Daten aus dem User Promt werden nun vier Charactere erstellt. 2x Charactere mit der 'besten' Klassen Wahl. Dies ist die erste Klasse in der Liste 'machted_classes'. Dann noch jeweils ein Charcter mit den beiden anderen Klassen.
Die Genertierten Charactere werden jeweils als JSON-Struktur ausgegeben und in der SQLite Datenbank gespeichert. 


## Programm-Struktur

```txt
main
| data
--| db
----|dnd_character_projekt.sqlite
--| debug_data
----|debug.log
--| llm_data
----|all_class_data_template.txt
----|system_message.txt
--| static_dnd_data
----| detailed_class_data
------| ...
----|all_classes.json
----|class_indizies.json
| src
--| api_endpoints
----|get_and_post_endpoints.py
----|get_endpoints.py
----|post_endpoints.py
--| database
----|db_creator.py
----|db_manager.py
----|models.py
--| dnd_api
----| base_classes
------| dnd_api_base.py
----|class_details.py
----|class_url_fetcher.py
----|dnd_api_manager.py
----|dnd_class_fether.py
----|dnd_details_fetcher.py
--| handle_data
----|character_data_loader.py
----|crud_base.py
----|crud_json.py
----|crud_txt.py
----|env_loader.py
--| helper
----| binary_algorythm
------|binary_base.py
------|bianry_dict.py
----|debug_helper.py
----|debug_log.py
----|progress_tracker.py
--| LLM
----|analyse_user_prompt.py
----|character_builder_app.py
----|system_request_builder.py
----|talk_to_mistral.py
--|app.py
|.env
|README.md
```

Im folgenden werde ich die einzelnen Module erklären.

Die Reihenfolge wird sein:

1. ```dnd_api```
2. ```llm```
   1. ```analyse user prompt```
   2. ```character builder app```



### dnd_api

Das dnd_api modul ist dafür zuständig alle Daten der 12 DnD-Klassen von der DnD5e-api herunter zu laden und lokal als JSON zu speichern. 
Für jede Klasse wird ein eigenes JSON-file angelegt, welches alle ```Spells```, ```level_features``` und ```subclass_features``` enthält.

```mermaid
---
title: DnD-api-manager
---
classDiagram
direction TB
    class DnDAPIBase {
	    + Summary
	    - Base class for interacting with the DnD5e API.
	    - Provides basic logic to make requests to the DnD5e API.
	    - Handles API responses and errors.
	    - Includes a delay to manage API request rates.
	    - Stores retrieved data in a dictionary.
	    + Methods
	    - load_data() : Loads data from the DnD5e API based on the provided URL and handles potential errors.
    }
    class DnDDetailsFetcher {
	    + Summary
	    - This class is responsible for loading detailed data for DnD classes.
	    - It inherits from DnDAPIBase and extends it with a configurable URL and data loading function.
	    - It includes a delay mechanism to protect the public API from overloading.
	    - It stores retrieved data in a dictionary.
	    - It provides methods to get and set the detail URL for fetching class data.
	    + Methods
	    - load_data(): Loads class data from the currently set URL(class_detail_url) with a delay to manage API request rates.
	    - detail_url() : Property to get the class_detail_url.
	    - detail_url.setter() : Setter method to define a new class_detail_url.
    }
    class DnDClassFetcher {
	    + Summary
	    - This class fetches and saves DnD class data.
	    - It inherits from DnDAPIBase to load data from a specified URL.
	    - It uses CrudJsonFiles to handle JSON data storage.
	    - It processes and filters the loaded data before saving.
	    - It provides a method to save the processed data.
	    + Methods
	    - load_and_save() : Loads data from the URL, processes it, and saves it.
	    - save_data() : Temporary method to save the processed data using CrudJsonFiles.
    }
    class DnDClassUrlFetcher {
	    + Summary
	    - Inherits from DnDAPIBase to fetch data from the DnD5e API.
	    - Specifically designed to retrieve URLs for all DnD classes.
	    - Loads data from a predefined API endpoint.
	    - Processes the loaded data to extract and return class URLs.
	    - Provides a method to get the URLs for all DnD classes.
	    + Methods
	    - get_class_urls() : Loads data from the API and returns a list of URLs for all DnD classes.
    }
    class ClassDetails {
	    + Summary
	    - Base class for all 12 DnD classes, providing the basic structure for subclasses.
	    - Manages data for a DnD class from the 5e API, including spells, levels, and subclasses.
	    - Loads and processes information about spells, levels, and subclasses.
	    - Enriches loaded data with detailed descriptions from the API.
	    - Uses ProgressTracker to monitor the loading progress of data.
	    + Methods
	    - initialize_all_data() : Initializes all base data including spells, levels, and subclasses.
	    - initialize_all_details() : Loads all details for spells, levels, and subclasses and returns enriched data.
	    - spell_details() : Loads detailed information about the class's spells.
	    - level_details() : Loads detailed information about the class's levels and features.
	    - subclass_details() : Loads detailed information about the class's subclasses.
    }
    class DnDApiManager {
	    + Summary
	    - Manages the fetching and storing of DnD class data from the DnD5e API.
	    - Loads base class data and detailed class data for all 12 DnD classes.
	    - Uses various helper classes to fetch, process, and store data.
	    - Tracks the progress of data loading and saving operations.
	    - Provides methods to load and save base and detailed class data.
	    + Methods
	    - run() : Executes the loading and saving of base and detailed class data.
	    - load_detaild_calss_datas() : Loads and saves detailed class data for each DnD class.
	    - load_base_class_datas() : Loads base data for all DnD classes from the DnD5e API.
    }
    class ProgressTracker {
	    + Summary
	    - Tracks and displays the progress of a task.
	    - Initializes with total steps, task name, and bar length for visualization.
	    - Provides methods to update the progress and mark the task as done.
	    - Uses standard output to display a progress bar and percentage completion.
	    - Clears the progress line and writes a completion message when done.
	    + Methods
	    - update() : Updates the progress bar and percentage based on the current step.
	    - done() : Marks the task as completed and clears the progress line.
    }
    class CrudJsonFiles {
	    + Summary
	    - Inherits from CrudBase to handle JSON file operations.
	    - Provides methods to save, load, and manage JSON data.
	    - Includes error handling for file operations.
	    - Supports creating new files and resetting existing files.
	    - Checks and creates directories if they do not exist.
	    + Methods
	    - data() : Property to get the data from the JSON file.
	    - data.setter() : Setter method to append new data to the JSON file.
	    - new_file() : Creates a new JSON file with the provided data.
	    - reset() : Resets the JSON file with optional new data.
	    - check_path() : Checks if the directory exists and creates it if it does not.
    }

    DnDAPIBase --|> DnDDetailsFetcher
    DnDAPIBase --|> DnDClassFetcher
    DnDAPIBase --|> DnDClassUrlFetcher
    ClassDetails <-- DnDDetailsFetcher
    ClassDetails <-- ProgressTracker
    DnDApiManager <-- ClassDetails
    DnDApiManager <-- DnDClassFetcher
    DnDApiManager <-- DnDClassUrlFetcher
    DnDApiManager <-- ProgressTracker
    CrudJsonFiles <--> DnDApiManager
    CrudJsonFiles <-- DnDClassFetcher

	class DnDAPIBase:::Peach
	class DnDDetailsFetcher:::Peach
	class DnDClassFetcher:::Peach
	class DnDClassUrlFetcher:::Peach
	class ClassDetails:::Peach
	class DnDApiManager:::Rose
	class ProgressTracker:::Sky
	class CrudJsonFiles:::Aqua

	classDef Rose :, stroke-width:5px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
	classDef Aqua :, stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
	classDef Peach :, stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
	classDef Sky :,stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C

```

### llm

Das llm-modul besteht aus zwei Anwendungen. 
1. Der Analyse des User Prompts
2. Die Generierung eines DnD Characters

**Analyse eines User Prompts**
```mermaid
---
title: Analyse User Prompt
---
classDiagram
direction TB
    class AnalyseUserPrompt {
	    + Summary
	    - Analyzes and rewrites user prompts to match specific character classes.
	    - Inherits from TalkToMistral to interact with a language model.
	    - Uses predefined system prompts to guide the rewriting process.
	    - Handles data retrieval and storage using CrudJsonFiles and DatabaseManager.
	    - Provides methods to generate and manage prompts for the language model.
	    + Methods
	    - rewrite() : Asks the language model to rewrite the user prompt and returns the response.
	    - generate_request_prompt() : Generates the prompt for the language model request by combining the system prompt and user prompt.
	    - prompt() : Property to get the user prompt.
	    - prompt.setter() : Setter method to define the user prompt.
    }
    class DatabaseManager {
	    + Summary
	    - Manages interactions with the database for storing and retrieving character data.
	    - Uses SQLAlchemy for database operations and handles various SQL exceptions.
	    - Supports saving and loading user prompts, character data, and related information.
	    - Provides methods for extracting and processing analyzed data.
	    - Includes debugging features to log and print intermediate data for verification.
	    + Methods
	    - save_user_prompt() : Saves user prompt data and related analyzed data to the database.
	    - load_character_prompts() : Loads character prompts and related data for a given idea_id.
	    - save_generated_characters() : Saves generated character data to the database.
	    - delete_character_by_idea_id() : Deletes a character idea and all related columns from the database.
	    - load_characters() : Loads all characters associated with a given idea_id from the database.
    }
    class TalkToMistral {
	    + Summary
	    - This class facilitates communication with the Mistral AI model.
	    - It initializes the Mistral client with an API key and sets the model to "mistral-small-latest".
	    - It provides methods to send prompts to the Mistral API and retrieve responses.
	    - It stores the latest response from the Mistral API.
	    - It handles cases where no response has been received yet.
	    + Methods
	    - ask() : Sends a prompt to the Mistral API and stores the response.
	    - response() : Returns the latest response from the Mistral API or a default message if no response is available.
    }
    class CrudJsonFiles {
	    + Summary
	    - Inherits from CrudBase to handle JSON file operations.
	    - Provides methods to save, load, and manage JSON data.
	    - Includes error handling for file operations.
	    - Supports creating new files and resetting existing files.
	    - Checks and creates directories if they do not exist.
	    + Methods
	    - data() : Property to get the data from the JSON file.
	    - data.setter() : Setter method to append new data to the JSON file.
	    - new_file() : Creates a new JSON file with the provided data.
	    - reset() : Resets the JSON file with optional new data.
	    - check_path() : Checks if the directory exists and creates it if it does not.
    }

    CrudJsonFiles --> AnalyseUserPrompt
    TalkToMistral <|-- AnalyseUserPrompt
    AnalyseUserPrompt --> DatabaseManager

	class AnalyseUserPrompt:::Rose
	class DatabaseManager:::Ash
	class TalkToMistral:::Peach
	class CrudJsonFiles:::Aqua

	classDef Rose :, stroke-width:5px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
	classDef Ash :, stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
	classDef Aqua :, stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
	classDef Peach :,stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D

```

**Generierung eines DnD Characters**
```mermaid
---
config:
  look: neo
  theme: base
title: Generate DnD Character
---
classDiagram
direction TB
    class DatabaseManager {
	    + Summary
	    - Manages interactions with the database for storing and retrieving character data.
	    - Uses SQLAlchemy for database operations and handles various SQL exceptions.
	    - Supports saving and loading user prompts, character data, and related information.
	    - Provides methods for extracting and processing analyzed data.
	    - Includes debugging features to log and print intermediate data for verification.
	    + Methods
	    - save_user_prompt() : Saves user prompt data and related analyzed data to the database.
	    - load_character_prompts() : Loads character prompts and related data for a given idea_id.
	    - save_generated_characters() : Saves generated character data to the database.
	    - delete_character_by_idea_id() : Deletes a character idea and all related columns from the database.
	    - load_characters() : Loads all characters associated with a given idea_id from the database.
    }
    class CharacterDataLoader {
	    + Summary
	    - This class is designed to load character data from local storage based on a given class name.
	    - It constructs file paths for base data, spells, levels, and subclasses.
	    - It uses `CrudJsonFiles` to retrieve and manage JSON data.
	    - The class supports 12 different character classes.
	    - It provides methods to fetch and return character data in a structured list.
	    + Methods
	    - class_data() : Retrieves and returns all class data, including base data, spells, level features, and subclasses.
	    - run() : Calls the class_data method to execute and return the character data.
    }
    class SystemRequestBuilder {
	    + Summary
	    - This class builds system messages by analyzing prompts and combining them with JSON data.
	    - It retrieves character data and rewritten user prompts to create detailed system prompts.
	    - It uses various helpers and managers for data handling and debugging.
	    - The class generates a list of system prompts, each tailored for a specific character.
	    - It supports debugging features to log and print intermediate data for verification.
	    + Methods
	    - generate_system_prompts() : Creates a list of system prompts, each containing a template, rewritten prompt, and necessary class data.
	    - add_class_data() : Loads class data and integrates it into a class data template.
	    - add_char_details() : Generates character details and replaces placeholders in the system message.
    }
    class CharacterBuilderApp {
	    + Summary
	    - This class serves as the main application for building characters using a language model.
	    - It combines `CharacterRequestBuilder` and `TalkToMistral` to generate character JSONs.
	    - It handles the generation of character prompts and the creation of characters based on these prompts.
	    - It supports debugging features to log and print intermediate data for verification.
	    - It saves the generated characters to a database.
	    + Methods
	    - generate_character_builder_prompts() : Returns a list of character builder prompts.
	    - generate_character() : Generates a character based on a given character prompt.
	    - run() : Generates a list of prompts, loops over them to create characters, and saves them to the database.
    }
    class TalkToMistral {
	    + Summary
	    - This class facilitates communication with the Mistral AI model.
	    - It initializes the Mistral client with an API key and sets the model to "mistral-small-latest".
	    - It provides methods to send prompts to the Mistral API and retrieve responses.
	    - It stores the latest response from the Mistral API.
	    - It handles cases where no response has been received yet.
	    + Methods
	    - ask() : Sends a prompt to the Mistral API and stores the response.
	    - response() : Returns the latest response from the Mistral API or a default message if no response is available.
    }
    DatabaseManager --> SystemRequestBuilder
    CharacterDataLoader --> SystemRequestBuilder
    SystemRequestBuilder --> CharacterBuilderApp
    DatabaseManager --> CharacterBuilderApp
    DatabaseManager <-- CharacterBuilderApp
    CharacterBuilderApp <-- TalkToMistral
	style CharacterBuilderApp :,stroke-width:5px
	class DatabaseManager:::Ash
	class CharacterDataLoader:::Pine
	class CharacterDataLoader:::Aqua
	class SystemRequestBuilder:::Peach
	class CharacterBuilderApp:::Rose
	class TalkToMistral:::Peach
	classDef Ash :, stroke-width:1px, stroke-dasharray:none, stroke:#999999, fill:#EEEEEE, color:#000000
	classDef Rose :, stroke-width:1px, stroke-dasharray:none, stroke:#FF5978, fill:#FFDFE5, color:#8E2236
	classDef Peach :, stroke-width:1px, stroke-dasharray:none, stroke:#FBB35A, fill:#FFEFDB, color:#8F632D
	classDef Pine :, stroke-width:1px, stroke-dasharray:none, stroke:#254336, fill:#27654A, color:#FFFFFF
	classDef Aqua :,stroke-width:1px, stroke-dasharray:none, stroke:#46EDC8, fill:#DEFFF8, color:#378E7A
```


