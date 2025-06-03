from src.handle_data.crud_txt import CrudTxtFiles


def main():
	write_hello()
	
def write_hello():
	hello = "Hello World!!!"
	
	crud_txt.data = hello
	
	
if __name__ == "__main__":
	file_path = "./hello_world.txt"
	crud_txt = CrudTxtFiles(file_path)
	main()
	
