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




