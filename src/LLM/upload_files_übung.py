"""
# class daten laden
	class_data = load_class_data(class_name)

# convert class_data to JSONL
	convertted_data = []
	for data in class_data:
		jsonl_data = convert_json_to_jsonl(data)
		converted_data.append(jsonl_data)
		
	return converte_data
	
# converted_data an mistral senden
	data = convert_data(json_data)
	request.post(data)
	

"""

import json
import requests



url = "https://api.mistral.ai/v1/files"

mein_body = {
	"id": "497f6eca-6276-4993-bfeb-53cbbbba6f09",
	"object": "/Users/felipepietzsch/Masterschool/Ohne Titel/DnD_Characterbuilder-with-AI-integration/static_dnd_data/detailed_class_data/cleric",
	"bytes": 13000,
	"created_at": 1716963433,
	"filename": "clericcleric.jsonl",
	"purpose": "fine-tune",
	"sample_type": "pretrain",
	"num_lines": 0,
	"source": "upload"
}

headers = {
    "Authorization": f"Bearer EBBtyAxkHIZOWJcTz3AzsTH0xyDKcDKt", #TODO: API key muss aus .env kommen!!!!!!!
    "Content-Type": "application/json"
}

response = requests.post(url, json=mein_body, headers=headers)

if response.status_code == 200:
    print("Erfolg:", response.json())
else:
    print("Fehler:", response.status_code, response.text)


