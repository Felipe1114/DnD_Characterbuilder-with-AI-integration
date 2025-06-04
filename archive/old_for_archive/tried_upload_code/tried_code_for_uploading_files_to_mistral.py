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
