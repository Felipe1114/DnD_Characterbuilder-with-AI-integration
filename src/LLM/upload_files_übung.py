
from mistralai import Mistral
from mistralai.models.sdkerror import SDKError
from src.debug.debug_log import DebugLog
from src.LLM.talk_to_mistral import TalkToMistral


@DebugLog.debug_log
def upload_files_to_mistral():
	api_key = "EBBtyAxkHIZOWJcTz3AzsTH0xyDKcDKt"
	file_path = "../../debug_data/jsonl_test_files/test_beta-a7_2.jsonl"
	
	# code from github: https://github.com/mistralai/client-python/blob/main/docs/sdks/files/README.md#upload
	try:
		with Mistral(
				api_key=api_key,
		) as mistral:
			res = mistral.files.upload(file={
				"file_name": "test_beta-a7_2.jsonl",
				"content": open(file_path, "rb"),
			})
			
			# Handle response
			
			print(res)
	# catches the errors and giving the info, with file has been used
	except SDKError as e:
		file_path_message = f"\nfile wiht error: {file_path!r}; \n{e}"
		raise SDKError(file_path_message)

def upload_files_with_response():
	# TODO: test this code
	import os
	from mistralai import Mistral
	
	# Retrieve the API key from environment variables
	api_key = os.environ["MISTRAL_API_KEY"]
	
	# Specify model
	model = "mistral-small-latest"
	
	# Initialize the Mistral client
	client = Mistral(api_key=api_key)
	
	# If local document, upload and retrieve the signed url
	# uploaded_pdf = client.files.upload(
	#     file={
	#         "file_name": "uploaded_file.pdf",
	#         "content": open("uploaded_file.pdf", "rb"),
	#     },
	#     purpose="ocr"
	# )
	# signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
	
	# Define the messages for the chat
	messages = [
		{
			"role": "user",
			"content": [
				{
					"type": "text",
					"text": "what is the last sentence in the document"
				},
				{
					"type": "document_url",
					"document_url": "https://arxiv.org/pdf/1805.04770"
					# "document_url": signed_url.url
				}
			]
		}
	]
	
	# Get the chat response
	chat_response = client.chat.complete(
		model=model,
		messages=messages
	)
	
	# Print the content of the response
	print(chat_response.choices[0].message.content)


# Output:
# The last sentence in the document is:\n\n\"Zaremba, W., Sutskever, I., and Vinyals, O. Recurrent neural network regularization. arXiv:1409.2329, 2014.

if __name__ == "__main__":
	mistral = TalkToMistral()
	question = "I´ve send a Jsonl file to you, with the name: 'test_beta-a7_2.jsonl'. Please give me a summery of the content of the file"
	mistral.ask(question)
	res = mistral.response()
	print(res)