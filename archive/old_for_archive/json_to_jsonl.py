"""
converts all four files for a dnd class from json to jsonl

This is nececary, cause the mistral api only accepts jsonl files in the request body
"""
import json

class JsonToJsonl:
	def convert_json_to_jsonl(self, input_data, output_file):
		with open(output_file, 'w') as jsonl_file:
			for data in input_data:
				# if data is a list, the list is iteratet, so the jsonl format is not broken
				if isinstance(data, list):
					if isinstance(data, list):
					
						for item in data:
							jsonl_file.write(json.dumps(item) + '\n')
					else:
						jsonl_file.write(json.dumps(data) + '\n')
				else:
					jsonl_file.write(json.dumps(data) + '\n')

if __name__ == "__main__":
	from src.handle_data.character_data_loader import CharacterDataLoader
	
	loader = CharacterDataLoader("cleric")
	data = loader.run()
	
	converter = JsonToJsonl()
	converter.convert_json_to_jsonl(data, "cleric_test.jsonl")
	
		