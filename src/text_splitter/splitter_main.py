from src.text_splitter.text_splitter import TextSplitter
from src.handle_data.crud_txt import CrudTxtFiles

chat_main_path = "/Users/felipepietzsch/Masterschool/Ohne Titel/DnD_Characterbuilder-with-AI-integration/data/llm_test_files/ChatGPT"
chat_main_file = "/chat_gpt_text.txt"
chat_crud = CrudTxtFiles(chat_main_path + chat_main_file)

chat_text = chat_crud.data

gemini_main_path = "/Users/felipepietzsch/Masterschool/Ohne Titel/DnD_Characterbuilder-with-AI-integration/data/llm_test_files/Gemini"
gemini_main_file = "/gemini_text.txt"
gemini_crud = CrudTxtFiles(gemini_main_path + gemini_main_file)

gemini_text = gemini_crud.data

chat_splitter = TextSplitter(chat_main_path, file_name="chat_gpt_texts", split_um=10)
chat_splitter.splitup(chat_text)

gemini_splitter = TextSplitter(gemini_main_path, file_name="gemini_texts", split_um=10)
gemini_splitter.splitup(gemini_text)