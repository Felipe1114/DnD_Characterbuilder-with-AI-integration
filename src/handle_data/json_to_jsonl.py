"""
converts all four files for a dnd class from json to jsonl

This is nececary, cause the mistral api only accepts jsonl files in the request body
"""
import json
class JsonToJsonl:
	def convert_json_to_jsonl(self, input_data, output_file):
		with open(output_file, 'w') as jsonl_file:
			for record in input_data:
				jsonl_file.write(json.dumps(record) + '\n')
		
		