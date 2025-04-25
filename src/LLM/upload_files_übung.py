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
from urllib.error import HTTPError

from mistralai import Mistral
import os
from src.debug.debug_log import DebugLog

def upload_files_to_mistral():
	api_key = "EBBtyAxkHIZOWJcTz3AzsTH0xyDKcDKt"
	url = "https://api.mistral.ai/v1/files" # nötig?
	file_path = "../../static_dnd_data/detailed_class_data/cleric/clericcleric.jsonl"
	
	# code from github
	with Mistral(
			api_key=api_key,
	) as mistral:
		res = mistral.files.upload(file={
			"file_name": "cleric_spells.json",
			"content": open(file_path, "rb"),
		})
		
		# Handle response
		print(res)
	
	# code from mistral-fine tuning
	"""#api_key = os.environ["MISTRAL_API_KEY"]
	
	client = Mistral(api_key=api_key)
	
	training_data = client.files.upload(
		file={
			"file_name": "cleric_test.jsonl",
			"content": open("cleric_test.jsonl", "rb"),
		}
	)
	
	# TODO die jsonl müssen mit bestimmten Keys ausgestattet sein
	# z.b message: [...]"""
	
	"""
	
	with open("cleric_test.jsonl", "rb") as f:
		files = {
		    "file": ("cleric_test.jsonl", f, "application/jsonl")
		}
		data = {
		    "purpose": "fine-tune",
		    "sample_type": "pretrain"
		}
		headers = {
		    "Authorization": f"Bearer {api_key}"
		}
		
		response = requests.post(url, headers=headers, files=files, data=data)
	
	if response.status_code == 422:
		raise ValueError(response.json())
	"""
	
upload_files_to_mistral()